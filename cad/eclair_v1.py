"""CARTOUCHE Éclair V1 — case, SSD and USB-C plug, around the real board.

Everything is in the board's own frame (the KiCad STEP export), millimetres:
X across the board, Y along it (USB-C at Y = -88, SSD towards -Y), Z up,
board bottom at Z = 0 and top at Z = 1.6.

Outputs (in ./out): case_base, case_lid, ssd_2230, usbc_plug as STEP + STL,
and eclair_v1_assembly.step / .glb (board + SSD + case + plug, mated).

Run: python eclair_v1.py   (CadQuery 2.x)
Values marked CHECK are the ones to confirm with a printed test and real parts.
"""
import os
import cadquery as cq

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")
BOARD_STEP = os.path.join(HERE, "..", "fab", "cartouche-usb4.step")
if not os.path.exists(BOARD_STEP):                  # layout of the GitHub repository
    BOARD_STEP = os.path.join(HERE, "..", "pcb", "fab", "cartouche-usb4.step")
os.makedirs(OUT, exist_ok=True)

# ---- the board (from KiCad) -------------------------------------------------
BX0, BX1 = 137.48, 159.52          # board edges, X
BYF, BYB = -88.16, -121.84         # front (USB-C) and back (M.2) edges, Y
BT = 1.6                           # board thickness
CX = (BX0 + BX1) / 2               # 148.50
HOLES = [(140.496, -90.951), (156.496, -90.951)]   # Ø3.2 plated: M3
USBC = dict(x=148.551, face=-88.06, z=3.15, w=8.94, h=3.26)  # receptacle opening
CHIP = dict(x=151.24, y=-106.88, top=2.58, size=10.0)        # ASM2464PD, top of package
TOP_PARTS = 4.80                   # highest part above Z=0 (USB-C shell)

# ---- the SSD (M.2 2230, M key) -----------------------------------------------
# Connector CN1 = ARGOSY NASM0-S6701-TPH4 (M.2 M key, 3.0 mm high), mounted on the
# board's BOTTOM side. Datasheet (LCSC C364435, drawing NXSM0-S67XX-XXH4):
#   - mated card at "1.90 REF" from the board  -> card face nearest the board at Z = -1.90
#   - "module seating plane to alignment post 1.75"; the Ø1.60 / Ø1.10 posts are the
#     NPTH holes at Y = -115.646 (drill file)       -> card edge at Y = -117.40
# v1.0 had the card at -3.0 (1.1 mm too low, below the slot) and 0.35 mm too deep:
# a real SSD could not be plugged in. Fixed in v1.1.
SSD_W, SSD_L, SSD_T = 22.0, 30.0, 0.8
CN1_POST_Y = -115.646
SSD_NEAR = -1.90                   # card face towards the board
SSD_CHIPS = 1.35                   # parts on the far side (single-sided 2230, S3)
SSD_EDGE = CN1_POST_Y - 1.75       # -117.40: card edge seated in the connector
SSD_END = SSD_EDGE - SSD_L         # -147.40: screw notch centre   CHECK with a real SSD
CN1 = dict(x0=137.51, x1=159.51, y0=-121.35, y1=-112.80, z0=-3.29)   # connector body (STEP)
NOTCH_R = 1.75

# ---- the case ----------------------------------------------------------------
WALL, FLOOR, ROOF = 1.2, 1.2, 1.2
GAP = 0.3                          # clearance around the board
IN_X0, IN_X1 = BX0 - GAP, BX1 + GAP
FRONT_OUT = USBC["face"]           # receptacle face flush with the case front
FRONT_IN = FRONT_OUT - 1.0         # front wall 1.0 mm, above the board
BACK_IN = SSD_END - 5.2            # room for the SSD screw head and the rear post
BACK_OUT = BACK_IN - WALL
Z_FLOOR_IN = -5.65                 # kept from v1.0 (screw lengths); 1.6 mm under the SSD chips
Z_BOT = Z_FLOOR_IN - FLOOR
Z_ROOF_IN = TOP_PARTS + 0.5                        # 5.30
Z_TOP = Z_ROOF_IN + ROOF
SPLIT = 0.0                        # base below, lid above (board bottom)
R_OUT = 2.0                        # outer vertical edge radius
LIP = 0.9                          # tongue of the base that the lid overlaps
REAR = (CX, SSD_END - 3.3)         # rear closing screw (M2)

OX0, OX1 = IN_X0 - WALL, IN_X1 + WALL


