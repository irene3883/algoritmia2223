
#!/usr/bin/env python3
import sys
from typing import TextIO


def read_data(f: TextIO) -> list[int]:
#En l tenemos una cadena por línea:
    lines = f.readlines()
# Transformamos cada línea en un entero:
    return [int(line) for line in lines]


def show_results(nums: list[int]):
# Recorremos las listas con el bucle for
    for num in nums:
        print(num)


if __name__ == "__main__":
    #si hacemos import de otro se ejecuta el main de ese, el main
    #solo se ejecutará si es el prog principal.(poner siempre)
    nums = read_data(sys.stdin)
    show_results(nums)
#resultado en terminal : python3 lee.py < nums/nums10 > solucion10.txt
#PS1=pract1$  --> cambiar el pwd