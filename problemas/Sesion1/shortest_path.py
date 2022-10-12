import sys
from typing import TextIO

from algoritmia.datastructures.queues import Fifo

from labyrinth import create_labyrinth
from algoritmia.datastructures.graphs import UndirectedGraph

Vertex= tuple[int, int]
Edge=tuple[Vertex, Vertex]


def bf_search(g: UndirectedGraph[Vertex], source: Vertex, target: Vertex) -> list[Edge]:
    res: list[Edge] = []
    queue: Fifo[Edge] = Fifo()
    seen: set[Vertex] = set()
    queue.push((source, source))
    seen.add(source)
    while len(queue) > 0:
        u, v = queue.pop()
        res.append((u, v))
        if v == target:
            return res
        for suc in g.succs(v):
            if suc not in seen:
                queue.push((v, suc))
                seen.add(suc)
    raise RuntimeError(f'Vértice {target} no alcanzable desde {source}')


def path_recover(edges: list[Edge],
                     target: Vertex) -> list[Vertex]:
    #construir bp
    bp: dict[Vertex, Vertex] = {}
    for u,v in edges:
        bp[v]=u

    #Recuperar caminos target(while)
    v=target
    path: list[Vertex] = [v] #parte del camino
    while v != bp[v]: #averiguar padre/abuelo de v hasta que llegue al principio
        v = bp[v] #lista fantasma
        path.append(v)

    #invertir camino y devolverlo
    path.reverse()
    return path


def read_data(f: TextIO) -> tuple[int, int]:
    rows = int(f.readline())
    cols = int(f.readline())
    return rows, cols


def process(rows: int, cols: int) -> tuple[UndirectedGraph[Vertex], list[Vertex]]:
    g_lab = create_labyrinth(rows,cols)
    edges= bf_search(g_lab, (0, 0), (rows-1, cols-1))
    path= path_recover(edges, (rows-1,cols-1))
    return g_lab,path

def show_results(path: list[Vertex]):
    for v in path:
        print(v)


if __name__ == '__main__':
    rows0, cols0= read_data(sys.stdin)
    g_lab0,path0=process(rows0,cols0)
    show_results(path0)


