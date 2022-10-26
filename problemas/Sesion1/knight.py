import datetime
import sys
from datetime import time
from typing import TextIO

from algoritmia.datastructures.graphs import UndirectedGraph
from algoritmia.algorithms.traversers import bf_vertex_traverser




Vertex = tuple[int, int]
Edge = tuple[Vertex, Vertex]


def knight_graph(rows: int, cols: int, ) -> UndirectedGraph[Vertex]:
    vertices: list[Vertex] = []
    for r in range(rows):
        for c in range(cols):
            vertices.append((r, c))

    # ojo con generar aristas repetidas( en lugar de 8 calcula 4 [abajo])
    edges: list[Edge] = []
    for r, c in vertices:
        for ir, ic in [(1, -2), (2, -1), (2, 1), (1, 2)]:  # vecrtor de incrementos
            r2 = r + ir
            c2 = c + ic
            if (r2, c2) in vertices:  # 0<=r2<rows and 0<=c2<cols
                edges.append(((r, c), (r2, c2)))
    return UndirectedGraph(V=vertices, E=edges)


def read_data(f: TextIO) -> tuple[int, int, int, int]:
    rows = int(f.readline())
    cols = int(f.readline())
    firstrow = int(f.readline())
    firstcol = int(f.readline())
    return rows, cols, firstrow, firstcol


def process(rows: int, cols: int, firstrow: int, firstcol: int) -> tuple[UndirectedGraph[Vertex], int]:
    g = knight_graph(rows, cols)
    # constructor de listas con iteradores lo completa --> for O(n)
    vertices: list[Vertex] = list(bf_vertex_traverser(g, (firstrow, firstcol)))
    return g, len(vertices)


def show_results(num: int):
    print(num)


if __name__ == '__main__':
    rows0, cols0, firstrow0, firstcol0 = read_data(sys.stdin)
    g0, num0 = process(rows0, cols0, firstrow0, firstcol0)
    show_results(num0)

