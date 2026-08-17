import csv
import tempfile
import unittest
from pathlib import Path

from tools.validate_m4_candidates import REQUIRED_COLUMNS, validate_registry


class M4CandidateValidatorTests(unittest.TestCase):
    def write_rows(self, rows):
        tmp = tempfile.TemporaryDirectory()
        path = Path(tmp.name) / "candidates.csv"
        with path.open("w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=sorted(REQUIRED_COLUMNS))
            writer.writeheader()
            for row in rows:
                writer.writerow(row)
        return tmp, path

    def base_row(self):
        return {
            "id": "M4-T001",
            "candidate": "test candidate",
            "category": "EXPERIMENT_AMBIENT",
            "pressure_gpa": "0",
            "tc_onset_k": "100",
            "tc_zero_k": "90",
            "tc_magnetic_k": "80",
            "tc_predicted_k": "",
            "transport_evidence": "yes",
            "magnetic_evidence": "yes",
            "structure_evidence": "yes",
            "internal_repeat": "yes",
            "independent_specific_replication": "no",
            "phase_room_temp_stable": "unknown",
            "status": "ACTIVE",
            "validated_room_temp_ambient": "false",
            "primary_source": "10.example/test",
        }

    def test_current_registry_passes(self):
        errors = validate_registry(Path("moonshots/superconductors/M4-candidates.csv"))
        self.assertEqual([], errors)

    def test_room_temperature_validation_fails_without_all_evidence(self):
        row = self.base_row()
        row.update(
            {
                "tc_zero_k": "300",
                "tc_magnetic_k": "300",
                "validated_room_temp_ambient": "true",
            }
        )
        tmp, path = self.write_rows([row])
        try:
            errors = validate_registry(path)
        finally:
            tmp.cleanup()
        joined = "\n".join(errors)
        self.assertIn("independent specific replication", joined)
        self.assertIn("room-temperature phase stability", joined)

    def test_validated_room_temperature_state_can_pass_strict_gate(self):
        row = self.base_row()
        row.update(
            {
                "tc_zero_k": "300",
                "tc_magnetic_k": "295",
                "independent_specific_replication": "yes",
                "phase_room_temp_stable": "yes",
                "validated_room_temp_ambient": "true",
            }
        )
        tmp, path = self.write_rows([row])
        try:
            errors = validate_registry(path)
        finally:
            tmp.cleanup()
        self.assertEqual([], errors)

    def test_theory_candidate_cannot_claim_experimental_evidence(self):
        row = self.base_row()
        row.update(
            {
                "category": "THEORY_AMBIENT",
                "tc_predicted_k": "300",
                "transport_evidence": "yes",
                "magnetic_evidence": "yes",
            }
        )
        tmp, path = self.write_rows([row])
        try:
            errors = validate_registry(path)
        finally:
            tmp.cleanup()
        joined = "\n".join(errors)
        self.assertIn("theory-only candidate cannot claim transport evidence", joined)
        self.assertIn("theory-only candidate cannot claim magnetic evidence", joined)

    def test_disconfirmed_candidate_can_never_be_validated(self):
        row = self.base_row()
        row.update(
            {
                "category": "NEGATIVE_CONTROL",
                "status": "DISCONFIRMED",
                "validated_room_temp_ambient": "true",
            }
        )
        tmp, path = self.write_rows([row])
        try:
            errors = validate_registry(path)
        finally:
            tmp.cleanup()
        self.assertTrue(any("cannot be validated" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
