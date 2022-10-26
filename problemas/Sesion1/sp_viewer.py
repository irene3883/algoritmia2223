
from shortest_path import process
from algoritmia.viewers.labyrinth_viewer import LabyrinthViewer

g_lab, path= process(15 ,20)
lv = LabyrinthViewer(g_lab)
lv.add_path(path)
lv.run()
