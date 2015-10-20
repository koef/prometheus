#!/usr/bin/env python


def saddle_point(matrix):
    row_numb = 0
    if len(matrix) == 1 and type(matrix[0])==int:
        return (0, 0)

    for row in matrix:
        l_min = row.index(min(row))
        r_min = len(row) - 1 - row[::-1].index(min(row))
        if l_min == r_min:
            x = l_min
            y = row_numb
            row_numb_t = 0
            not_saddle = False
            for row_t in range(len(matrix)):
                if row_numb != row_numb_t:
                    if row[x] <= matrix[row_t][x]:
                        not_saddle = True
                        break
                row_numb_t += 1
            if not not_saddle:
                return (y, x)
        row_numb += 1
    return False


print saddle_point([[2], [4], [5]])