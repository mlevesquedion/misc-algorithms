rows, cols = 100, 201


# how short/DRY can we make this code?
x = int(rows/2) + 1 if rows % 2 == 1 else int(rows/2)
y = int(cols/2) + 1 if cols % 2 == 1 else int(cols/2)
xref, yref = x, y


# this is pretty good
x = rows//2 + rows % 2
y = cols//2 + cols % 2
assert x, y == (xref, yref)


# needs more functions
x = sum(divmod(rows, 2))
y = sum(divmod(cols, 2))
assert x, y == (xref, yref)


# how about a one liner
from itertools import starmap
x, y = map(sum, starmap(divmod, zip([rows, cols], [2] * 2)))
assert x, y == (xref, yref)


# numpy
import numpy as np
x, y = np.array(np.divmod([rows, cols], 2)).sum(axis=0)
assert x, y == (xref, yref)
