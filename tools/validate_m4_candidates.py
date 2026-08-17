#!/usr/bin/env python3
"""Validate the machine-readable M4 superconductivity candidate registry.

The validator is intentionally conservative. It does not decide whether a material
is superconducting; it prevents unsupported evidence states from being encoded as
validated room-temperature ambient-pressure superconductivity.
"""
from __future__ import annotations

import argparse
import csv
from pathlib import Path


REQUIRED_COLUMNS = {
    "id",
    "candidate",
    "category",
    "pressure_gpa",
    "tc_onset_k",
    "tc_zero_k",
    "tc_magnetic_k",
    "tc_predicted_k",
    "transport_evidence",
    "magnetic_evidence",
    "structure_evidence",
    "internal_repeat",
    "independent_specific_replication",
    "phase_room_temp_stable",
    "status",
    "validated_room_temp_ambient",
    "primary_source",
}

TRUE_VALUES = {"true", "yes"}
FALSE_VALUES = {"false", "no"}

# Deliberately conservative evidence-gate definitions, not universal physics terms.
# 0.001 GPa = 1 MPa (~10 bar): intentionally looser than atmospheric pressure
# to tolerate metadata/experimental reporting while excluding genuinely pressurized states.
AMBIENT_PRESSURE_MAX_GPA = 0.001
# 293.15 K = 20 °C: lower bound for the repository's "room-temperature" validation label.
ROOM_TEMPERATURE_MIN_K = 293.15


def text(row: dict[str, str], key: str) -> str:
    return (row.get(key) or "").strip()


def parse_float(row: dict[str, str], key: str) -> float | None:
    value = text(row, key)
    if not value:
        return None
    try:
        return float(value)
    except ValueError as exc:
        raise ValueError(f"{text(row, 'id')}: {key} must be numeric or blank, got {value!r}") from exc


def validate_registry(path: Path) -> list[str]:
    errors: list[str] = []
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        fields = set(reader.fieldnames or [])
        missing = REQUIRED_COLUMNS - fields
        if missing:
            return [f"missing required columns: {sorted(missing)}"]
        rows = list(reader)

    seen_ids: set[str] = set()
    for line_number, row in enumerate(rows, start=2):
        candidate_id = text(row, "id")
        prefix = candidate_id or f"line {line_number}"
        if not candidate_id:
            errors.append(f"line {line_number}: empty id")
            continue
        if candidate_id in seen_ids:
            errors.append(f"{prefix}: duplicate id")
        seen_ids.add(candidate_id)

        try:
            pressure = parse_float(row, "pressure_gpa")
            tc_zero = parse_float(row, "tc_zero_k")
            tc_magnetic = parse_float(row, "tc_magnetic_k")
            tc_predicted = parse_float(row, "tc_predicted_k")
        except ValueError as exc:
            errors.append(str(exc))
            continue

        category = text(row, "category")
        status = text(row, "status")
        validated = text(row, "validated_room_temp_ambient").lower()

        if validated not in TRUE_VALUES | FALSE_VALUES:
            errors.append(f"{prefix}: validated_room_temp_ambient must be true/false")

        if category == "THEORY_AMBIENT":
            if tc_predicted is None:
                errors.append(f"{prefix}: theory candidate requires tc_predicted_k")
            if text(row, "transport_evidence").lower() == "yes":
                errors.append(f"{prefix}: theory-only candidate cannot claim transport evidence")
            if text(row, "magnetic_evidence").lower() == "yes":
                errors.append(f"{prefix}: theory-only candidate cannot claim magnetic evidence")

        if category == "NEGATIVE_CONTROL" and status not in {"DISCONFIRMED", "RETRACTED"}:
            errors.append(f"{prefix}: negative control must remain DISCONFIRMED or RETRACTED")

        if status in {"DISCONFIRMED", "RETRACTED"} and validated in TRUE_VALUES:
            errors.append(f"{prefix}: disconfirmed/retracted candidate cannot be validated")

        if validated in TRUE_VALUES:
            if pressure is None or pressure > AMBIENT_PRESSURE_MAX_GPA:
                errors.append(
                    f"{prefix}: validated ambient state requires pressure "
                    f"<={AMBIENT_PRESSURE_MAX_GPA} GPa"
                )
            if tc_zero is None or tc_zero < ROOM_TEMPERATURE_MIN_K:
                errors.append(
                    f"{prefix}: validated room-temperature state requires tc_zero_k "
                    f">={ROOM_TEMPERATURE_MIN_K}"
                )
            if tc_magnetic is None or tc_magnetic < ROOM_TEMPERATURE_MIN_K:
                errors.append(
                    f"{prefix}: validated room-temperature state requires tc_magnetic_k "
                    f">={ROOM_TEMPERATURE_MIN_K}"
                )
            if text(row, "transport_evidence").lower() != "yes":
                errors.append(f"{prefix}: validated state requires transport evidence")
            if text(row, "magnetic_evidence").lower() != "yes":
                errors.append(f"{prefix}: validated state requires magnetic evidence")
            if text(row, "structure_evidence").lower() != "yes":
                errors.append(f"{prefix}: validated state requires structure/phase evidence")
            if text(row, "independent_specific_replication").lower() != "yes":
                errors.append(f"{prefix}: validated state requires independent specific replication")
            if text(row, "phase_room_temp_stable").lower() != "yes":
                errors.append(f"{prefix}: validated state requires room-temperature phase stability")

        if not text(row, "primary_source"):
            errors.append(f"{prefix}: primary_source is required")

    return errors


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "registry",
        nargs="?",
        type=Path,
        default=Path("moonshots/superconductors/M4-candidates.csv"),
    )
    args = parser.parse_args()
    errors = validate_registry(args.registry)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        raise SystemExit(1)
    print(f"M4 registry valid: {args.registry}")


if __name__ == "__main__":
    main()
