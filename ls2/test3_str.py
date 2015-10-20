#!/usr/bin/env python
import sys

x = float(sys.argv[1])
y = float(sys.argv[2])
z = float(sys.argv[3])

if x > 1:
    kupl = 'la' + '-la' * (int(x)-1)
elif x == 1:
    kupl = 'la'
else:
    kupl = ''

if y >= 1 and kupl != '':
    song = (' ' + kupl) * int(y)
else:
    song = ''

if z == 1:
    song = song + '!'
else:
    song = song + '.'

print 'Everybody sing a song:' + song
