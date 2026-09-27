# Firmware and software

## How Éclair shows up as a drive

Éclair needs **no driver** on Windows, macOS or Linux:

- **On a USB4 / Thunderbolt 3–4 port**, the ASM2464PD tunnels PCIe: the computer
  sees the M.2 SSD as a native **NVMe drive** (≈ 3.5 GB/s expected).
- **On a USB 3.x port** (or with the USB-A cable), the ASM2464PD presents the SSD as
  a **USB mass-storage device using UAS** (≈ 1 GB/s on 10 Gb/s USB).

This behaviour is implemented by ASMedia's firmware, stored in the SPI flash on the
board (U31, ZD25WQ16). The chip's firmware is closed: it cannot be rewritten, only
flashed and configured.

## Flashing a new board (once per board)

1. Get the firmware package and ASMedia's tool from the original open design:
   [Leaves232/2230-USB4-SSD-Enclosure-Design](https://github.com/Leaves232/2230-USB4-SSD-Enclosure-Design)
   (`ASM2464PD_FW_250123_85_00_00.zip`). It is **not redistributed here**
   (ASMedia's licence).
2. Plug the new board (with its SSD) into a Windows PC on a USB 3 port.
3. Run the ASMedia MP tool from the package, load the firmware `.bin`, flash, unplug.
4. Plug it again: a new disk appears. Check it with `eclair_check.py` below.

## eclair_check.py — is it seen, and how fast is it?

A small cross-platform script (Python 3, no dependency) that tells how the drive is
connected (NVMe over USB4, or USB) and measures its real sequential write and read
speed with a test file. **Not yet run on real Éclair hardware** (the boards are not
built yet); it runs on any drive today.

```
python eclair_check.py E:\          # Windows
python3 eclair_check.py /media/you/CARTOUCHE   # Linux / macOS
```

## CARTOUCHE software

Éclair runs the same CARTOUCHE software as the USB keys (local AI runtime, chat
interface, models). Two things change for Éclair and are planned in the software:

- **Preparing the drive** (CARTOUCHE Creator) is done on a USB 3 port, where Éclair is
  a USB disk, so the existing, safe "USB disks only" rule still applies.
- **Authenticity check**: the licence is bound to the drive's hardware identity. On
  USB4 the identity comes from the NVMe SSD instead of the USB bridge, so the
  licence stores both, and the runtime accepts either.
