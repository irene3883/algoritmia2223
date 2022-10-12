import sys
from random import shuffle
from typing import TextIO
from algoritmia.datastructures.graphs import UndirectedGraph
from algoritmia.datastructures.mergefindsets import MergeFindSet
from algoritmia.viewers.labyrinth_viewer import LabyrinthViewer

Vertex = tuple[int,int]
Edge = tuple[Vertex,Vertex]
def read_data(f: TextIO) -> tuple[int, int]:
    rows = int(f.readline())
    cols = int(f.readline())
    return rows, cols


def process(rows: int, cols: int) -> UndirectedGraph:
    #paso 1
    vertices: list[Vertex] = []     #indicar tipos con chicha
    for r in range(rows):
        for c in range(cols):
            v = (r,c)
            vertices.append(v)  #append((r,c))
    #print(f'DEBUG vertices: {vertices}')

    #paso2
    mfs = MergeFindSet()  #cuando dos objetos con diferente etiqueta hace merge, la etiqueta pasa a ser la misma
    for v in vertices:
        mfs.add(v)
    #print(f'DEBUG mfs: {mfs}')




    #paso3                                                     r-1 c
    #añadir cada vertice arriba izquierda y no las 4.   r c-1   r c
    # dentro :   r-1 >=0 r>=1 r>0   --> arista insertar

    edges: list[Edge] = []
    for v in vertices:
        r,c = v
        if r > 0:
            e: Edge = ((r,c), (r-1, c))  #edges.append(((r,c),(r-1,c)))
            edges.append(e)
        if c >0:
            edges.append(((r,c),(r,c-1)))
    shuffle(edges)
    # print(f'DEBUG edges: {edges}')


    #Paso 4
    corridors: list[Edge] = []

    #Paso 5
    for e in edges:
        u,v = e
        if mfs.find(u) != mfs.find(v):
            mfs.merge(u,v)
            corridors.append(e)

    return UndirectedGraph(E = corridors)


def show_results(labyrinth: UndirectedGraph):
    print(labyrinth)


if __name__ == "__main__":
    rows, cols = read_data(sys.stdin)
    #rows, cols=2,3  (para trabajar)
    labyrinth = process(rows, cols)
    lv = LabyrinthViewer(labyrinth, canvas_width=800,canvas_height=600, wall_width=1)
    lv.run()
