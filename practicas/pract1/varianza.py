
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

def process(nums: list[int]) -> float:
    s = 0
    for num in nums:   #se hará n veces ( la talla siempre será n, no se puede tocar)
                        #Theta(n)
        s += (num - average(nums)) ** 2  #exponente es gratis, suma tambien, average es lo mas caro
                                        # n veces Theta(n) = Theta(n²)
        #la media no cambia, es siempre igual, se puede sacar y calcular 1 vez
    return s / len(nums)
#algoritmo cuadrático = ineficiente


def precess1(nums: list[int]) -> float:
    s=0
    avg = average(nums)     #Theta(n)
    for num in nums:        #Theta(n)
        s+=(num-avg) ** 2   #n veces Theta(1) = Theta(n)
    return s/len(nums)
def show_results(v: float):
# Recorremos las listas con el bucle for
    print(v)


if __name__ == "__main__":
    #si hacemos import de otro se ejecuta el main de ese, el main
    #solo se ejecutará si es el prog principal.(poner siempre)
    nums = read_data(sys.stdin)
    v= process(nums)
    show_results(v)
#resultado en terminal : python3 lee.py < nums/nums10 > solucion10.txt
#PS1=pract1$  --> cambiar el pwd