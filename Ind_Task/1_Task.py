#!/usr/bin/nev python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    # Ввести кортеж одной строкой.
    A = tuple(input("Введите элементы: ").split())
    pred = []

    for i, element in enumerate(A):
        if pred == element:
            print("Элементы кортежа после пары одинаковых элементов: ", A[i+1:])
            break
        pred = element
