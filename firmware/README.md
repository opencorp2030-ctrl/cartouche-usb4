# Firmware and software

## How Éclair shows up

| Port | Seen by the computer as | Expected speed |
|---|---|---|
| USB4 / Thunderbolt 3–4 | native NVMe drive (PCIe tunnelled by the ASM2464PD) | ≈ 3.5 GB/s |
| USB 3.x, or with the USB-A cable | USB mass storage (UAS) | ≈ 1 GB/s |

- Driver: none needed (Windows, macOS, Linux).
- Firmware: ASMedia, closed source, in the SPI flash on the board (U31, ZD25WQ16). It can only be flashed and configured.

## Flashing a new board (once per board)

1. Get the firmware package and ASMedia's tool from
   [Leaves232/2230-USB4-SSD-Enclosure-Design](https://github.com/Leaves232/2230-USB4-SSD-Enclosure-Design)
   (`ASM2464PD_FW_250123_85_00_00.zip`). Not redistributed here (ASMedia's licence).
2. Plug the new board (with its SSD) into a Windows PC on a USB 3 port.
3. Run the ASMedia MP tool, load the firmware `.bin`, flash, unplug.
4. Plug it again: a new disk appears. Check it with `eclair_check.py`.

## eclair_check.py

Python 3, no dependency. Shows how the drive is connected (NVMe over USB4, or USB)
and measures sequential write and read speed with a test file.
Status: works on any drive; not run on real Éclair hardware yet (boards not built).

```
python eclair_check.py E:\                      # Windows
python3 eclair_check.py /media/you/CARTOUCHE    # Linux / macOS
```

## CARTOUCHE software

| Step | On Éclair |
|---|---|
| Runtime | same CARTOUCHE software as the USB keys (local AI runtime, chat interface, models) |
| Preparing the drive (CARTOUCHE Creator) | on a USB 3 port, where Éclair is a USB disk |
| Authenticity check | licence bound to the NVMe SSD's identity on USB4, or to the USB bridge on USB 3 (CARTOUCHE 1.0.9) |
