#!/usr/bin/env python3
"""1:1 drilling template for the Éclair Dock (A4 PDF), from the CAD numbers in
hardware/cartouche-usb4/cad/eclair_v1.py. Output: site/assets/gabarit-support-eclair.pdf"""
import os, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
X0, X1, FRONT, REAR, SCREWS, EDGE = 133.53, 163.47, -139.8, -66.0, (-100.0, -128.0), 30.0
W, L = X1 - X0, REAR - FRONT                                   # 29.94 × 73.8 mm
fig = plt.figure(figsize=(210 / 25.4, 297 / 25.4))
ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, 210); ax.set_ylim(0, 297); ax.axis("off")
ox, oy = 105 - W / 2, 150                                      # footprint: open end at the bottom
fy = lambda y: oy + (y - FRONT)                                # CAD y → page mm (open end at oy)
ax.add_patch(Rectangle((ox, oy), W, L, fill=False, lw=0.8, ls=(0, (4, 3))))
for y in SCREWS:
    cx, cy = 105, fy(y)
    ax.add_patch(Circle((cx, cy), 1.25, fill=False, lw=0.6)); ax.add_patch(Circle((cx, cy), 4.5, fill=False, lw=0.4))
    ax.plot([cx - 7, cx + 7], [cy, cy], lw=0.4, color="k"); ax.plot([cx, cx], [cy - 7, cy + 7], lw=0.4, color="k")
    ax.text(cx + 9, cy, "avant-trou Ø2,5", va="center", fontsize=7)
ax.plot([20, 190], [oy - EDGE] * 2, lw=1.2, color="k")
ax.text(105, oy - EDGE - 5, "BORD DU BUREAU (côté où vous êtes assis)", ha="center", fontsize=8, weight="bold")
ax.annotate("", (105, oy - EDGE), (105, oy), arrowprops=dict(arrowstyle="<->", lw=0.6))
ax.text(108, oy - EDGE / 2, "30 mm", va="center", fontsize=7)
ax.text(105, oy + L + 6, "côté fermé (câble)", ha="center", fontsize=7)
ax.text(105, oy + 3, "côté ouvert : Éclair entre ici", ha="center", fontsize=7)
ax.text(105, 280, "SUPPORT ÉCLAIR · GABARIT DE PERÇAGE 1:1", ha="center", fontsize=12, weight="bold")
ax.text(105, 272, "Imprimer à 100 % (taille réelle, sans « ajuster à la page »). Vérifier la barre de 50 mm.", ha="center", fontsize=8)
ax.plot([80, 130], [40, 40], lw=1.4, color="k"); ax.plot([80, 80], [38, 42], lw=1.4, color="k"); ax.plot([130, 130], [38, 42], lw=1.4, color="k")
ax.text(105, 44, "50 mm", ha="center", fontsize=8)
steps = ["1. Scotcher le gabarit sous le bureau, la ligne du bas sur le bord.", "2. Marquer les deux croix au crayon (ou pointer à travers).",
         "3. Retirer le gabarit, percer Ø2,5 mm sur 14 mm (plateau de 18 mm d’épaisseur minimum).", "4. Visser le support : 2 vis à bois Ø4 × 16 tête fraisée, sans forcer."]
for i, t in enumerate(steps): ax.text(20, 100 - i * 8, t, fontsize=8)
ax.text(105, 12, "cartouche.candygate.eu/support-pose.html · d'après le modèle CAD (eclair_v1.py)", ha="center", fontsize=6, color="#666")
out = os.path.join(ROOT, "site", "assets", "gabarit-support-eclair.pdf")
fig.savefig(out); print(out)