def outer_block(z0, z1):
    return (cq.Workplane("XY").workplane(offset=z0)
            .center(CX, (FRONT_OUT + BACK_OUT) / 2)
            .rect(OX1 - OX0, FRONT_OUT - BACK_OUT).extrude(z1 - z0)
            .edges("|Z").fillet(R_OUT))


def cavity(z0, z1, shrink=0.0):
    return (cq.Workplane("XY").workplane(offset=z0)
            .center(CX, (FRONT_IN + BACK_IN) / 2)
            .rect(IN_X1 - IN_X0 - 2 * shrink, FRONT_IN - BACK_IN - 2 * shrink).extrude(z1 - z0)
            .edges("|Z").fillet(0.8))


def post(x, y, z0, z1, d):
    return cq.Workplane("XY").workplane(offset=z0).center(x, y).circle(d / 2).extrude(z1 - z0)


def hole(x, y, z0, z1, d):
    return cq.Workplane("XY").workplane(offset=z0).center(x, y).circle(d / 2).extrude(z1 - z0)


# ---- base: floor, walls up to the split, board posts, SSD standoff, lip -------
base = outer_block(Z_BOT, SPLIT).cut(cavity(Z_FLOOR_IN, SPLIT + 1))
# under the board the front wall reaches the board edge (the board rests on it)
base = base.union(cq.Workplane("XY").workplane(offset=Z_FLOOR_IN)
                  .center(CX, (FRONT_OUT + FRONT_IN) / 2).rect(IN_X1 - IN_X0, FRONT_OUT - FRONT_IN)
                  .extrude(SPLIT - Z_FLOOR_IN))
for x, y in HOLES:                                  # board posts, M3 passes through
    base = base.union(post(x, y, Z_FLOOR_IN, SPLIT, 5.6))
    base = base.cut(hole(x, y, Z_BOT - 1, SPLIT + 1, 3.4))
    base = base.cut(cq.Workplane("XY").workplane(offset=Z_BOT).center(x, y)
                    .circle(3.1).workplane(offset=1.7).circle(1.7).loft())      # countersink
base = base.union(post(CX, SSD_END, Z_FLOOR_IN, SSD_NEAR - SSD_T, 4.2))       # SSD standoff
base = base.cut(hole(CX, SSD_END, Z_FLOOR_IN, SSD_NEAR, 1.7))                # M2 pilot   CHECK
base = base.union(post(*REAR, Z_FLOOR_IN, SPLIT, 4.6))                        # rear post
base = base.cut(hole(*REAR, Z_BOT - 1, SPLIT + 1, 2.4))
base = base.cut(cq.Workplane("XY").workplane(offset=Z_BOT).center(*REAR).circle(2.2).workplane(offset=1.2).circle(1.2).loft())
# lip around the cavity, above the split, that the lid slides over
lip = cavity(SPLIT, SPLIT + 1.2).cut(cavity(SPLIT - 1, SPLIT + 2, shrink=LIP))
lip = lip.cut(cq.Workplane("XY").workplane(offset=SPLIT - 1)                   # no lip where the board sits
              .center(CX, (FRONT_IN + BYB) / 2).rect(IN_X1 - IN_X0 + 2, FRONT_IN - BYB + 0.6).extrude(3))
lip = lip.cut(hole(*REAR, SPLIT - 1, SPLIT + 3, 5.4))                          # clear the lid's rear post
base = base.union(lip)

# ---- passive cooling (v1.2) -------------------------------------------------------
# Leaves232's README: "ASM2464PD finished product will inevitably overheat and
# disconnect without heat dissipation" (he used a laptop fan). No fan here, so:
#  - the chip already presses a 1 mm pad on a boss of the aluminium lid (below);
#  - the SSD now presses a 1 mm pad (20 x 22 mm) on a boss of the aluminium base,
#    so the base spreads the SSD's heat too;
#  - 5 fins under the base add surface (the top stays flat for the engraving).
SSD_PAD = dict(w=20.0, l=22.0, t=1.0, squeeze=0.8)                  # pad squeezed to 0.8 mm
SSD_LOW = SSD_NEAR - SSD_T - SSD_CHIPS                              # lowest SSD part, -4.05
PAD_Y = SSD_EDGE - 5.0 - SSD_PAD["l"] / 2                          # under controller + NAND
base = base.union(cq.Workplane("XY").workplane(offset=Z_FLOOR_IN - 0.01)
                  .center(CX, PAD_Y).rect(SSD_PAD["w"], SSD_PAD["l"])
                  .extrude(SSD_LOW - SSD_PAD["squeeze"] - Z_FLOOR_IN + 0.01))    # CHECK with the real SSD
