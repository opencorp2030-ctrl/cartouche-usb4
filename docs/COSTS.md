# Cost of one CARTOUCHE Éclair (USB4 drive), per capacity

**Real** = a quote or a public price · **estimate** = not quoted by a supplier yet.

![component cost](images/component-cost.png)

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

## Per capacity: sold at cost

I think it's important to support the developers and teenagers who will be
interested, and I'm not especially trying to make a profit on this project.

- Price = unit cost + card fees (1.5 % + 0.25 €) + seller's social contributions (12.3 %) + 5 % reserve (faulty units, returns).
- Shipping: charged separately, at cost.
- Public breakdown: [cartouche.candygate.eu/nos-prix.html](https://cartouche.candygate.eu/nos-prix.html) (computed by `tools/prix_coutant.py`).
- SSD prices: retail estimates for an M.2 2230 NVMe (2 TB: $120–140 seen). Costs for the first batch of 10.

| Capacity | SSD | Unit cost (incl. box) | Price | Of which reserve |
|---|---|---|---|---|
| 256 GB | ≈ 30 € | 149 € | 184 € | 9.36 € |
| 512 GB | ≈ 45 € | 164 € | 203 € | 10.73 € |
| 1 TB | ≈ 80 € | 199 € | 246 € | 12.80 € |
| 2 TB | ≈ 130 € | 249 € | 307 € | 15.38 € |

- Batches of 100: board ≈ 38 €, case ≈ 15 € → prices about 45 € lower per unit.
- Not included: one-off costs of the first run (stencil, CNC programming) and prototype revisions; not paid by buyers.
- In the box: USB-A cable (any computer, ≈ 1 GB/s) + USB-C 40 Gb/s cable (full USB4 speed, ≈ 3.5 GB/s).

## What to buy besides the assembled board

- Assembler (NextPCB, turnkey PCBA): buys and solders every BOM part (regulators, USB-C and M.2 connectors, crystal, flash, passives).
- ASM2464PD: ask the assembler to source it (missing from the original BOM match); otherwise JLCPCB C7509569, or Alibaba ($26.60) sent as a consigned part.

Per drive, bought separately:

| Part | Where | Per drive |
|---|---|---|
| M.2 2230 NVMe SSD (256 GB – 2 TB), e.g. WD SN740, Kioxia BG6, Corsair MP600 Mini | retail | 30–130 € |
| Aluminium case, 2 halves, CNC + anodised + laser-engraved | CNC supplier (from the STEP model) | ≈ 15–35 € |
| Thermal pad 1 mm, ≥ 12 W/mK: cut 10 × 10 mm for the ASM2464PD, 22 × 20 mm for the SSD | one 100 × 100 mm sheet (≈ 10 €) does about 25 drives | ≈ 0.40 € |
| 2 × M3 × 12 countersunk (board + case), 1 × M2 × 10 (rear), 1 × M2 × 3 (SSD) | screw kits (≈ 1–10 €) | ≈ 0.30 € |
| USB-C 40 Gb/s cable + USB-A 10 Gb/s cable | retail | ≈ 25 € |
| Box, foam insert, printed notice | packaging supplier / print shop | ≈ 3 € |

One-off tools: a Windows PC to flash the ASMedia firmware (free tool from the original project), a USB4 or Thunderbolt computer to measure the real speed.
