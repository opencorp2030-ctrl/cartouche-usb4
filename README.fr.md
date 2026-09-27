# CARTOUCHE USB4 — carte « cartouche » pour SSD NVMe 2230

Carte électronique de la CARTOUCHE matérielle : **un seul port USB-C**, une puce
**ASMedia ASM2464PD** (USB4 40 Gb/s ↔ PCIe 4.0 x4) et un **SSD NVMe M.2 2230**
couché sous la carte, dans un format de cartouche de jeu (30 × 64 mm).

| | |
|---|---|
| Débit | ~3,5–3,8 Go/s en USB4 / Thunderbolt 3‑4 ; ~1 Go/s sur un port USB 3.2 10 Gb/s ; fonctionne aussi en USB 3.0 |
| Stockage | SSD NVMe 2230, **2 To maximum** (limite de l'alimentation 3,3 V) |
| Circuit | 4 couches, 1,6 mm, impédance contrôlée 85 Ω, pistes 3,5 mil, vias 0,3/0,2 mm |

![dessus](images/top.png) ![dessous](images/bottom.png)

## Origine et licence

Le cœur électronique (schéma, routage USB4/PCIe, alimentations) vient du projet
**[Leaves232/2230-USB4-SSD-Enclosure-Design](https://github.com/Leaves232/2230-USB4-SSD-Enclosure-Design)**,
sous licence MIT (voir `LICENSE-upstream-MIT`), testé par son auteur avec un SSD
Hynix P44 Pro 2 To. CARTOUCHE y ajoute : le contour cartouche 30 × 64 mm qui
entoure le SSD, une boutonnière M2 pour visser le SSD, la sérigraphie.
**La zone rapide (USB4, PCIe) n'a pas été modifiée.**

## Fichiers

- `cartouche-usb4.kicad_pcb` / `.kicad_pro` — projet KiCad 9.
- `fab/cartouche-usb4-gerbers.zip` — Gerbers + perçages, à envoyer au fabricant.
- `fab/positions.csv` — positions des composants (assemblage).
- `fab/nomenclature-BOM.xlsx`, `fab/devis-composants-reference.xlsx` — composants (du projet d'origine).
- `fab/exigences-fabrication.xlsx` — exigences de fabrication d'origine.
- `fab/gabarit-1-1.pdf` — contour à l'échelle 1:1.
- `scripts/` — conversion Altium → KiCad et génération de la cartouche (reproductible).

Le schéma d'origine est au format Altium (`ASM2464PD.SchDoc` dans le dépôt
d'origine) ; KiCad l'ouvre via *Fichier → Importer → Projet non-KiCad*.

## Faire fabriquer

Paramètres (identiques à la carte d'origine, fabriquée chez Huaqiu) :
4 couches · FR‑4 TG150 · 1,6 mm · **impédance contrôlée : paires différentielles
85 Ω sur les couches extérieures** · pistes/isolements 3,5/3,5 mil · vias 0,2 mm
(bouchés par le vernis) · finition ENIG · cuivre 1 oz extérieur / 0,5 oz intérieur.

- Assemblage : la puce ASM2464PD est un **BGA au pas de 0,46 mm** : faites-la
  poser par le fabricant (assemblage PCBA), pas à la main.
- ⚠️ **Ne relancez pas le remplissage des zones** (touche B) dans KiCad : les plans
  de cuivre sont ceux calculés sur la carte d'origine. Le DRC signale 506 écarts
  « zone isolation 0,5 mm » et des ponts de vernis sous le BGA : ils viennent de
  l'import Altium, pas d'erreurs réelles (pistes et pastilles : 0 erreur,
  0 connexion manquante).

## Avant de commander : à vérifier

1. **Imprimez `fab/gabarit-1-1.pdf` à 100 %** et posez un vrai SSD 2230 dessus :
   son encoche doit tomber dans la boutonnière (elle laisse ±3 mm de jeu).
   Vis M2 + entretoise de la hauteur du connecteur M.2.
2. **Refroidissement obligatoire** : l'ASM2464PD chauffe et se déconnecte sans
   dissipateur. Prévoir un pad thermique entre la puce et le boîtier (la finition
   Métal en aluminium sert alors de radiateur).
3. **Firmware** : une carte neuve doit être programmée une fois avec l'outil
   ASMedia (ASM246xMPTool) et le firmware fournis dans le dépôt d'origine
   (non redistribués ici).
