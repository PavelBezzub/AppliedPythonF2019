#!/usr/bin/env python
# coding: utf-8
def calculate_determinant(list_of_lists):
    m = len(list_of_lists)
    def determinant(list_of_lists, m):
        def GetMatr(mas, p, i, j, m):
            di = 0
            for ki in range(m - 1):
                if (ki == i):
                    di = 1
                dj = 0
                for kj in range(m - 1):
                    if (kj == j):
                        dj = 1
                    p[ki][kj] = mas[ki + di][kj + dj]
        p = [0] * m
        for i in range(m):
            p[i] = [0] * m
        j = 0
        d = 0
        k = 1
        n = m - 1
        if (m < 1 ):
            return None
        if (m == 1):
            d = list_of_lists[0][0]
            return (d)
        if (m == 2):
            d = (list_of_lists[0][0] * list_of_lists[1][1]) - (list_of_lists[1][0] * list_of_lists[0][1])
            return (d)
        if (m > 2):
            for i in range(m):
                GetMatr(list_of_lists, p, i, 0, m)
                d = d + k * list_of_lists[i][0] * determinant(p, n)
                k = -k
        return (d)
        raise NotImplementedError
