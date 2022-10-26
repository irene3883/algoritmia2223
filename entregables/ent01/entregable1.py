#!/usr/bin/env python3
import sys
from random import shuffle, seed
from typing import TextIO, Optional

from algoritmia.datastructures.graphs import UndirectedGraph
from algoritmia.datastructures.mergefindsets import MergeFindSet
from algoritmia.datastructures.queues import Fifo

Vertex = tuple[int, int]
Edge = tuple[Vertex, Vertex]

NO_VALID_WALL = 'NO VALID WALL'


# Función ya implementada
# Esta función utiliza un MFSet para crear un laberinto, pero le añade n aristas
# adicionales que provocan que el laberinto tenga ciclos.
def create_labyrinth(rows: int, cols: int, n: int, s: int) -> UndirectedGraph[Vertex]:
    vertices: list[Vertex] = [(r, c) for r in range(rows) for c in range(cols)]
    mfs: MergeFindSet[Vertex] = MergeFindSet((v,) for v in vertices)
    edges: list[Edge] = [((r, c), (r + 1, c)) for r in range(rows - 1) for c in range(cols)]
    edges.extend([((r, c), (r, c + 1)) for r in range(rows) for c in range(cols - 1)])
    seed(s)
    shuffle(edges)
    corridors: list[Edge] = []
    for (u, v) in edges:
        if mfs.find(u) != mfs.find(v):
            mfs.merge(u, v)
            corridors.append((u, v))
        elif n > 0:
            n -= 1
            corridors.append((u, v))
    return UndirectedGraph(E=corridors)


def bf_search(g: UndirectedGraph[Vertex], source: Vertex, target: Vertex, rows: int, cols: int) -> tuple[list[int],list[Edge]]:
    res: list[Edge] = []
    matriz = [0]*rows
    for i in range(rows): matriz[i]=[0]*cols
    queue: Fifo[Edge] = Fifo()
    seen: set[Vertex] = set()
    queue.push((source, source))
    seen.add(source)
    tamaño = 0
    while len(queue) > 0:
        u, v = queue.pop()
        r,c=v
        res.append((u, v))
        tamaño=matriz[r][c]+1
        if v == target:
            return matriz,res
        for suc in g.succs(v):
            if suc not in seen:
                queue.push((v, suc))
                seen.add(suc)
                matriz[suc[0]][suc[1]]=tamaño
    raise RuntimeError(f'Vértice {target} no alcanzable desde {source}')


def path_recover(edges: list[Edge],
                 target: Vertex) -> list[Vertex]:
    # construir bp
    bp: dict[Vertex, Vertex] = {}
    for u, v in edges:
        bp[v] = u

    # Recuperar caminos target(while)
    v = target
    path: list[Vertex] = [v]  # parte del camino
    while v != bp[v]:  # averiguar padre/abuelo de v hasta que llegue al principio
        v = bp[v]  # lista fantasma
        path.append(v)

    # invertir camino y devolverlo
    path.reverse()
    return path


def read_data(f: TextIO) -> tuple[UndirectedGraph[Vertex], int, int]:
    rows = int(f.readline())
    cols = int(f.readline())
    n = int(f.readline())
    s = int(f.readline())
    g: UndirectedGraph[Vertex] = create_labyrinth(rows, cols, n, s)
    return g, rows, cols


def process(lab: UndirectedGraph[Vertex], rows: int, cols: int) -> tuple[Optional[Edge], int, int]:
    inicio = (0,0)
    fin = (rows - 1, cols - 1)
    min = rows + cols -2
    matriza ,caminoa = bf_search(lab, inicio, fin, rows,cols)
    matrizd, caminod = bf_search(lab,fin,inicio, rows,cols)
    actual = viejo = len(path_recover(caminoa,fin))-1
    existentes= set(lab.E)
    pared : Edge= None
    if viejo == min:
        return None, viejo, actual
    for r in range(rows):
        for c in range(cols):
            if r<rows-1:
                ed: Edge = ((r,c),(r+1, c))
                if ed not in existentes:
                    antes = matriza[r][c]
                    despues = matrizd[r+1][c]
                    if antes != 0 and despues != 0:
                        nuevo = (matriza[r][c] + matrizd[r+1][c]) + 1
                        if nuevo == min:
                            return ed, viejo, nuevo
                        elif nuevo < actual:
                            actual = nuevo
                            pared = ed
                        elif nuevo == actual:
                            if pared!= None and ed < pared:
                                pared = ed

            if c< cols-1:
                ed: Edge = ((r, c), (r, c+1))
                if ed not in existentes:
                    antes = matriza[r][c]
                    despues = matrizd[r ][c+1]
                    if antes != 0 and despues != 0:
                        nuevo = (matriza[r][c] + matrizd[r][c+1]) + 1
                        if nuevo == min:
                            return ed, viejo, nuevo
                        elif nuevo < actual:
                            actual = nuevo
                            pared = ed
                        elif nuevo == actual:
                            if pared!= None and ed < pared:
                                pared = ed
            if r> 0:
                ed : Edge = ((r-1,c), (r,c))
                if ed not in existentes:
                    antes = matriza[r][c]
                    despues = matrizd[r-1][c]
                    if antes != 0 and despues != 0:
                        nuevo = (matriza[r][c] + matrizd[r-1][c]) + 1
                        if nuevo == min:
                            return ed, viejo, nuevo
                        elif nuevo < actual:
                            actual = nuevo
                            pared = ed
                        elif nuevo == actual:
                            if pared!= None and ed < pared:
                                pared = ed

            if c>0:
                ed: Edge= ((r,c-1),(r,c))
                if ed not in existentes:
                    antes = matriza[r][c]
                    despues = matrizd[r ][c-1]
                    if antes != 0 and despues != 0:
                        nuevo = (matriza[r][c] + matrizd[r][c-1]) + 1
                        if nuevo == min:
                            return ed, viejo, nuevo
                        elif nuevo < actual:
                            actual = nuevo
                            pared = ed
                        elif nuevo == actual:
                            if pared!= None and ed < pared:
                                pared = ed
    return pared, viejo, actual


def show_results(edge_to_add: Optional[Edge], length_before: int, length_after: int):
    if edge_to_add is None:
        print('NO VALID WALL')
    else:
        u,v=edge_to_add
        u1,u2=u
        v1,v2=v
        print(u1,u2,v1,v2)
    print(length_before)
    print(length_after)


if __name__ == '__main__':
    graph0, rows0, cols0 = read_data(sys.stdin)
    edge_to_add0, length_before0, length_after0 = process(graph0, rows0, cols0)
    show_results(edge_to_add0, length_before0, length_after0)