FIN_H, FIN_W, FIN_Y0, FIN_Y1 = 1.0, 1.2, -96.0, -146.0             # clear of the screw countersinks
for dx in (-8, -4, 0, 4, 8):
    base = base.union(cq.Workplane("XY").workplane(offset=Z_BOT - FIN_H)
                      .center(CX + dx, (FIN_Y0 + FIN_Y1) / 2).rect(FIN_W, FIN_Y0 - FIN_Y1)
                      .extrude(FIN_H + 0.01).edges("|Z").fillet(0.5))

# ---- lid: roof, walls down to the split, USB-C opening, screw bosses, heat boss --
lid = outer_block(SPLIT, Z_TOP).cut(cavity(SPLIT - 1, Z_ROOF_IN))
lid = lid.cut(cavity(SPLIT - 1, SPLIT + 1.25, shrink=-0.15))                  # seat for the base lip
# front wall above the board, with the opening for the receptacle
lid = lid.union(cq.Workplane("XY").workplane(offset=BT + 0.1)
                .center(CX, (FRONT_OUT + FRONT_IN) / 2).rect(IN_X1 - IN_X0, FRONT_OUT - FRONT_IN)
                .extrude(Z_ROOF_IN - BT - 0.1))
lid = lid.cut(cq.Workplane("XZ", origin=(0, FRONT_OUT + 1, 0)).center(USBC["x"], USBC["z"])
              .rect(USBC["w"] + 0.4, USBC["h"] + 0.4).extrude(3).edges("|Y").fillet(1.7))
# the board edge passes under the front wall
lid = lid.cut(cq.Workplane("XY").workplane(offset=SPLIT - 0.1)
              .center(CX, (FRONT_OUT + 0.5 + BYB) / 2).rect(IN_X1 - IN_X0, FRONT_OUT + 0.5 - BYB).extrude(BT + 0.2))
for x, y in HOLES:                                  # M3 bosses from the roof down to the board
    lid = lid.union(post(x, y, BT, Z_ROOF_IN, 5.6))
    lid = lid.cut(hole(x, y, BT - 0.1, Z_TOP - 0.6, 2.6))                      # M3 pilot: M3x12 countersunk from below  CHECK
# a small part next to the right screw (x 153.8–154.3, y -90.0 to -89.0) : pocket in the boss
lid = lid.cut(cq.Workplane("XY").workplane(offset=BT - 0.1).center(154.0, -89.5).rect(1.2, 1.6).extrude(1.2))
lid = lid.union(post(*REAR, SPLIT + 0.05, Z_ROOF_IN, 4.6))
lid = lid.cut(hole(*REAR, SPLIT, Z_TOP - 0.6, 1.7))                           # M2x10 countersunk from below
# boss pressing a 1 mm thermal pad onto the USB4 chip (pad squeezed to 0.8 mm)
lid = lid.union(cq.Workplane("XY").workplane(offset=CHIP["top"] + 0.8)
                .center(CHIP["x"], CHIP["y"]).rect(CHIP["size"], CHIP["size"]).extrude(Z_ROOF_IN - CHIP["top"] - 0.8 + 0.1))
# engraving area (0.3 mm deep): the laser marks it; kept flat here

# ---- SSD mock-up (to scale, to test the fit) ------------------------------------
ssd = (cq.Workplane("XY").workplane(offset=SSD_NEAR - SSD_T)
       .center(CX, SSD_EDGE - SSD_L / 2).rect(SSD_W, SSD_L).extrude(SSD_T))
ssd = ssd.cut(hole(CX, SSD_END, SSD_NEAR - 2, SSD_NEAR + 1, 2 * NOTCH_R))       # end notch
ssd = ssd.cut(cq.Workplane("XY").workplane(offset=SSD_NEAR - 2)                 # M key notch
              .center(CX - SSD_W / 2 + 19.85 - 0.6 + 0.6, SSD_EDGE - 2).rect(1.2, 4.2).extrude(3))
ssd = ssd.union(cq.Workplane("XY").workplane(offset=SSD_NEAR - SSD_T - 1.2)     # controller
                .center(CX - 4.5, SSD_EDGE - 9.5).rect(8.5, 8.5).extrude(1.2))
ssd = ssd.union(cq.Workplane("XY").workplane(offset=SSD_NEAR - SSD_T - SSD_CHIPS)  # NAND
                .center(CX + 2.5, SSD_EDGE - 21.0).rect(14.0, 12.0).extrude(SSD_CHIPS))

