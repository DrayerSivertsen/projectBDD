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
        dict_list = list(self.gdict.items())

        new_dict_list = []
        for dict_tuple in dict_list:
            new_dict_list.append((dict_tuple[0], dict_tuple[1][0]))
            new_dict_list.append((dict_tuple[0], dict_tuple[1][1]))

        for i in range(len(new_dict_list)):
            duo = new_dict_list[i]
            binary_key = format(duo[0], '05b')
            expression += "("
            for j in range(len(binary_key)):
                if binary_key[j] == "0":
                    expression += "~xx" + str(j)
                else:
                    expression += "xx" + str(j)
                if j != len(binary_key) - 1:
                    expression += " & "
            expression += ")"

            expression += " & "

            binary_key = format(duo[1], '05b')
            expression += "("
            for j in range(len(binary_key)):
                if binary_key[j] == "0":
                    expression += "~yy" + str(j)
                else:
                    expression += "yy" + str(j)
                if j != len(binary_key) - 1:
                    expression += " & "
            expression += ")"

            if self.gdict.keys() != 31:
                expression += " | "
        expression = expression[:-3]

        print(expression)

        return expression


R = graph()

# add satisfied edges to graph
for i in range(0, 32):
    for j in range(0, 32):
        if (i + 3) % 32 == j % 32 or (i + 8) % 32 == j % 32:
            R.addEdge((i, j))


xx1, xx2, xx3, xx4, xx5, yy1, yy2, yy3, yy4, yy5 = map(
    bddvar, "xx1, xx2, xx3, xx4, xx5, yy1, yy2, yy3, yy4, yy5".split())

even_nums = [val for val in range(32) if val % 2 == 0]  # array of even numbers

prime_nums = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31]  # array of prime numbers

# R.printGraph()

def boolean_even(even_nums):
    formula = ""
    for i in range(len(even_nums)):
        binary = format(even_nums[i], '05b')
        formula += "("
        for j in range(len(binary)):
            if binary[j] == "0":
                formula += "~yy" + str(j)
            else:
                formula += "yy" + str(j)
            if j != len(binary) - 1:
                formula += " & "
        formula += ")"
        if i != len(even_nums) - 1:
            formula += " | "

    # print('\n\n' + "EVEN: " + formula + '\n\n')
    return formula

def boolean_prime(prime_nums):
    formula = ""
    for i in range(len(prime_nums)):
        binary = format(prime_nums[i], '05b')
        formula += "("
        for j in range(len(binary)):
            if binary[j] == "0":
                formula += "~xx" + str(j)
            else:
                formula += "xx" + str(j)
            if j != len(binary) - 1:
                formula += " & "
        formula += ")"
        if i != len(prime_nums) - 1:
            formula += " | "

    # print("PRIME: " + formula + '\n\n')
    return formula




EVEN_ = expr(boolean_even(even_nums))
PRIME_ = expr(boolean_prime(prime_nums))
RR_ = expr(R.boolean_R())

EVEN = expr2bdd(EVEN_)
PRIME = expr2bdd(PRIME_)
RR = expr2bdd(RR_)


# step3.1. Obtain BDDs RR, EV EN , P RIM E for the finite sets R, [even], [prime] , respectively.
# Pay attention to the use of BDD variables in your BDDs. Your code shall also verify the following
# test cases:

# RR(27, 3) is true;
num1 = format(27, '05b')
num2 = format(3, '05b')

if(RR.restrict({xx1:int(num1[0]), xx2:int(num1[1]), xx3:int(num1[2]), xx4:int(num1[3]), xx5:int(num1[4]), yy1:int(num2[0]), 
yy2:int(num2[1]), yy3:int(num2[2]), yy4:int(num2[3]), yy5:int(num2[4])})):
    print("RR(27, 3) is true\n")
else:
    print("RR(27, 3) is false\n")

# RR(16, 20) is false;
num1 = format(16, '05b')
num2 = format(20, '05b')

if(RR.restrict({xx1:int(num1[0]), xx2:int(num1[1]), xx3:int(num1[2]), xx4:int(num1[3]), xx5:int(num1[4]), yy1:int(num2[0]), 
yy2:int(num2[1]), yy3:int(num2[2]), yy4:int(num2[3]), yy5:int(num2[4])})):
    print("RR(16, 20) is true\n")
else:
    print("RR(16, 20) is false\n")
# EVEN (14) is true;
num2 = format(14, '05b')

if(EVEN.restrict({yy1:int(num2[0]), yy2:int(num2[1]), yy3:int(num2[2]), yy4:int(num2[3]), yy5:int(num2[4])})):
    print("EVEN(14) is true\n")
else:
    print("EVEN(14) is false\n")
# EVEN (13) is false;
num2 = format(13, '05b')

if(EVEN.restrict({yy1:int(num2[0]), yy2:int(num2[1]), yy3:int(num2[2]), yy4:int(num2[3]), yy5:int(num2[4])})):
    print("EVEN(13) is true\n")
else:
    print("EVEN(13) is false\n")
# PRIME(7) is true;
num1 = format(7, '05b')

if(PRIME.restrict({xx1:int(num1[0]), xx2:int(num1[1]), xx3:int(num1[2]), xx4:int(num1[3]), xx5:int(num1[4])})):
    print("PRIME(7) is true\n")
else:
    print("PRIME(7) is false\n")
# PRIME(2) is false.
num1 = format(2, '05b')

if(PRIME.restrict({xx1:int(num1[0]), xx2:int(num1[1]), xx3:int(num1[2]), xx4:int(num1[3]), xx5:int(num1[4])})):
    print("PRIME(2) is true\n")
else:
    print("PRIME(2) is false\n")


# step3.2. Compute BDD RR2 for the set R ◦R, from BDD RR. Herein, RR2 encodes the set of
# node pairs such that one can reach the other in two steps. Your code shall also verify the following
# test cases:
# RR2(27, 6) is true;
# RR2(27, 9) is false.
