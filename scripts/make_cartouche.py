"""Builds CARTOUCHE USB4 from the imported upstream board (MIT, Leaves232):
fab rules of the original (4 layers, 3.5 mil, 0.2 mm vias).

v1.1 (default): the smallest possible board, for a closed case. The board
keeps the original 22.0 x 33.7 mm outline (the electronics fill it), with no
silkscreen text: the name is engraved on the case, and the case holds the
M.2 2230 SSD, as in the original enclosure.
v1.0 (--cartridge): 30 x 64 mm cartridge outline around the SSD, slotted M2
mounting hole, silkscreen. Kept for reference.
The high-speed area (USB4, PCIe) is never modified.

Usage: make_cartouche.py upstream-import.kicad_pcb out.kicad_pcb [--cartridge]"""
import pcbnew, sys
src, dst = sys.argv[1], sys.argv[2]
rules_only = "--cartridge" not in sys.argv[3:]
b = pcbnew.LoadBoard(src)
MM = pcbnew.FromMM
P = lambda x, y: pcbnew.VECTOR2I(MM(x), MM(y))

ds = b.GetDesignSettings()
ds.m_MinClearance = MM(0.0889)          # 3.5 mil
ds.m_TrackMinWidth = MM(0.08)
ds.m_MinThroughDrill = MM(0.2)
ds.m_ViasMinSize = MM(0.3)
ds.m_ViasMinAnnularWidth = MM(0.05)
ds.m_HoleClearance = MM(0.13)
ds.m_HoleToHoleMin = MM(0.2)
ds.m_CopperEdgeClearance = MM(0.1)
ds.m_SolderMaskMinWidth = MM(0)
ds.m_AllowSoldermaskBridgesInFPs = True  # 0.46 mm BGA: no mask web between balls
ds.m_MinSilkTextHeight = MM(0.5)
nc = ds.m_NetSettings.GetDefaultNetclass()
nc.SetClearance(MM(0.0889)); nc.SetTrackWidth(MM(0.08))
nc.SetViaDiameter(MM(0.3)); nc.SetViaDrill(MM(0.2))
nc.SetDiffPairWidth(MM(0.0889)); nc.SetDiffPairGap(MM(0.0889))

if not rules_only:
    # 1. New outline: 30 x 64 mm cartridge, rounded top, chamfered grip end.
    for d in list(b.GetDrawings()):
        if d.GetLayer() == pcbnew.Edge_Cuts:
            b.Remove(d)
    x0, x1, y0, y1, r, ch = 133.5, 163.5, 88.16, 152.0, 3.0, 5.0
    def line(a, c):
        s = pcbnew.PCB_SHAPE(b, pcbnew.SHAPE_T_SEGMENT); s.SetStart(P(*a)); s.SetEnd(P(*c))
        s.SetLayer(pcbnew.Edge_Cuts); s.SetWidth(MM(0.1)); b.Add(s)
    def arc(center, start, end):
        s = pcbnew.PCB_SHAPE(b, pcbnew.SHAPE_T_ARC); s.SetCenter(P(*center)); s.SetStart(P(*start)); s.SetEnd(P(*end))
        s.SetLayer(pcbnew.Edge_Cuts); s.SetWidth(MM(0.1)); b.Add(s)
    line((x0 + r, y0), (x1 - r, y0))
    arc((x1 - r, y0 + r), (x1 - r, y0), (x1, y0 + r))
    line((x1, y0 + r), (x1, y1 - ch))
    line((x1, y1 - ch), (x1 - ch, y1))
    line((x1 - ch, y1), (x0 + ch, y1))
    line((x0 + ch, y1), (x0, y1 - ch))
    line((x0, y1 - ch), (x0, y0 + r))
    arc((x0 + r, y0 + r), (x0, y0 + r), (x0 + r, y0))

    # 2. Slotted M2 hole for the SSD screw (non plated, 2.2 mm, 6 mm travel).
    fp = pcbnew.FOOTPRINT(b)
    fp.SetReference("H1"); fp.SetValue("M2 SSD 2230")
    pad = pcbnew.PAD(fp)
    pad.SetAttribute(pcbnew.PAD_ATTRIB_NPTH); pad.SetShape(pcbnew.PAD_SHAPE_OVAL)
    pad.SetDrillShape(pcbnew.PAD_DRILL_SHAPE_OBLONG)
    pad.SetSize(pcbnew.VECTOR2I(MM(2.2), MM(6.2))); pad.SetDrillSize(pcbnew.VECTOR2I(MM(2.2), MM(6.2)))
    pad.SetLayerSet(pad.UnplatedHoleMask())
    fp.Add(pad)
    fp.SetPosition(P(148.5, 145.0))
    b.Add(fp)

    # 3. Silkscreen on the top side, over the SSD area (no parts there).
    def text(s, x, y, h, bold=False, layer=pcbnew.F_SilkS, thick=None):
        t = pcbnew.PCB_TEXT(b); t.SetText(s); t.SetPosition(P(x, y)); t.SetLayer(layer)
        t.SetTextSize(pcbnew.VECTOR2I(MM(h), MM(h))); t.SetTextThickness(MM(thick or h * (0.2 if bold else 0.15)))
        t.SetBold(bold); t.SetHorizJustify(pcbnew.GR_TEXT_H_ALIGN_CENTER); b.Add(t)
    text("CARTOUCHE", 148.5, 128.0, 3.2, bold=True)
    text("L'IA dans votre poche", 148.5, 132.6, 1.3)
    text("USB4 40 Gb/s · NVMe 2230", 148.5, 137.2, 1.1)
    text("SSD", 148.5, 149.2, 1.0)
    text("v1.0 · base: Leaves232 USB4 2230 (MIT)", 148.5, 140.4, 0.7)

pcbnew.SaveBoard(dst, b)
bb = b.GetBoardEdgesBoundingBox()
print("ok", flush=True)
