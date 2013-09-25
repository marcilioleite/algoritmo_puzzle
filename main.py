from timer import Timer
from search import search

matrix = [[0,1,0,0,0],
          [0,0,1,0,0],
          [1,1,1,1,1],
          [1,0,1,0,1],
          [1,0,1,0,1]]

matching = []

with Timer() as t:             
    search(matrix, matching, 2, 2)
print "Elapsed time: %s s" % t.secs

print matching