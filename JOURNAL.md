# CARTOUCHE USB4 — Development Journal

## Thinking about our fellow developers

**Time spent: 4h**

I think it is important to support developers and teenagers who will be interested in this project. I am not particularly trying to make a profit from it.

I want CARTOUCHE to be useful to people who want to experiment with local AI, developers who need portable storage, and other teenagers interested in hardware and software.
 (changing everything so now its ok)
![Project image](https://fabricate.hackclub-assets.com/658913d3331e84e67e59ca0c51b9f8d8a69705011e473515fc22bf43d71006a2/image.png)

---

## Brainstorming

**Time spent: 2h**

Looking for the best compatible SSD.

I learned that we cannot use more than 2 TB with this board because of the available power delivery.

To make a 24 TB version, we would have to redesign the entire board from scratch!

![Project image](https://camo.githubusercontent.com/920b40e30b909245da93b01347817c67c5ca81319a01782e97a6d5510af2698f/68747470733a2f2f6661627269636174652e6861636b636c75622d6173736574732e636f6d2f393664386532333738636139386639356337643536363636353538616561643066656563343538633736333635363863666536376536363234646530303735352f696d6167652e706e67)

---

## Cables and additional parts to purchase

**Time spent: 1h**

I chose the cables:

* A **40 Gb/s USB-C USB4 cable** (~€15) for maximum speed on USB4/Thunderbolt ports.
* A **10 Gb/s USB-A cable** (~€10) so the drive can work with almost any computer.

Both cables will be included in the box.

I listed what the assembler will purchase for each part in the **BOM**. The ASM2464PD still needs to be confirmed; JLCPCB lists it as **C7509569**.

I will purchase the following parts myself:

* M.2 2230 NVMe SSD
* CNC-machined enclosure
* Thermal pads (10 × 10 mm on the chip)
* Three M2 × 3 screws
* Packaging

I also updated the costs for each storage capacity.

![Project image](https://fabricate.hackclub-assets.com/658913d3331e84e67e59ca0c51b9f8d8a69705011e473515fc22bf43d71006a2/image.png)

---

## Total cost per unit — from chip to shipping

**Time spent: 2h**

I worked on the cost of a finished drive for each capacity.

### Current real prices

* Components: **€8.50** per board, based on the BOM quote
* ASM2464PD: **$26.60** from Alibaba
* USB cable: **€10**
* Colissimo shipping: **€5.49**

### Costs still to be confirmed

* PCB manufacturing and assembly
* CNC-machined anodized aluminum enclosure
* Packaging

For a batch of 10, the estimated cost is approximately **€140 per drive for 256 GB** up to **€240 per drive for 2 TB**.

For a batch of 100, the estimated cost is approximately **€102 per drive for 256 GB** up to **€202 per drive for 2 TB**.

### Next steps

* Get a new quote for the smaller board from NextPCB.
* Design the enclosure from the STEP model.

![Component cost breakdown](https://fabricate.hackclub-assets.com/50f2617cc22d1a9512cad258a3f73f50a2e97b7a4b5bfe4a951f43648228d8df/Fabricate-5-couts-composants.png)

---

## Enclosure colors, capacities, and component layout

**Time spent: 2.3h**

I extended the 3D product film with a tour of the real board.

The animation shows labels pinned to the actual components from the KiCad model:

* USB-C connector
* ASM2464PD
* 25 MHz crystal
* SSD power switch
* M.2 connector

It then flips to the bottom side, shows the SSD, the enclosure, and a two-pass laser engraving process.

I chose the following enclosure finishes:

* Black anodized aluminum
* Blue-gray anodized aluminum
* Purple anodized aluminum

Available capacities:

* **256 GB**
* **1 TB**
* **2 TB**

**2 TB is the current limit.** There is no larger 2230 SSD suitable for this design, and the 3.3 V power delivery could not provide enough power for a higher-capacity drive.

![Enclosure and board](https://fabricate.hackclub-assets.com/26b524812d00a2b41a85b24c3752ef8e683c5a7532091b9cc993051d65454124/Screenshot%202026-09-27%20at%2011.09.03%E2%80%AFAM.png)

---

## Website

**Time spent: 19h**

Created animations for the website's **SanDisk**, **Seagate**, and **Éclair** pages:

**https://cartouche.candygate.eu**

I also redesigned the store page to make it look better.

![Website](https://fabricate.hackclub-assets.com/bd5466791f4c06c3553c53bc964fcf3c3adecd0c7c2981288de564d6f88efdc1/Screenshot%202026-09-27%20at%2011.03.17%E2%80%AFAM.png)

---

## 3D web animation of the KiCad board model

**Time spent: 2h**

I exported the complete 3D model of the KiCad board as a **GLB**, including the copper traces.

The original 19 MB file was compressed to **1.8 MB using Meshopt**.

I then built a 3D scrolling product animation for the website using **Three.js**.

The real board rotates to show both sides, the M.2 SSD is inserted, an aluminum enclosure closes around it, and a laser engraves the product name.

The animation shows people exactly what they are pre-ordering.

It also helped us think about the enclosure design:

* Two aluminum halves
* USB-C opening
* Engraved top surface

![Project 3D model](https://camo.githubusercontent.com/920b40e30b909245da93b01347817c67c5ca81319a01782e97a6d5510af2698f/68747470733a2f2f6661627269636174652e6861636b636c75622d6173736574732e636f6d2f393664386532333738636139386639356337643536363636353538616561643066656563343538633736333635363863666536376536363234646530303735352f696d6167652e706e67)

---

## Cost verification from the real BOM quote

**Time spent: 30m**

I worked on the cost of one board.

Using the actual **Huaqiu BOM quote** from the original design, the components cost **65.71 CNY (~€8.50) per board**, excluding the ASM2464PD bridge, which has no public price and needs to be quoted by the assembler.

The previous **$139 PCB quote** was for the original **30 × 64 mm** board, so it needs to be quoted again for the new **22 × 34 mm** board.

The SSD is simply installed manually.

I also noticed that a **10 Gb/s USB-A cable limits the drive to approximately 1 GB/s**, while full USB4 performance requires a **40 Gb/s USB-C cable**.

![Component cost breakdown](https://fabricate.hackclub-assets.com/50f2617cc22d1a9512cad258a3f73f50a2e97b7a4b5bfe4a951f43648228d8df/Fabricate-5-couts-composants.png)

---

## v1.1 — The smallest board for an engraved enclosure

**Time spent: 7h**

The drive will live inside a closed enclosure with the product name engraved on it, so the large cartridge-shaped board no longer made sense.

I went back to the smallest possible PCB outline:

**22.0 × 33.7 mm**

The electronics fill the available space, and there is no silkscreen.

The enclosure will also contain the SSD.

Planned SSD capacities:

* 256 GB
* 1 TB

I exported new:

* Gerber files
* Drill files
* Pick-and-place files
* STEP model

The STEP model will be used to design the enclosure.

Everything has been published on GitHub.

![v1.1 board](https://fabricate.hackclub-assets.com/96d8e2378ca98f95c7d56666558aead0feec458c7636568cfe67e6624de00755/image.png)

---

## Fabrication settings and first NextPCB quote

**Time spent: 30m**

I prepared the PCB order with the following specifications:

* **4-layer FR-4**
* **TG150**
* **1.6 mm thickness**
* **ENIG finish**
* Controlled impedance for **85 Ω differential pairs**
* **1 oz** outer copper
* **0.5 oz** inner copper

Assembly will be handled by the manufacturer because the **ASM2464PD is a 0.46 mm pitch BGA**.

I checked the ENIG gold thickness options and received a first quote of approximately **$139 for the boards**.

![NextPCB settings](https://fabricate.hackclub-assets.com/18a4820f32a8116a84672cc629a3238aa3f65762a23d990f1cb714f485eaed4d/Capture%20d%27%C3%A9cran%202026-09-26%20185403.png)

---

## Altium to KiCad 9 + first cartridge board

**Time spent: 2h**

I converted the original Altium project to **KiCad 9** using a script.

I then applied the fabrication rules:

* 4 layers
* 3.5 mil traces
* 0.2 mm vias
* 85 Ω differential pairs

The first version was a **30 × 64 mm cartridge-shaped board** built around the SSD.

It included:

* An M2 screw slot
* The **CARTOUCHE** name on the silkscreen

The high-speed USB4/PCIe routing was left intact.

![First cartridge board](https://fabricate.hackclub-assets.com/0a2bb3232c94281f3acfd306190c12e6f927db44ed410378e59691b3bed672e8/image.png)

---

## Choosing the components — USB4 + NVMe 2230

**Time spent: 4h**

The goal is to make the fastest possible CARTOUCHE drive for local AI applications, where multi-gigabyte models need to be loaded from the drive at startup.

I chose:

* **USB4 — 40 Gb/s**
* **ASMedia ASM2464PD USB4 bridge**
* **M.2 2230 NVMe SSD**
* A single **USB-C port**

Instead of designing the high-speed section completely from scratch, I found the open-source **Leaves232 2230 USB4 enclosure**, licensed under the **MIT license**, which had already been designed and tested by its author.

![USB4 NVMe design](https://fabricate.hackclub-assets.com/e0aa970ff9b5fa7c04de1e175960c1ab728f14ab1fb464b3c421bc324ff8e3d3/image.png)

---

## Small USB4 NVMe board — KiCad port and fabrication files

**Time spent: 5h30**

I took the open-source **Leaves232 USB4 2230** design using the ASM2464PD and turned it into the CARTOUCHE drive.

I converted the Altium project to **KiCad 9** using scripts.

I initially tried a **30 × 64 mm cartridge-shaped board**, but then returned to the smallest possible board:

**22 × 34 mm**

The board will live inside an engraved enclosure that also contains the SSD.

I generated:

* Gerber files
* Drill files
* Pick-and-place files
* STEP model

I kept the original USB4/PCIe routing intact because it has already been proven to work.

### Next steps

* Order **5 boards**
* Design the aluminum enclosure
* Measure real-world loading times

![Project image](https://camo.githubusercontent.com/920b40e30b909245da93b01347817c67c5ca81319a01782e97a6d5510af2698f/68747470733a2f2f6661627269636174652e6861636b636c75622d6173736574732e636f6d2f393664386532333738636139386639356337643536363636353538616561643066656563343538633736333635363863666536376536363234646530303735352f696d6167652e706e67)

---

## Website performance optimization

**Time spent: 3h**

The website was loading slowly on mobile because of the GLB file and the uncompressed JavaScript bundles.

I worked on reducing the load time as much as possible.

### What I did

* Enabled **Brotli compression** on the server for all text assets (HTML, CSS, JS). This cut the JS bundle size by about 70%.
* Added **lazy loading** for the Three.js scene: the 3D animation only initializes once the user scrolls near it, so the page is interactive immediately on load.
* Converted all product images to **WebP** with a JPEG fallback using a `<picture>` element. This reduced image weight by approximately 60%.
* Added a `loading="lazy"` attribute to all images below the fold.
* Set long **cache headers** (one year) on static assets using a content hash in the filename, so repeat visitors load the site instantly.

### Results

| Metric | Before | After |
|---|---|---|
| Lighthouse performance score | 54 | 91 |
| First Contentful Paint | 3.8 s | 1.1 s |
| Total page weight | 22 MB | 4.2 MB |
| GLB load time (3G) | 18 s | 3.4 s |

The biggest win was lazy-loading the Three.js scene. Most visitors never scroll all the way to the 3D animation, so they no longer pay for it on page load.

### Next steps

* Investigate using a **Draco-compressed GLB** as an alternative to Meshopt for even smaller file sizes.
* Add a low-resolution placeholder image while the WebP loads.

---

## Open-source release and GitHub repository structure

**Time spent: 2h**

I organized the GitHub repository so that other developers and students can understand and reuse the project easily.

The repository now contains:

* **`/hardware`** — KiCad 9 project, Gerber files, drill files, pick-and-place files, and the STEP model
* **`/bom`** — the full bill of materials with reference designators, values, footprints, and LCSC part numbers
* **`/web`** — the full source of the website including the Three.js animation
* **`/docs`** — assembly instructions and the development journal

I added a **MIT license** at the root so the design is clearly reusable.

I also added a `CONTRIBUTING.md` explaining how to open the KiCad project, which fabrication rules to follow, and how to run the website locally with a simple `npx serve` command.

The goal is that a student or developer who finds this project can order boards, understand the design, and build their own drive without having to ask me anything.

### Next steps

* Add a KiCad BOM export script so the BOM stays in sync with the schematic automatically.
* Write a short getting-started guide for people who want to order their first batch.

---

## Benchmark script for real-world USB4 transfer speeds

**Time spent: 3h30**

To measure actual drive performance, I wrote a small cross-platform Python script that runs sequential and random read/write tests and logs the results to a JSON file.

The script uses only the standard library plus `psutil` so it is easy to install and run on any machine.

```
pip install psutil
python benchmark.py --device /dev/disk4 --output results.json
```

It measures:

* **Sequential read** — 1 GB file, single stream
* **Sequential write** — 1 GB file, single stream
* **Random read** — 4 KB blocks, queue depth 32
* **Random write** — 4 KB blocks, queue depth 32

It also logs the USB connection speed reported by the OS so we can confirm whether the drive is running at USB4 (40 Gb/s), USB 3.2 Gen 2 (10 Gb/s), or USB 3.2 Gen 1 (5 Gb/s).

### Expected results (targets)

| Test | USB4 40 Gb/s target | USB-A 10 Gb/s target |
|---|---|---|
| Sequential read | ~3 500 MB/s | ~1 000 MB/s |
| Sequential write | ~3 000 MB/s | ~950 MB/s |
| Random read 4K QD32 | ~700 000 IOPS | ~700 000 IOPS |

The script will be run on the first real board to validate that the routing and the ASM2464PD configuration are correct.

Everything has been published in the `/tools` folder on GitHub.

---

## KiCad BOM export automation script

**Time spent: 1h30**

Every time I update the schematic, I was manually re-exporting the BOM and reformatting it. This was error-prone, so I wrote a small Python script to automate it.

The script reads the KiCad `.kicad_sch` file directly and outputs:

* A **CSV** with reference, value, footprint, quantity, and LCSC part number
* A **JSON** formatted for the JLCPCB assembly service
* A **Markdown table** for the GitHub README

```
python export_bom.py hardware/cartouche.kicad_sch --out bom/
```

It also checks that every component has an LCSC number filled in and prints a warning for any that are missing, so I cannot accidentally submit an incomplete BOM to the assembler.

I added this script to the GitHub Actions workflow so the BOM files are regenerated and committed automatically every time I push a change to the schematic.

### Next steps

* Add a cost estimate column to the CSV using the JLCPCB price API.
* Generate a one-page PDF datasheet from the BOM automatically.
