---
title: "Cartouche USB"
author: "arthur.ellies"
description: "CARTOUCHE is a way to store heavy AI models and run them easily and fast, while keeping your data from going to third-party servers."
created_at: "2026-09-26"
---

# September 26: Website

Creating animations on the website on Sandisk, Seagate and Eclair pages : https://cartouche.candygate.eu !

Changing the shop page to something better

![Website](https://fabricate.hackclub-assets.com/bd5466791f4c06c3553c53bc964fcf3c3adecd0c7c2981288de564d6f88efdc1/Screenshot%202026-09-27%20at%2011.03.17%E2%80%AFAM.png)

**Total time spent: 13h48m**

# September 26: Choosing the components — USB4 + NVMe 2230

Goal: the fastest possible drive for CARTOUCHE, a local AI that loads multi-GB models from the drive at every start. Chose USB4 (40 Gb/s) with the ASMedia ASM2464PD bridge and an M.2 2230 NVMe SSD, single USB-C port. Instead of designing the high-speed part from scratch, found the open-source Leaves232 2230 USB4 enclosure (MIT), already built and tested by its author.

![USB4 NVMe design](https://fabricate.hackclub-assets.com/e0aa970ff9b5fa7c04de1e175960c1ab728f14ab1fb464b3c421bc324ff8e3d3/image.png)

**Total time spent: 3h18m**

# September 26: Altium to KiCad 9 + first cartridge board

Converted the original Altium project to KiCad 9 with a script, then applied its fab rules (4 layers, 3.5 mil tracks, 0.2 mm vias, 85 ohm pairs). First version: a 30x64 mm game-cartridge board around the SSD, with an M2 screw slot and the CARTOUCHE name on the silkscreen. High-speed USB4/PCIe routing left untouched.

![First cartridge board](https://fabricate.hackclub-assets.com/0a2bb3232c94281f3acfd306190c12e6f927db44ed410378e59691b3bed672e8/image.png)

**Total time spent: 1h**

# September 26: Fabrication settings and first NextPCB quote

Prepared the order: 4-layer FR-4 TG150, 1.6 mm, ENIG, controlled impedance for the 85 ohm differential pairs, 1 oz outer / 0.5 oz inner copper, assembly by the fab because the ASM2464PD is a 0.46 mm pitch BGA. Checked the ENIG gold thickness options and got a first quote (about $139 for the boards).

![NextPCB settings](https://fabricate.hackclub-assets.com/18a4820f32a8116a84672cc629a3238aa3f65762a23d990f1cb714f485eaed4d/Capture%20d%27%C3%A9cran%202026-09-26%20185403.png)

**Total time spent: 12m**

# September 27: v1.1 — The smallest board for an engraved enclosure

The drive will live in a closed case with the name engraved on it, so the big cartridge board made no sense. Went back to the smallest possible outline, 22.0 x 33.7 mm (the electronics fill it), no silkscreen, the case holds the SSD. Planned SSD: 256 GB or 1 TB. Exported new Gerbers, drills, pick-and-place and a STEP model to design the case, and published everything on GitHub.

![v1.1 board](https://fabricate.hackclub-assets.com/96d8e2378ca98f95c7d56666558aead0feec458c7636568cfe67e6624de00755/image.png)

**Total time spent: 5h**

# September 27: Small USB4 NVMe board — KiCad port and fabrication files

Took the open-source Leaves232 USB4 2230 enclosure (ASM2464PD, MIT) and made it the CARTOUCHE drive. Converted the Altium project to KiCad 9 with scripts, tried a 30×64 mm cartridge board first, then went back to the smallest possible 22×34 mm board since it will live in an engraved case that also holds the SSD. Generated Gerbers, drill files, pick-and-place, and a STEP model to design the case. Kept the USB4/PCIe routing untouched since it's proven.
Next: order 5 boards, design the aluminium case, measure real load times.

![Project image](https://camo.githubusercontent.com/920b40e30b909245da93b01347817c67c5ca81319a01782e97a6d5510af2698f/68747470733a2f2f6661627269636174652e6861636b636c75622d6173736574732e636f6d2f393664386532333738636139386639356337643536363636353538616561643066656563343538633736333635363863666536376536363234646530303735352f696d6167652e706e67)

**Total time spent: 3h**

# September 27: Cost verification from the real BOM quote

Worked out what one board costs. From the original design's real Huaqiu BOM quote: 65.71 CNY (about 8.5 €) of components per board, without the ASM2464PD bridge, which has no public price and must be quoted by the assembler. The old $139 PCB quote was for the 30x64 mm board, so it needs redoing for the new 22x34 mm one. The SSD just plugs in by hand. Noted that a 10 Gb/s USB-A cable caps it at about 1 GB/s; full USB4 needs a 40 Gb/s USB-C cable.

![Component cost breakdown](https://fabricate.hackclub-assets.com/50f2617cc22d1a9512cad258a3f73f50a2e97b7a4b5bfe4a951f43648228d8df/Fabricate-5-couts-composants.png)

**Total time spent: 12m**

# September 27: 3D web animation of the KiCad board model

Exported the board's full 3D model from KiCad (GLB with copper tracks, 19 MB compressed to 1.8 MB with meshopt) and built a scroll-driven 3D film for the product page with three.js: the real board turns around to show both sides, the M.2 SSD plugs in, an aluminium case closes around it and a laser engraves the name. It shows people exactly what they pre-order, and made us think through the case: two aluminium halves, USB-C opening, engraved top.

![Project 3D model](https://camo.githubusercontent.com/920b40e30b909245da93b01347817c67c5ca81319a01782e97a6d5510af2698f/68747470733a2f2f6661627269636174652e6861636b636c75622d6173736574732e636f6d2f393664386532333738636139386639356337643536363636353538616561643066656563343538633736333635363863666536376536363234646530303735352f696d6167652e706e67)

**Total time spent: 1h**

# September 27: Enclosure colors, capacities, and component layout

Extended the 3D product film with a tour of the real board: labels pinned to the actual components from the KiCad model (USB-C, ASM2464PD, 25 MHz crystal, SSD power switch, M.2 connector), a flip to the bottom side, then the SSD, the case and a two-pass laser engraving. Picked the case finishes (black, blue-grey, violet anodised aluminium) and capacities: 256 GB, 1 TB and 2 TB. 2 TB is the limit: no bigger 2230 SSD exists and the 3.3 V supply couldn't power one.

![Enclosure and board](https://fabricate.hackclub-assets.com/26b524812d00a2b41a85b24c3752ef8e683c5a7532091b9cc993051d65454124/Screenshot%202026-09-27%20at%2011.09.03%E2%80%AFAM.png)

**Total time spent: 24m**

# September 27: Cables and additional parts to purchase

Chose the cables: a USB-C 40 Gb/s USB4 cable (about 15 €) for full speed on USB4/Thunderbolt ports, plus a 10 Gb/s USB-A cable (10 €) so it works on any computer. Both go in the box. Listed what the assembler buys (every BOM part; the ASM2464PD must be confirmed, JLCPCB stocks it as C7509569) and what I buy myself: the M.2 2230 SSD, the CNC case, thermal pads (10x10 mm on the chip), three M2x3 screws and packaging. Updated the per-capacity costs.

![Project image](https://fabricate.hackclub-assets.com/658913d3331e84e67e59ca0c51b9f8d8a69705011e473515fc22bf43d71006a2/image.png)

**Total time spent: 12m**

# September 27: Total cost per unit — from chip to shipping

Worked out what one finished drive costs, per capacity. Real prices: parts 8.50 € (BOM quote), ASM2464PD $26.60 (Alibaba), cable 10 €, Colissimo shipping 5.49 €. Estimates to confirm: PCB and assembly, CNC anodised aluminium case, box. A batch of 10 costs about 140 € (256 GB) to 240 € (2 TB) per drive, and a batch of 100 about 102 € to 202 €. Next: re-quote the smaller board at NextPCB and draw the case from the STEP model.

![Component cost breakdown](https://fabricate.hackclub-assets.com/50f2617cc22d1a9512cad258a3f73f50a2e97b7a4b5bfe4a951f43648228d8df/Fabricate-5-couts-composants.png)

**Total time spent: 24m**

# September 27: Brainstorming

looking for the best SSD compatible
i learnt that we can't use more than 2To for this card because of the power supply
to go to a 24To key we will need to design all the card from 0 again!

![Project image](https://camo.githubusercontent.com/920b40e30b909245da93b01347817c67c5ca81319a01782e97a6d5510af2698f/68747470733a2f2f6661627269636174652e6861636b636c75622d6173736574732e636f6d2f393664386532333738636139386639356337643536363636353538616561643066656563343538633736333635363863666536376536363234646530303735352f696d6167652e706e67)

**Total time spent: 1h12m**

# September 27: Thinking about our fellow developers

I think it's important to support the developers and teenagers who will be interested, and I'm not especially trying to make a profit on this project.

![Project image](https://fabricate.hackclub-assets.com/658913d3331e84e67e59ca0c51b9f8d8a69705011e473515fc22bf43d71006a2/image.png)

**Total time spent: 2h**

# September 28: One error patched

When I printed the parts, they didn't fit, so after some research I realised it simply wasn't the right components. The mock-up just didn't have a slot, and the SSD was too low. I'm going to reprint everything to test the layout and the screws.

![Section of the assembly](https://raw.githubusercontent.com/opencorp2030-ctrl/cartouche-usb4/main/docs/images/model-section.png)

**Total time spent: 1h18m**

# September 28: The board runs too hot

I was thinking that a board that can handle up to 40 Gb/s would get very hot during long sessions, and since this case is meant to stay plugged in, hung under a desk, all day long, I had to avoid setting that desk on fire :)

I think this is the best option: my other idea was to add a fan, but that would make the case much more fragile and noisy, and I'd also have to add vents to the case. We'll try it on the prototype, and if it gets too hot, we'll rethink the system.

I updated the website with new animations so customers can understand.

This project is aimed at young devs at my high school: I talked about it with the principal and with some students who would be very interested in buying one at cost.

![Cooling: heat path inside the case (section, to scale)](https://raw.githubusercontent.com/opencorp2030-ctrl/cartouche-usb4/main/docs/images/cooling-diagram.png)

![Airflow direction under the desk (cross-section, to scale)](https://raw.githubusercontent.com/opencorp2030-ctrl/cartouche-usb4/main/docs/images/airflow-diagram.png)

![Expected temperatures before / after the cooling changes (estimate)](https://raw.githubusercontent.com/opencorp2030-ctrl/cartouche-usb4/main/docs/images/cooling-estimate.png)

**Total time spent: 2h**
