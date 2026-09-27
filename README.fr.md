# CARTOUCHE USB4 — carte USB4 pour SSD NVMe 2230, la plus petite possible

Carte électronique de la CARTOUCHE matérielle : **un seul port USB-C**, une puce
**ASMedia ASM2464PD** (USB4 40 Gb/s ↔ PCIe 4.0 x4) et un connecteur pour un **SSD
NVMe M.2 2230**. Elle est faite pour être enfermée dans une coque : elle est donc
**aussi petite que l'électronique le permet**, sans aucun texte (le nom CARTOUCHE
est gravé sur la coque).

| | |
|---|---|
| Carte | **22,0 × 33,7 mm**, 4 couches, 1,6 mm |
| Avec le SSD branché | environ **22 × 56 mm** (le SSD s'enfiche au bout de la carte, dans son alignement) |
| Débit | ~3,5–3,8 Go/s en USB4 / Thunderbolt 3‑4 ; ~1 Go/s sur un port USB 3.2 10 Gb/s ; fonctionne aussi en USB 3.0 |
| Stockage prévu | SSD NVMe 2230 de **256 Go**, ou **1 To** si le fournisseur peut (2 To au maximum : limite de l'alimentation 3,3 V) |
| Circuit | impédance contrôlée 85 Ω, pistes 3,5 mil, vias 0,3/0,2 mm |

![dessus](images/top.png) ![dessous](images/bottom.png)

## Versions

- **v1.1 (actuelle)** : contour d'origine de 22,0 × 33,7 mm, le plus petit
  possible. Pas de sérigraphie ajoutée, pas de trou de vis : **c'est la coque qui
  maintient le SSD**, comme dans le boîtier d'origine.
- v1.0 : carte « cartouche » de 30 × 64 mm entourant le SSD, avec le nom
  sérigraphié et une boutonnière M2. Abandonnée : inutile une fois la carte dans
  une coque. Toujours générable avec `scripts/make_cartouche.py … --cartridge`.

## Origine et licence

Le cœur électronique (schéma, routage USB4/PCIe, alimentations, contour) vient du
projet **[Leaves232/2230-USB4-SSD-Enclosure-Design](https://github.com/Leaves232/2230-USB4-SSD-Enclosure-Design)**,
sous licence MIT (voir `LICENSE-upstream-MIT`), testé par son auteur avec un SSD
Hynix P44 Pro 2 To. Sa signature au dos de la carte est conservée.
CARTOUCHE y apporte : la conversion Altium → KiCad 9 (scripts reproductibles),
le dossier de fabrication complet et la maquette 3D pour dessiner la coque.
**La zone rapide (USB4, PCIe) n'a pas été modifiée.**

## Fichiers

- `cartouche-usb4.kicad_pcb` / `.kicad_pro` — projet KiCad 9.
- `fab/cartouche-usb4-gerbers.zip` — Gerbers + perçages (métallisés et non métallisés séparés), à envoyer au fabricant.
- `fab/positions.csv` — positions des composants (assemblage).
- `fab/cartouche-usb4.step` — **maquette 3D de la carte avec ses composants, pour dessiner la coque**.
- `fab/nomenclature-BOM.xlsx`, `fab/devis-composants-reference.xlsx` — composants (du projet d'origine).
- `fab/exigences-fabrication.xlsx` — exigences de fabrication d'origine.
- `fab/gabarit-1-1.pdf` — contour et encombrement à l'échelle 1:1.
- `scripts/` — conversion Altium → KiCad et génération de la carte (reproductible).

## Faire fabriquer

Paramètres (identiques à la carte d'origine, fabriquée chez Huaqiu) :
4 couches · FR‑4 TG150 · 1,6 mm · **impédance contrôlée : paires différentielles
85 Ω sur les couches extérieures** · pistes/isolements 3,5/3,5 mil · vias 0,2 mm
(bouchés par le vernis) · finition ENIG · cuivre 1 oz extérieur / 0,5 oz intérieur.

- Assemblage : la puce ASM2464PD est un **BGA au pas de 0,46 mm** : faites-la
  poser par le fabricant (assemblage PCBA), pas à la main.
- ⚠️ **Ne relancez pas le remplissage des zones** (touche B) dans KiCad : les plans
  de cuivre sont ceux calculés sur la carte d'origine. Le DRC signale 507 écarts
  d'isolation de zones, 199 ponts de vernis sous le BGA, 5 écarts trou/zone et
  3 éléments au ras du bord (les pattes du connecteur M.2, où le SSD s'enfiche) :
  tous viennent de la carte d'origine telle qu'elle a été fabriquée, pas
  d'erreurs réelles (0 connexion manquante).

## La coque : à prévoir

1. **Maintien du SSD** : un plot avec une vis M2 (ou une butée) dans la coque, à
   30 mm du connecteur, puisque la carte ne porte plus la vis.
2. **Refroidissement obligatoire** : l'ASM2464PD chauffe et se déconnecte sans
   dissipateur. Pad thermique entre la puce et la coque (une coque en aluminium
   sert alors de radiateur).
3. Les deux grands trous près du port USB-C servent à visser la carte dans la coque.
4. **Firmware** : une carte neuve doit être programmée une fois avec l'outil
   ASMedia (ASM246xMPTool) et le firmware fournis dans le dépôt d'origine
   (non redistribués ici).
