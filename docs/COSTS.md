# Cost of one CARTOUCHE Éclair (USB4 drive), per capacity

Each line says where the number comes from. **Real** = a quote or a public
price; **estimate** = our assumption until the supplier quotes it.

![component cost](component-cost.png)

## Complete board (PCB + parts + assembly)

| Item | First batch of 10 | Batch of 100 | Source |
|---|---|---|---|
| Parts except the USB4 chip | 8.50 € | 8.50 € | **real**: Huaqiu BOM quote, 65.71 CNY |
| ASM2464PD (USB4 chip) | 24.50 € ($26.60) | 23.60 € ($25.60) | **real**: Alibaba price for 1–99 / 100–499 pcs |
| Bare 4-layer PCB, 22 × 34 mm, controlled impedance | ≈ 12 € | ≈ 2.50 € | estimate (to re-quote with the new Gerbers) |
| Assembly (PCBA, BGA) | ≈ 10 € | ≈ 3 € | estimate (NextPCB advertises a free first assembly) |
| **Complete board** | **≈ 55 €** | **≈ 38 €** | |

## Everything around it

| Item | Batch of 10 | Batch of 100 | Source |
|---|---|---|---|
| Aluminium case, CNC, anodised, laser-engraved | ≈ 35 € | ≈ 15 € | estimate (to quote once the case is drawn) |
| Thermal pad + screws | 1 € | 1 € | estimate |
| USB-A → USB-C cable, 10 Gb/s, 0.5 m (any computer) | 10 € | 10 € | **real**: found by the maker |
| USB-C ↔ USB-C cable, USB4 40 Gb/s, 0.5 m (full speed) | ≈ 15 € | ≈ 15 € | **real** prices seen: 14.90 € (0.5 m), $13.99 (UGREEN 1 m, sale) |
| Box, foam, printed notice | ≈ 3 € | ≈ 3 € | estimate |
| Shipping, Colissimo home delivery, 250 g | 5.49 € | 5.49 € | **real**: La Poste 2026 rate (free for the customer above 59 €) |

## Per capacity

SSD prices are retail estimates for an M.2 2230 NVMe (2 TB: $120–140 seen).
Card fees: Stripe ≈ 1.5 % + 0.25 €. Micro-enterprise contributions on sales
(France): ≈ 12.4 % of the price.

| Capacity | SSD | Total cost (10 / 100) | Price | Left per unit (10 / 100) |
|---|---|---|---|---|
| 256 GB | ≈ 30 € | 154 € / 117 € | 249 € | 60 € / 97 € |
| 512 GB | ≈ 45 € | 169 € / 132 € | 299 € | 88 € / 125 € |
| 1 TB | ≈ 80 € | 204 € / 167 € | 399 € | 139 € / 176 € |
| 2 TB | ≈ 130 € | 254 € / 217 € | 599 € | 261 € / 298 € |

Not included: one-off costs of the first run (stencil, CNC programming), the
first prototypes that may need a second revision, and income tax.

Two cables ship in the box: the USB-A one works on any computer (about 1 GB/s,
the 10 Gb/s USB limit); the USB-C 40 Gb/s one gives full USB4 speed (≈ 3.5 GB/s)
on a USB4 / Thunderbolt port.

## What to buy besides the assembled board

The assembler (NextPCB, turnkey PCBA) buys and solders every part of the BOM
(regulators, USB-C connector, M.2 connector, crystal, flash, passives). Ask them
to source the **ASM2464PD** too: it was missing from the original BOM match. If
they can't, JLCPCB lists it (part C7509569), or buy it on Alibaba ($26.60) and
send it to the assembler (consigned part).

Per drive, bought separately:

| Part | Where | Per drive |
|---|---|---|
| M.2 2230 NVMe SSD (256 GB – 2 TB), e.g. WD SN740, Kioxia BG6, Corsair MP600 Mini | retail | 30–130 € |
| Aluminium case, 2 halves, CNC + anodised + laser-engraved | CNC supplier (from the STEP model) | ≈ 15–35 € |
| Thermal pad 1 mm, ≥ 12 W/mK: cut 10 × 10 mm for the ASM2464PD, 22 × 20 mm for the SSD | one 100 × 100 mm sheet (≈ 10 €) does about 25 drives | ≈ 0.40 € |
| 3 × M2 × 3 mm screws (board to case ×2, SSD ×1) | M.2 screw kit (≈ 1–10 €) | ≈ 0.20 € |
| USB-C 40 Gb/s cable + USB-A 10 Gb/s cable | retail | ≈ 25 € |
| Box, foam insert, printed notice | packaging supplier / print shop | ≈ 3 € |

One-off: a Windows PC to flash the ASMedia firmware once per board (free tool
from the original project), and a USB4 or Thunderbolt computer to measure the
real speed.
