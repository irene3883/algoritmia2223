from algoritmia.viewers.graph2d_viewer import Graph2dViewer

from knight import process

g, num = process(2,5,0,0)
print(f'Vertices alcanzables: {num}')
gv = Graph2dViewer(g, vertexmode=Graph2dViewer.ROW_COL)
gv.run()
