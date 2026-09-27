# Cost estimate (prototype, 5 boards)

Component prices come from the original design's real BOM quote from Huaqiu
(`fab/devis-composants-reference.xlsx`, tax included, 2025): **65.71 CNY
(≈ 8.5 €) per board, without the ASM2464PD**, which is sold separately and has no
public price (to be quoted by the assembler or sourced from an ASMedia distributor).

![component cost](component-cost.png)

| Item | Per unit | Status |
|---|---|---|
| Components except ASM2464PD | ≈ 8.5 € | real quote (Huaqiu) |
| ASM2464PD | to be quoted | no public price found |
| 4-layer impedance PCB, 22 × 34 mm | to be re-quoted | the $139 quote was for the old 30 × 64 mm board |
| Assembly (PCBA, BGA) | to be quoted | NextPCB advertises free assembly on a first order (up to $500) |
| M.2 2230 NVMe SSD, 256 GB | ≈ 25–40 € | retail, plugged in by hand (no soldering) |
| M.2 2230 NVMe SSD, 1 TB | to be checked | retail |
| USB-A → USB-C cable, 10 Gb/s, 0.5 m | ≈ 10 € | found by the maker |
| Case (engraved) | to be designed | from `fab/cartouche-usb4.step` |

Note: a 10 Gb/s USB-A cable limits the drive to about 1 GB/s. Full USB4 speed
(≈ 3.5 GB/s) needs a USB-C 40 Gb/s (USB4 / Thunderbolt) cable and port.
