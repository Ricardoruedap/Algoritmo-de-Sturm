#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 10:44:40 2021

"""

#Algoritmo de Sturm

def division (v, p):
    n = p[0]
    Lista = list(v)
    for i in range (len(v)-(len(p)-1)):
        Lista[i] = Lista[i]/n 
        coef = Lista[i]
        if coef!= 0: 
            for j in range(1, len(p)):
                Lista[j + i] = - p[j] * coef + Lista[i + j]
    z = -(len(p)-1)
    x_0 = Lista[z:]
    while x_0[0] == 0:
        x_0.pop(0)
    return Lista[:z], x_0

#Se pidiran las siguientes cosas, la funcion que por lo que se va a necesitar una funcion esta se metera en forma de lista, y tambien se va a pedir un rango menor y mayor, que sirve para encontrar los siguientes datos   
def raices (Coeficientes,izq,der):
#Se crea una variable con unalista vacia para despues llenar los datos 
    li = []
#Se guardan los elementos de la funcion (coeficientes) en otra lista gracias a la funcion ".append"
    li.append(Coeficientes)
    derivada = []
#Se crea un for donde se toma como el rango la lista en este caso "Coeficientes" ya que esta 
    for i in range(len(Coeficientes)-1):
        aux_3 = -(i-len(Coeficientes)+1)*Coeficientes[i]
        derivada.append(aux_3)
    n=len(derivada)
    li.append(derivada)
    l1st = []
    l2 = []
    c1 = 0
    c2 = 0
    while n > 1 :
        n_1 = len(li)
        a = li[n_1-2]
        b = li[n_1-1]
        h,c = division(a, b)
        for i in range(len(c)):
            c[i] = c[i]*-1
        li.append(c)
        n = len(c)
    for i in range(len(li)):
        aux = 0
        r = len(li[i])
        for l in range(r):
            aux = aux*izq+li[i][l]
        l1st.append(aux)
        aux = 0
        for k in range(r):
            aux = aux*der+li[i][k]
        l2.append(aux)
    print("Evolución de las cadenas:\n")
    print(l1st)
    print("\n", l2)
    for i in range(len(l1st)-1):
        if l1st[i] > 0:
            if l1st[i+1] > 0:
                c1 = c1+0
            else:
                c1 = c1+1
        else:
            if l1st[i+1] < 0:
                c1= c1+0
            else:
                c1 = c1+1
    for i in range(len(l2)-1):
        if l2[i] > 0:
            if l2[i+1] > 0:
                c2 = c2+0
            else:
                c2 = c2+1
        else:
            if l2[i+1] < 0:
                c2 = c2+0
            else:
                c2 = c2+1
    
    print("\n Para la función f(x) = x^6 - 4x^3 + x - 2 se encontraron:", c1-c2, "raíces en el intervalo") 
    print("[", izq, ",", der, "]")
raices([1,0,0,-4,0,1,-2],-2,2)
