#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    #Дано предложение. Удалить из него все буквы с (как в кириллице так и на латинице).
    s = input("Введите предложение: ")
    s = s.replace('c', '')  # eng
    s = s.replace('с', '')  # rus
    print(s)