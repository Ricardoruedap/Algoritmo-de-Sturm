#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 11:38:05 2021

@author: eduardomv
"""

import time

#La solución es 0.56409973
'''
La linea 17 es equivalente al siguiente código:
    
def mi_funcion(x):
    return x**3 + 5*x - 3
'''
mi_funcion = lambda x: x**3 + 5*x - 3
Coef = [1.0, 0.0, 5.0, -3.0]
derivar = lambda f, x, h=0.0001: (f(x+h)-f(x-h))/(2*h)

def Horner_method(coefs, z):
    n = len(coefs) - 1
    b = coefs[0]
    c = b
    for i in range(1,n):
        b = coefs[i] + z * b
        c = b + z*c
    b = coefs[n] + z * b
     
    return b, c


def Newton_method(f, x_start, umbral, iter_max):
    x_sol = x_start
    if isinstance(f, list):           
        f_x = 1
        for i in range(iter_max):
            if abs(f_x) < umbral:
                return x_sol
            f_x, f_prima_x = Horner_method(f, x_sol)
            x_sol = x_sol - (f_x/f_prima_x)
            file.write("{:2d}. {:.8f}\n".format(i+1,x_sol))
    else:
        for i in range(iter_max):
            f_x = f(x_sol)
            f_prima_x = derivar(f, x_sol)
            x_sol = x_sol - f_x/f_prima_x
            file.write("{:2d}. {:.8f}\n".format(i+1,x_sol))
            if abs(f(x_sol)) < umbral:
                return x_sol

file = open("Newton_Horner.txt", "w+")
file.write("f(x) = x^3 + 5x - 3\n\n")
file.write("Coeficientes de la ecuación de grado 3: 1, 0, 5, 3.\n\n")
file.write("Raíz encontrada en Newton-Horner:\n")
tiempo_inicio1 = time.perf_counter()
print(Newton_method(Coef, 0, 0.0001, 1000))
tiempo_computo1 = time.perf_counter() - tiempo_inicio1
file.write("El tiempo de cómputo fue {:2f} segundos.\n".format(tiempo_computo1))
file.write("\n Raíz en Newton:\n")
tiempo_inicio2 = time.perf_counter()
print(Newton_method(mi_funcion, 0, 0.0001, 1000))
tiempo_computo2 = time.perf_counter() - tiempo_inicio2
file.write("El tiempo de cómputo fue {:2f} segundos.".format(tiempo_computo2))
file.close()

#mi_funcion_sol1 = Newton_method(mi_funcion, 0, 0.0001, 1000) 
#mi_funcion_sol2 = Newton_method(Coef, 0, 0.0001, 1000) 
tiempo_inicio = time.perf_counter()
tiempo_computo = time.perf_counter() - tiempo_inicio

#pito
