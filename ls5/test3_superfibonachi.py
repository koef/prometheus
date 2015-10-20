#!/usr/bin/env python
def super_fibonacci(n, m):
    sf_list = []
    for c in range(n):
        if c < m:
            sf_list.append(1)
        else:
            i = c - m 
            cur_row = 0
            while i <= c - 1:
                cur_row += sf_list[i]
                i += 1
            sf_list.append(cur_row)

    return sf_list[n - 1]

print super_fibonacci(9, 3)
