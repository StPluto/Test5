#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    #Вариант 13. Дано предложение. Вывести «столбиком» все его буквы и, стоящие на четных местах.
    n = (input("Введите предложение:"))
    for i, letter in enumerate(n):
        if letter == "и" and not i % 2:
            print(f"{letter}")