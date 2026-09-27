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
| USB-A → USB-C cable, 10 Gb/s, 0.5 m | 10 € | 10 € | **real**: found by the maker |
| Box, foam, printed notice | ≈ 3 € | ≈ 3 € | estimate |
| Shipping, Colissimo home delivery, 250 g | 5.49 € | 5.49 € | **real**: La Poste 2026 rate (free for the customer above 59 €) |

## Per capacity

SSD prices are retail estimates for an M.2 2230 NVMe (2 TB: $120–140 seen).
Card fees: Stripe ≈ 1.5 % + 0.25 €. Micro-enterprise contributions on sales
(France): ≈ 12.4 % of the price.

| Capacity | SSD | Total cost (10 / 100) | Price | Left per unit (10 / 100) |
|---|---|---|---|---|
| 256 GB | ≈ 30 € | 140 € / 102 € | 249 € | 75 € / 112 € |
| 512 GB | ≈ 45 € | 155 € / 117 € | 299 € | 103 € / 140 € |
| 1 TB | ≈ 80 € | 190 € / 152 € | 399 € | 154 € / 191 € |
| 2 TB | ≈ 130 € | 240 € / 202 € | 599 € | 276 € / 313 € |

Not included: one-off costs of the first run (stencil, CNC programming), the
first prototypes that may need a second revision, and income tax.

Note: a 10 Gb/s USB-A cable limits the drive to about 1 GB/s. Full USB4 speed
(≈ 3.5 GB/s) needs a USB-C 40 Gb/s (USB4 / Thunderbolt) cable and port.
