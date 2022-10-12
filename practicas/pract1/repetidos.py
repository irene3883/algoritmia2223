
#!/usr/bin/env python3
import sys
from typing import TextIO


def read_data(f: TextIO) -> list[int]:
#En l tenemos una cadena por línea:
    lines = f.readlines()
# Transformamos cada línea en un entero:
    return [int(line) for line in lines]


def average(nums: list[int]) -> float:
    return sum(nums)/len(nums) #len es gratis, sum coste lineal coste =  Theta(n)

def process(data: list[int]) -> bool:  #bucles anidados coste Theta(n²)
    repeated = False
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            if data[i] == data[j]:
                repeated = True
    return repeated


def process1(data: list[int]) -> bool:  #depende de mejor o peor caso: Theta(n) o O(n²)
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            if data[i] == data[j]:
                return True;
    return False


def process2(data: list[int]) -> bool:  #depende de mejor o peor caso: Theta(n) o O(n²)
    data_s =sorted(data) #coste siempre el mismo = 0(n*log n) un poco mas que n
    prev = data_s[0]-1
    for num in data_s:
        if prev == num:
            return True  #n veces 0(1) 0(n)
        prev= num
    return False

def show_result(result: bool):
    print("No hay repetidos" if not result else "Hay repetidos")


if __name__ == "__main__":
    #si hacemos import de otro se ejecuta el main de ese, el main
    #solo se ejecutará si es el prog principal.(poner siempre)
    nums = read_data(sys.stdin)
    result = process(nums)
    show_result(result)


#resultado en terminal : python3 lee.py < nums/nums10 > solucion10.txt
#PS1=pract1$  --> cambiar el pwd