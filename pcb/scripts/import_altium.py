import pcbnew, sys
# Map every Altium layer KiCad is unsure about automatically (no dialog).
io = pcbnew.PCB_IO_MGR.PluginFind(pcbnew.PCB_IO_MGR.ALTIUM_DESIGNER)
props = pcbnew.STRING_UTF8_MAP() if hasattr(pcbnew, "STRING_UTF8_MAP") else None
board = io.LoadBoard(sys.argv[1], None, props) if props is not None else io.LoadBoard(sys.argv[1], None)
pcbnew.SaveBoard(sys.argv[2], board)
bb = board.GetBoardEdgesBoundingBox()
print("footprints", len(board.GetFootprints()), "tracks", len(board.GetTracks()), "copper", board.GetCopperLayerCount(), "size", round(pcbnew.ToMM(bb.GetWidth()),2), "x", round(pcbnew.ToMM(bb.GetHeight()),2), flush=True)
