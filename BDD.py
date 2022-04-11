import pyeda
from pyeda.inter import *

# create graph
class graph:
    def __init__(self):
        self.gdict = dict()
    # get the keys of the dictionary
    def addEdge(self, edge):
        vert1, vert2 = edge[0], edge[1]
        if vert1 in self.gdict.keys():
            self.gdict[vert1].append(vert2)
        else:
            self.gdict[vert1] = [vert2]
    def printGraph(self):
        for key, list in self.gdict.items():
            print(key, list)



R = graph()

# add satisfied edges to graph
for i in range(0, 32):
    for j in range(0, 32):
        if (i + 3) % 32 == j % 32 or (i + 8) % 32 == j % 32:
            R.addEdge((i,j))


xx1, xx2, xx3, xx4, xx5, yy1, yy2, yy3, yy4, yy5 = map(exprvar, "xx1, xx2, xx3, xx4, xx5, yy1, yy2, yy3, yy4, yy5".split())







