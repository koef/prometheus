# -*- coding: utf-8 -*-
__author__ = 'koef'


def make_sudoku(size):
    sudoku = []
    counter = 1
    for y in range(size**2):
        sudoku.append([])
        for x in range(size**2):
            sudoku[y].append(counter)
            counter += 1
            if counter == size**2+1:
                counter = 1
        if (y+1) % size == 0:
            counter -= size + 2
        else:
            counter += size
        if counter > size**2:
            counter -= size**2
        if counter < 1:
            counter += size**2-1
    return sudoku


print make_sudoku(1)

for line in make_sudoku(4):
    string = ""
    for row in line:
        string += "% 4d" % row
    print string
