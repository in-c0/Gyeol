import csv
import tempfile
import unittest
from pathlib import Path

from tools.select_epic_manifest import select_videos


class SelectEpicManifestTests(unittest.TestCase):
    def write_fixture(self, root: Path) -> Path:
        path = root / "annotations.csv"
        with path.open("w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(
                f,
                fieldnames=["participant_id", "video_id", "start_timestamp", "stop_timestamp"],
            )
            writer.writeheader()
            for participant in [f"P{i:02d}" for i in range(1, 6)]:
                # Deliberately unsorted and duplicated: selection must be deterministic.
                for video_id in (
                    f"{participant}_03",
                    f"{participant}_01",
                    f"{participant}_02",
                    f"{participant}_01",
                ):
                    writer.writerow(
                        {
                            "participant_id": participant,
                            "video_id": video_id,
                            "start_timestamp": "00:00:01",
                            "stop_timestamp": "00:00:02",
                        }
                    )
        return path

    def test_selects_first_two_unique_videos_per_participant(self):
        with tempfile.TemporaryDirectory() as tmp:
            csv_path = self.write_fixture(Path(tmp))
            manifest = select_videos(
                csv_path,
                [f"P{i:02d}" for i in range(1, 6)],
            )

        expected = []
        for participant in [f"P{i:02d}" for i in range(1, 6)]:
            expected.extend(
                [
                    (participant, f"{participant}_01", "tuning"),
                    (participant, f"{participant}_02", "held_out"),
                ]
            )
        actual = [
            (item["participant_id"], item["video_id"], item["split"])
            for item in manifest["videos"]
        ]
        self.assertEqual(expected, actual)
        self.assertEqual(10, len(manifest["videos"]))
        self.assertEqual(600, manifest["selection_rule"]["clip_max_duration_s"])
        self.assertEqual(40, manifest["source"]["rows"])
        self.assertEqual(64, len(manifest["source"]["sha256"]))

    def test_fails_closed_when_participant_has_too_few_videos(self):
        with tempfile.TemporaryDirectory() as tmp:
            csv_path = Path(tmp) / "annotations.csv"
            csv_path.write_text(
                "participant_id,video_id\nP01,P01_01\n",
                encoding="utf-8",
            )
            with self.assertRaisesRegex(ValueError, "need 2 videos"):
                select_videos(csv_path, ["P01"])


if __name__ == "__main__":
    unittest.main()
