import math
import unittest

from tools.c5_event_memory_surrogate import (
    decay_alpha,
    digital_accumulation_ops,
    event_memory_transform,
)


class C5EventMemorySurrogateTests(unittest.TestCase):
    def test_impulse_decays_exponentially(self):
        dt_s = 0.1
        tau_s = 0.2
        alpha = math.exp(-dt_s / tau_s)
        _, memory = event_memory_transform(
            [[1.0], [0.0], [0.0]],
            dt_s=dt_s,
            tau_s=tau_s,
        )
        self.assertAlmostEqual(1.0, memory[0][0])
        self.assertAlmostEqual(alpha, memory[1][0])
        self.assertAlmostEqual(alpha * alpha, memory[2][0])

    def test_memory_distinguishes_recent_history_when_fast_channel_matches(self):
        _, a_memory = event_memory_transform(
            [[1.0], [0.0]], dt_s=0.05, tau_s=0.25
        )
        _, b_memory = event_memory_transform(
            [[0.0], [0.0]], dt_s=0.05, tau_s=0.25
        )
        self.assertEqual(0.0, b_memory[-1][0])
        self.assertGreater(a_memory[-1][0], b_memory[-1][0])

    def test_multiple_channels_are_independent(self):
        _, memory = event_memory_transform(
            [[1.0, 0.0], [0.0, 2.0]], dt_s=0.1, tau_s=0.2
        )
        alpha = math.exp(-0.5)
        self.assertAlmostEqual(alpha, memory[-1][0])
        self.assertAlmostEqual(2.0, memory[-1][1])

    def test_rejects_invalid_time_constants_and_shape(self):
        with self.assertRaises(ValueError):
            decay_alpha(0.0, 1.0)
        with self.assertRaises(ValueError):
            decay_alpha(1.0, 0.0)
        with self.assertRaises(ValueError):
            event_memory_transform([[]], dt_s=0.1, tau_s=0.2)
        with self.assertRaises(ValueError):
            event_memory_transform([[1.0], [1.0, 2.0]], dt_s=0.1, tau_s=0.2)

    def test_digital_accumulation_operation_accounting(self):
        self.assertEqual(
            {
                "persistent_state_values": 4,
                "multiplies": 40,
                "adds": 40,
            },
            digital_accumulation_ops(10, 4),
        )
        with self.assertRaises(ValueError):
            digital_accumulation_ops(-1, 4)


if __name__ == "__main__":
    unittest.main()
