# -*- coding: utf-8 -*-
"""Main_Project3.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15FXrZvsqeSt8EbAjU95bEzLHO5Jt65h-

**MAIN ASSIGNMENT 3**
"""

import pandas as pd
import numpy as np
from math import sqrt

"""**READ DATA**"""

data = pd.read_csv("https://bit.ly/data_mobil")
input_data = pd.read_csv("https://bit.ly/data_input")

print("\nDataset\n", data)
print("\nData Input\n", input_data)

"""**DEFINE METHODS**"""

def Euclidean(data_test, data_input):
    result = []

    for i in range(len(data_test["Ukuran"])):
        value = 0
        for name in data_test:
            if name == "Nama Mobil":
                continue
            value += (data_test[name][i] - data_input[name][0])**2

        result.append(sqrt(value))

    return result

def Manhattan(data_test, data_input):
    result = []

    for i in range(len(data_test["Ukuran"])):
        value = 0
        for name in data_test:
            if name == "Nama Mobil":
                continue
            value += abs(data_test[name][i] - data_input[name][0])

        result.append(value)

    return result

def Minkowski(data_test, data_input, h):
    result = []

    for i in range(len(data_test["Ukuran"])):
        value = 0
        for name in data_test:
            if name == "Nama Mobil":
                continue
            value += abs(data_test[name][i] - data_input[name][0])**h

        result.append(value**(1/h))

    return result

def Supremum(data_test, data_input):
    result = []

    for i in range(len(data_test["Ukuran"])):
        value = []
        for name in data_test:
            if name == "Nama Mobil":
                continue
            value.append(abs(data_test[name][i] - data_input[name][0]))

        result.append(max(value))

    return result

def knn(size):
    data2 = data.copy()
    data2["manhattan"] = Manhattan(data, input_data)
    data2["euclidean"] = Euclidean(data, input_data)
    data2["minkowski"] = Minkowski(data, input_data, 1.5)
    data2["supremum"] = Supremum(data, input_data)

    man = data2.sort_values(by=["manhattan"])[:size]
    eu = data2.sort_values(by=['euclidean'])[:size]
    mink = data2.sort_values(by=['minkowski'])[:size]
    sp = data2.sort_values(by=['supremum'])[:size]

    man.to_excel('recommend_manhattan.xls', index=False)
    eu.to_excel('recommend_euclidean.xls', index=False)
    mink.to_excel('recommend_minkowski.xls', index=False)
    sp.to_excel('recommend_supremum.xls', index=False)

    return man, eu, mink, sp

if __name__ == "__main__":
    man, eu, mink, sp = knn(3)

    print("\n===recommendation===")
    print("\nManhattan\n", man)
    print("\nEuclidean\n", eu)
    print("\nMinkowski\n", mink)
    print("\nSupremum\n", sp)