# ---- USB-C plug and cable, mated in the receptacle ------------------------------
ins = 6.2                          # shell inside the receptacle
shell = (cq.Workplane("XZ", origin=(0, USBC["face"] - ins, 0)).center(USBC["x"], USBC["z"])
         .rect(8.25, 2.4).extrude(-6.65).edges("|Y").fillet(1.15))
over = (cq.Workplane("XZ", origin=(0, USBC["face"] - ins + 6.65, 0)).center(USBC["x"], USBC["z"])
        .rect(12.4, 6.5).extrude(-18).edges("|Y").fillet(2.4))
cable = (cq.Workplane("XZ", origin=(0, USBC["face"] - ins + 6.65 + 18, 0)).center(USBC["x"], USBC["z"])
         .circle(2.0).extrude(-25))
plug = shell.union(over).union(cable)

# ---- exports -------------------------------------------------------------------
parts = {"case_base": base, "case_lid": lid, "ssd_2230": ssd, "usbc_plug": plug}
for name, wp in parts.items():
    cq.exporters.export(wp, os.path.join(OUT, name + ".step"))
    cq.exporters.export(wp, os.path.join(OUT, name + ".stl"), tolerance=0.02, angularTolerance=0.1)

board = cq.importers.importStep(BOARD_STEP)

# ---- printable board mock-up (for the fit test) ---------------------------------
# The connector's 3D model from KiCad is a solid block: nothing can be plugged into
# it. The mock-up is the real board and parts, with the card slot cut into CN1 at
# the datasheet height, 1.0 mm high for an FDM print (the real card is 0.8 mm).
SLOT_H = 1.0
slot = (cq.Workplane("XY").workplane(offset=SSD_NEAR - SSD_T - (SLOT_H - SSD_T) / 2)
        .center(CX, (CN1["y0"] - 2 + SSD_EDGE + 0.3) / 2)
        .rect(SSD_W + 0.4, SSD_EDGE + 0.3 - (CN1["y0"] - 2)).extrude(SLOT_H))
mock_parts = []
for v in board.solids().vals():
    b = v.BoundingBox()
    if abs(b.ymin - CN1["y0"]) < 0.05 and b.zmin < -3:          # CN1: cut the slot
        v = cq.Workplane("XY").add(v).cut(slot).val()
    mock_parts.append(v)
mock = cq.Workplane("XY").add(cq.Compound.makeCompound(mock_parts))
cq.exporters.export(mock, os.path.join(OUT, "board_mockup.stl"), tolerance=0.1, angularTolerance=0.5)
cq.exporters.export(mock, os.path.join(OUT, "board_mockup.step"))

# ---- fit checks ------------------------------------------------------------------
def vol(a, b):
    try:
        return a.intersect(b).val().Volume()
    except Exception:
        return 0.0
checks = {
    "SSD in mock-up slot (must be 0)": vol(ssd, mock),
    "SSD x case base": vol(ssd, base), "SSD x case lid": vol(ssd, lid),
    "mock-up x base": vol(mock, base), "mock-up x lid": vol(mock, lid),
    "SSD pad boss top (Z)": SSD_LOW - SSD_PAD["squeeze"],
    "plug x lid": vol(plug, lid), "plug x base": vol(plug, base), "base x lid": vol(base, lid),
}
for k, v in checks.items():
    print(f"{k:34s} {v:8.2f}")
print(f"SSD card: Z {SSD_NEAR - SSD_T:.2f} .. {SSD_NEAR:.2f}, edge Y {SSD_EDGE:.2f}, end {SSD_END:.2f}")
asm = (cq.Assembly(name="eclair_v1")
       .add(board, name="board")
       .add(ssd, name="ssd_2230", color=cq.Color(0.08, 0.12, 0.09))
       .add(base, name="case_base", color=cq.Color(0.10, 0.10, 0.12))
       .add(lid, name="case_lid", color=cq.Color(0.42, 0.48, 0.56, 0.35))
       .add(plug, name="usbc_plug", color=cq.Color(0.12, 0.12, 0.13)))
asm.save(os.path.join(OUT, "eclair_v1_assembly.step"))
asm.save(os.path.join(OUT, "eclair_v1_assembly.glb"))
bb = base.union(lid).val().BoundingBox()
print(f"case: {bb.xlen:.1f} x {bb.ylen:.1f} x {bb.zlen:.1f} mm")
