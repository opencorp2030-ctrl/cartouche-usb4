#!/usr/bin/env python3
"""eclair_check — how is a CARTOUCHE Éclair connected, and how fast is it?

Usage: eclair_check.py <path on the drive> [size in MB, default 2048]

Writes a test file on the drive, reads it back, prints MB/s, then removes it.
On Windows it also asks the system which bus the disk is on (NVMe = USB4 tunnel,
USB = USB 3 fallback). The read is done right after the write, so on computers
with a lot of free memory part of it may come from the cache: a second run after
unplugging and replugging gives the cold figure.
"""
import os
import subprocess
import sys
import time


def bus_type(path):
    if os.name != "nt":
        return "?"
    letter = os.path.splitdrive(os.path.abspath(path))[0].rstrip(":")
    ps = f"(Get-Partition -DriveLetter {letter} | Get-Disk).BusType"
    try:
        return subprocess.run(["powershell", "-NoProfile", "-Command", ps], capture_output=True, text=True, timeout=30).stdout.strip() or "?"
    except Exception:
        return "?"


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    root, mb = sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else 2048
    test = os.path.join(root, "eclair_check.tmp")
    block = os.urandom(16 << 20)
    n = max(1, mb // 16)
    t = time.perf_counter()
    with open(test, "wb", buffering=0) as f:
        for _ in range(n):
            f.write(block)
        os.fsync(f.fileno())
    w = n * 16 / (time.perf_counter() - t)
    t = time.perf_counter()
    with open(test, "rb", buffering=0) as f:
        while f.read(16 << 20):
            pass
    r = n * 16 / (time.perf_counter() - t)
    os.remove(test)
    bus = bus_type(root)
    link = {"NVMe": "USB4 / Thunderbolt (PCIe tunnel)", "USB": "USB 3 (UAS)"}.get(bus, "unknown")
    print(f"bus: {bus} -> {link}")
    print(f"write: {w:,.0f} MB/s   read: {r:,.0f} MB/s   ({n * 16} MB)")
    if bus == "USB" and r > 0:
        print("tip: on a USB4 or Thunderbolt port, with the USB-C 40 Gb/s cable, Éclair runs as NVMe (≈ 3.5 GB/s expected)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
