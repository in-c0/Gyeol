#!/usr/bin/env python3
"""Deterministically select the B-001 EPIC-KITCHENS video manifest.

Stdlib-only so it can run in research CI and on a fresh clone.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
from collections import defaultdict
from pathlib import Path


DEFAULT_PARTICIPANTS = [f"P{i:02d}" for i in range(1, 6)]


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def participant_for(row: dict[str, str]) -> str:
    participant = (row.get("participant_id") or "").strip()
    if participant:
        return participant
    video_id = (row.get("video_id") or "").strip()
    if "_" in video_id:
        return video_id.split("_", 1)[0]
    raise ValueError("row has neither participant_id nor inferable video_id")


def parse_exclusions(values: list[str]) -> dict[str, str]:
    exclusions: dict[str, str] = {}
    for value in values:
        if "=" not in value:
            raise ValueError(f"exclusion must be VIDEO_ID=reason, got {value!r}")
        video_id, reason = value.split("=", 1)
        video_id = video_id.strip()
        reason = reason.strip()
        if not video_id or not reason:
            raise ValueError(f"exclusion must contain non-empty video ID and reason: {value!r}")
        if video_id in exclusions:
            raise ValueError(f"duplicate exclusion for {video_id}")
        exclusions[video_id] = reason
    return exclusions


def select_videos(
    csv_path: Path,
    participants: list[str],
    videos_per_participant: int = 2,
    clip_max_duration_s: int = 600,
    exclusions: dict[str, str] | None = None,
) -> dict:
    exclusions = exclusions or {}
    videos: dict[str, set[str]] = defaultdict(set)
    row_count = 0

    with csv_path.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        missing = {"video_id"}.difference(reader.fieldnames or [])
        if missing:
            raise ValueError(f"missing required CSV columns: {sorted(missing)}")
        for row in reader:
            row_count += 1
            participant = participant_for(row)
            if participant not in participants:
                continue
            video_id = (row.get("video_id") or "").strip()
            if video_id:
                videos[participant].add(video_id)

    all_selected_participant_videos = set().union(*(videos[p] for p in participants))
    unknown_exclusions = sorted(set(exclusions).difference(all_selected_participant_videos))
    if unknown_exclusions:
        raise ValueError(f"excluded video IDs not present in selected participants: {unknown_exclusions}")

    selections = []
    for participant in participants:
        ordered = sorted(
            video_id
            for video_id in videos.get(participant, set())
            if video_id not in exclusions
        )
        if len(ordered) < videos_per_participant:
            raise ValueError(
                f"{participant}: need {videos_per_participant} non-excluded videos, found {len(ordered)}"
            )
        chosen = ordered[:videos_per_participant]
        for index, video_id in enumerate(chosen):
            split = "tuning" if index == 0 else "held_out" if index == 1 else f"extra_{index}"
            selections.append(
                {
                    "participant_id": participant,
                    "video_id": video_id,
                    "split": split,
                    "clip_start_s": 0,
                    "clip_max_duration_s": clip_max_duration_s,
                }
            )

    return {
        "schema_version": 1,
        "experiment": "B-001-event-first-perception",
        "source": {
            "path": csv_path.name,
            "sha256": sha256_file(csv_path),
            "rows": row_count,
        },
        "selection_rule": {
            "participants": participants,
            "videos_per_participant": videos_per_participant,
            "ordering": "lexicographic video_id after recorded exclusions",
            "clip_start_s": 0,
            "clip_max_duration_s": clip_max_duration_s,
        },
        "videos": selections,
        "exclusions": [
            {"video_id": video_id, "reason": exclusions[video_id]}
            for video_id in sorted(exclusions)
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("annotations_csv", type=Path)
    parser.add_argument("--participants", nargs="+", default=DEFAULT_PARTICIPANTS)
    parser.add_argument("--videos-per-participant", type=int, default=2)
    parser.add_argument("--clip-max-duration-s", type=int, default=600)
    parser.add_argument(
        "--exclude",
        action="append",
        default=[],
        metavar="VIDEO_ID=REASON",
        help="record an unavailable/corrupt video before deterministic substitution",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("experiments/results/B-001-manifest.json"),
    )
    args = parser.parse_args()

    try:
        exclusions = parse_exclusions(args.exclude)
    except ValueError as exc:
        parser.error(str(exc))

    manifest = select_videos(
        args.annotations_csv,
        args.participants,
        args.videos_per_participant,
        args.clip_max_duration_s,
        exclusions,
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {len(manifest['videos'])} videos to {args.output}")
    for item in manifest["videos"]:
        print(f"{item['split']:8} {item['participant_id']} {item['video_id']}")
    for item in manifest["exclusions"]:
        print(f"excluded {item['video_id']}: {item['reason']}")


if __name__ == "__main__":
    main()
