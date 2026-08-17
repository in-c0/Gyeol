#!/usr/bin/env python3
"""Software surrogate for M1-C5 analog event + persistent-memory sensing.

This models representation dynamics only. It does not model device physics,
photophysics, circuit power, or whole-system energy.
"""
from __future__ import annotations

import argparse
import math
from collections.abc import Sequence


def decay_alpha(dt_s: float, tau_s: float) -> float:
    """Return exponential decay coefficient exp(-dt/tau)."""
    if dt_s <= 0:
        raise ValueError("dt_s must be > 0")
    if tau_s <= 0:
        raise ValueError("tau_s must be > 0")
    return math.exp(-dt_s / tau_s)


def event_memory_transform(
    event_frames: Sequence[Sequence[float]],
    *,
    dt_s: float,
    tau_s: float,
) -> tuple[list[list[float]], list[list[float]]]:
    """Produce fast-event and exponentially persistent-memory channels.

    For each channel c and timestep t:

        memory[t, c] = alpha * memory[t-1, c] + event[t, c]

    This is intentionally a simple linear reservoir surrogate. It is not a
    claim that a physical C5 sensor has exactly this transfer function.
    """
    alpha = decay_alpha(dt_s, tau_s)
    if not event_frames:
        return [], []

    width = len(event_frames[0])
    if width == 0:
        raise ValueError("event frames must have at least one channel")

    state = [0.0] * width
    fast_out: list[list[float]] = []
    memory_out: list[list[float]] = []

    for index, frame in enumerate(event_frames):
        if len(frame) != width:
            raise ValueError(
                f"inconsistent frame width at index {index}: expected {width}, got {len(frame)}"
            )
        fast = [float(value) for value in frame]
        state = [
            alpha * previous + current
            for previous, current in zip(state, fast)
        ]
        fast_out.append(fast)
        memory_out.append(state.copy())

    return fast_out, memory_out


def digital_accumulation_ops(steps: int, channels: int) -> dict[str, int]:
    """Count the minimal digital recurrence operations for the same reservoir.

    Accounting only: these counts are not an energy model.
    """
    if steps < 0:
        raise ValueError("steps must be >= 0")
    if channels < 0:
        raise ValueError("channels must be >= 0")
    updates = steps * channels
    return {
        "persistent_state_values": channels,
        "multiplies": updates,
        "adds": updates,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dt-ms", type=float, default=50.0)
    parser.add_argument("--tau-ms", type=float, default=250.0)
    args = parser.parse_args()

    frames = [[1.0], [0.0], [0.0], [-0.5], [0.0]]
    fast, memory = event_memory_transform(
        frames,
        dt_s=args.dt_ms / 1000.0,
        tau_s=args.tau_ms / 1000.0,
    )
    alpha = decay_alpha(args.dt_ms / 1000.0, args.tau_ms / 1000.0)

    print(f"alpha={alpha:.6f}")
    for index, (event, state) in enumerate(zip(fast, memory)):
        print(f"t={index:02d} event={event} memory={state}")
    print("digital-equivalent recurrence:", digital_accumulation_ops(len(frames), 1))


if __name__ == "__main__":
    main()
