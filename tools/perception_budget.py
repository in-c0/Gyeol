#!/usr/bin/env python3
"""Architecture-level bandwidth model for Gyeol perception pipelines.

Models data movement, not whole-device power. Use this to pre-register break-even
points before hardware measurements are available.
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class FrameStream:
    width: int = 1920
    height: int = 1080
    fps: float = 30.0
    bits_per_pixel: float = 12.0

    @property
    def megabytes_per_second(self) -> float:
        return self.width * self.height * self.fps * self.bits_per_pixel / 8 / 1_000_000


def event_mb_s(events_per_second: float, bytes_per_event: float) -> float:
    return events_per_second * bytes_per_event / 1_000_000


def main() -> None:
    rgb = FrameStream()
    print(f"RGB baseline: {rgb.megabytes_per_second:.2f} MB/s ({rgb.width}x{rgb.height}@{rgb.fps:g}, {rgb.bits_per_pixel:g} bpp)")

    # 8 B/event is a conservative software-record representation, not a claim
    # about any sensor's physical wire format.
    for eps in (100_000, 500_000, 1_000_000, 5_000_000):
        ev = event_mb_s(eps, 8)
        print(f"Events: {eps/1e6:.1f} Mev/s @ 8 B/event -> {ev:.2f} MB/s; RGB/event ratio {rgb.megabytes_per_second/ev:.2f}x")

    semantic = 10 * 64 / 1_000_000
    print(f"Semantic state: 10 events/s @ 64 B/event -> {semantic:.6f} MB/s; RGB/semantic ratio {rgb.megabytes_per_second/semantic:,.0f}x")

    for bytes_per_event in (4, 8, 16):
        break_even_eps = rgb.megabytes_per_second * 1_000_000 / bytes_per_event
        print(f"Break-even vs RGB at {bytes_per_event} B/event: {break_even_eps/1e6:.2f} Mev/s")


if __name__ == "__main__":
    main()
