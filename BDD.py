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

    def boolean_R(self):
        expression = ""
        for i in self.gdict:
            binary_key = format(self.gdict.keys(), '05b')
            expression += "("
            for j in range(len(binary_key)):
                if binary_key[j] == "0":
                    expression += "~xx" + str(j)
                else:
                    formula += "xx" + str(j)
                if j != len(binary_key) - 1:
                    expression += " & "
            expression += ")"
            if self.gdict.keys() != 31:
                expression += " | "


R = graph()

# add satisfied edges to graph
for i in range(0, 32):
    for j in range(0, 32):
        if (i + 3) % 32 == j % 32 or (i + 8) % 32 == j % 32:
            R.addEdge((i, j))


xx1, xx2, xx3, xx4, xx5, yy1, yy2, yy3, yy4, yy5 = map(
    exprvar, "xx1, xx2, xx3, xx4, xx5, yy1, yy2, yy3, yy4, yy5".split())

even_nums = [val for val in range(32) if val % 2 == 0]  # array of even numbers

prime_nums = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31]  # array of prime numbers


def boolean_even(even_nums):
    formula = ""
    for i in range(len(even_nums)):
        binary = format(even_nums[i], '05b')
        formula += "("
        for j in range(len(binary)):
            if binary[j] == "0":
                formula += "~xx" + str(j)
            else:
                formula += "xx" + str(j)
            if j != len(binary) - 1:
                formula += " & "
        formula += ")"
        if i != len(even_nums) - 1:
            formula += " | "

    print('\n\n' + "EVEN: " + formula + '\n\n')
    return formula

def boolean_prime(prime_nums):
    formula = ""
    for i in range(len(prime_nums)):
        binary = format(prime_nums[i], '05b')
        formula += "("
        for j in range(len(binary)):
            if binary[j] == "0":
                formula += "~yy" + str(j)
            else:
                formula += "yy" + str(j)
            if j != len(binary) - 1:
                formula += " & "
        formula += ")"
        if i != len(prime_nums) - 1:
            formula += " | "

    print("PRIME: " + formula + '\n\n')
    return formula




EVEN = expr(boolean_even(even_nums))
PRIME = expr(boolean_prime(prime_nums))

EVEN = expr2bdd(EVEN)
PRIME = expr2bdd(PRIME)


