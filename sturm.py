#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 10:44:40 2021

"""

#Algoritmo de Sturm

def division (v, p):
    f = list(v)
    n = p[0]
    for i in range (len(v)-(len(p)-1)):
        f[i] = f[i]/n 
        co = f[i]
        if co!= 0: 
            for j in range(1, len(p)):
                f[i + j] = f[i + j] - p[j] * co
    b = -(len(p)-1)
    x = f[b:]
    while x[0] == 0:
        x.pop(0)
    return f[:b], x
Jeje