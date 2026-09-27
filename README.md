# CARTOUCHE USB4 — a tiny USB4 NVMe drive for a local AI

![CARTOUCHE USB4](images/banner.png)

A tiny board that turns an **M.2 2230 NVMe SSD** into a **USB4 (40 Gb/s) drive**
with a **single USB-C port**. The board is **22.0 × 33.7 mm**, as small as the
electronics allow, because it goes inside a closed case: the whole drive, SSD
plugged in, is about **22 × 56 mm**. The CARTOUCHE name is engraved on the case,
not printed on the board.

It is the hardware for [CARTOUCHE](https://cartouche.candygate.eu): a complete AI
assistant that runs **offline, from the drive itself**. You plug it into any
Windows, macOS or Linux computer, double-click, and chat with an open-source
language model. Nothing is installed on the computer and nothing is sent to the
Internet.

| Top | Bottom |
|---|---|
| ![top](images/top.png) | ![bottom](images/bottom.png) |

## Why this board

A local AI reads **billions of bytes** every time it starts: a 3 GB model has to be
read from the drive before the first answer. Today CARTOUCHE ships on USB flash
keys. We measured what that means on the same computer:

| Drive | Read speed | Time to read a 3 GB model |
|---|---|---|
| Ordinary USB key (measured) | 18 MB/s | ~167 s |
| Portable hard drive, Seagate One Touch (measured) | 125 MB/s | ~24 s |
| Best USB flash key we sell, SanDisk (manufacturer figure) | up to 400 MB/s | ~8 s |
| **This board, USB4 + NVMe (expected)** | **~3,500 MB/s** | **< 1 s** |

The larger models (9B–30B parameters, 6–14 GB) are the ones that give really good
answers, and they are exactly the ones that are painful to load from a key. With
USB4 and an NVMe SSD, even a 14 GB model loads in a few seconds, and the drive
is smaller than most USB keys' packaging. CARTOUCHE means *cartridge*: you plug
your AI in like a game.

## What it is

| | |
|---|---|
| Bridge chip | ASMedia **ASM2464PD** (USB4 40 Gb/s ↔ PCIe 4.0 x4) |
| Storage | M.2 **2230** NVMe SSD, plugged in line at the end of the board. Planned: **256 GB**, or **1 TB** if our supplier can; 2 TB max (3.3 V power budget) |
| Connector | one USB-C (USB4 / Thunderbolt 3–4, falls back to USB 3.2 and USB 3.0) |
| Expected speed | ~3.5–3.8 GB/s on USB4/Thunderbolt, ~1 GB/s on USB 3.2 10 Gb/s |
| PCB | 4 layers, 1.6 mm, 85 Ω controlled impedance, 3.5 mil tracks, 0.3/0.2 mm vias, ENIG |
| Board size | **22.0 × 33.7 mm** (≈ 22 × 56 mm with the SSD) |

## Credit: what is ours and what is not

The electronic core (schematic, USB4/PCIe routing, power supplies) comes from the
open-source project
**[Leaves232/2230-USB4-SSD-Enclosure-Design](https://github.com/Leaves232/2230-USB4-SSD-Enclosure-Design)**
(MIT licence, see [`LICENSE-upstream-MIT`](LICENSE-upstream-MIT)), whose author
built and tested it with a 2 TB Hynix P44 Pro SSD.

For CARTOUCHE we:

- converted the original Altium design to **KiCad 9** (reproducible scripts in [`scripts/`](scripts));
- kept the original, smallest possible outline and removed everything that only
  made sense on an open board (v1.0 was a 30 × 64 mm cartridge with a printed
  name: pointless once the board lives in a case);
- made the **fabrication package** (Gerbers with separate plated / non-plated
  drills, pick-and-place, 1:1 template) and a **STEP model** to design the case.

The original author's signature on the back of the board is kept.

The high-speed area (USB4, PCIe) was **not modified**: it is the part that was
proven to work.

## Files

| File | What it is |
|---|---|
| `cartouche-usb4.kicad_pcb`, `.kicad_pro` | KiCad 9 project |
| `fab/cartouche-usb4-gerbers.zip` | Gerbers and drill files, ready for the fab |
| `fab/gerbers/` | the same, unzipped |
| `fab/cartouche-usb4.step` | 3D model of the assembled board, to design the case |
| `fab/positions.csv` | component positions (pick and place) |
| `fab/nomenclature-BOM.xlsx` | bill of materials (from the original design) |
| `fab/devis-composants-reference.xlsx` | reference component quote (from the original design) |
| `fab/exigences-fabrication.xlsx` | original fabrication requirements |
| `fab/gabarit-1-1.pdf` | 1:1 outline and courtyards |
| `scripts/` | Altium → KiCad import and cartridge generation |

## How to get it made

Same settings as the original board (made at Huaqiu / NextPCB):

- 4 layers · FR-4 TG150 · 1.6 mm · ENIG · 1 oz outer / 0.5 oz inner copper
- **controlled impedance: 85 Ω differential pairs on the outer layers**
- tracks/spacing 3.5/3.5 mil · 0.2 mm vias, tented
- **assembly by the fab (PCBA)**: the ASM2464PD is a 0.46 mm pitch BGA, it cannot be soldered by hand

Notes:

- Do **not** refill the copper zones in KiCad (shortcut B): the planes are the ones
  from the original board. The DRC reports 507 zone clearance items, 199 solder-mask
  bridges under the BGA, 5 hole/zone items and 3 items at the board edge (the M.2
  connector's legs, where the SSD plugs in). They all come from the original board
  as it was manufactured, not real errors (0 unconnected).
- **The case holds the SSD** (an M2 screw boss or a stop at the SSD's end), since the
  board no longer carries the screw.
- **Cooling is mandatory**: the ASM2464PD needs a thermal pad to the case,
  otherwise it overheats and disconnects. An aluminium case doubles as the heatsink.
- A new board must be flashed once with the ASMedia tool and firmware provided in
  the original repository (not redistributed here).

## Cost

See [`docs/COSTS.md`](docs/COSTS.md): about 8.5 € of components per board (real quote), plus the ASM2464PD, the PCB, assembly, SSD, cable and case.

## Status

Designed, not built yet. Next steps: order 5 assembled boards, design the
aluminium case from the STEP model (engraved name, SSD holder, heatsink), then
measure real load times with CARTOUCHE.

A French version of this README is in [`README.fr.md`](README.fr.md).

## Licence

MIT, like the original design. See [`LICENSE`](LICENSE) and
[`LICENSE-upstream-MIT`](LICENSE-upstream-MIT).
