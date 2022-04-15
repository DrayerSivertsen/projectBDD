from pyeda.inter import *

# create graph G that satisfies, all 0 ≤ i, j ≤ 31, there is an edge from node 
# i to node j iff (i + 3) % 32 = j%32 or (i + 8) % 32 = j % 32

class graph:
    def __init__(self):
        self.gdict = dict() # create dictionary for the graph to be represented

    def addEdge(self, edge): # function adds an edge to the graph
        vert1, vert2 = edge[0], edge[1]
        if vert1 in self.gdict.keys():
            self.gdict[vert1].append(vert2)
        else:
            self.gdict[vert1] = [vert2]

    def printGraph(self): # prints the graph by dict keys and item list
        for key, list in self.gdict.items():
            print(key, list)

    def boolean_R(self): # contructs the boolean expression for R
        expression = ""
        dict_list = list(self.gdict.items()) # change the dictionary into a list

        new_dict_list = []
        for dict_tuple in dict_list:
            new_dict_list.append((dict_tuple[0], dict_tuple[1][0]))
            new_dict_list.append((dict_tuple[0], dict_tuple[1][1]))

        for i in range(len(new_dict_list)):
            pair = new_dict_list[i]
            binary_key = format(pair[0], '05b') # convert number to binary
            expression += "("
            for j in range(len(binary_key)):
                if binary_key[j] == "0":
                    expression += "~xx" + str(j + 1)
                else:
                    expression += "xx" + str(j + 1)
                if j != len(binary_key) - 1:
                    expression += " & "
            expression += ")"

            expression += " & "

            binary_key = format(pair[1], '05b') # convert number to binary
            expression += "("
            for j in range(len(binary_key)):
                if binary_key[j] == "0":
                    expression += "~yy" + str(j + 1)
                else:
                    expression += "yy" + str(j + 1)
                if j != len(binary_key) - 1:
                    expression += " & "
            expression += ")"

            if self.gdict.keys() != 31:
                expression += " | "
        expression = expression[:-3] # remove the extra spaces and '|'

        # print(expression)

        return expression


R = graph() # initalize the graph R

# add satisfied edges to graph
for i in range(0, 32):
    for j in range(0, 32):
        if (i + 3) % 32 == j % 32 or (i + 8) % 32 == j % 32:
            R.addEdge((i, j))

# create bddvars to be used in bdd test cases and manipulation
xx1, xx2, xx3, xx4, xx5, yy1, yy2, yy3, yy4, yy5, zz1, zz2, zz3, zz4, zz5 = map(bddvar, 
"xx1 xx2 xx3 xx4 xx5 yy1 yy2 yy3 yy4 yy5 zz1 zz2 zz3 zz4 zz5".split())


even_nums = [val for val in range(32) if val % 2 == 0]  # array of even numbers

prime_nums = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31]  # array of prime numbers

# R.printGraph()


def boolean_even(even_nums): # construct the boolean expression for EVEN
    formula = ""
    for i in range(len(even_nums)):
        binary = format(even_nums[i], '05b') # convert number to binary
        formula += "("
        for j in range(len(binary)):
            if binary[j] == "0":
                formula += "~yy" + str(j + 1)
            else:
                formula += "yy" + str(j + 1)
            if j != len(binary) - 1:
                formula += " & "
        formula += ")"
        if i != len(even_nums) - 1:
            formula += " | "

    # print('\n\n' + "EVEN: " + formula + '\n\n')
    return formula


def boolean_prime(prime_nums): # construct boolean expression for PRIME
    formula = ""
    for i in range(len(prime_nums)):
        binary = format(prime_nums[i], '05b') # convert number to binary
        formula += "("
        for j in range(len(binary)):
            if binary[j] == "0":
                formula += "~xx" + str(j + 1)
            else:
                formula += "xx" + str(j + 1)
            if j != len(binary) - 1:
                formula += " & "
        formula += ")"
        if i != len(prime_nums) - 1:
            formula += " | "

    # print("PRIME: " + formula + '\n\n')
    return formula

# convert boolean strings to an expression and then to a bdd (assigning to relative var)
EVEN = expr2bdd(expr(boolean_even(even_nums)))
PRIME = expr2bdd(expr(boolean_prime(prime_nums)))
RR = expr2bdd(expr(R.boolean_R()))


# step3.1. Obtain BDDs RR, EVEN , PRIME for the finite sets R, [even], [prime] , respectively.
# Pay attention to the use of BDD variables in your BDDs. Your code shall also verify the following
# test cases:

print("\n\n******** Test Cases ********")

# RR(27, 3) is true;
num1 = format(27, '05b') # convert to binary
num2 = format(3, '05b') # convert to binary

# assign each binary digit to a bddvar passing a dictionary of the elements into the restrict command
if RR.restrict({xx1: int(num1[0]), xx2: int(num1[1]), xx3: int(num1[2]), xx4: int(num1[3]), xx5: int(num1[4]), yy1: int(num2[0]),
yy2: int(num2[1]), yy3: int(num2[2]), yy4: int(num2[3]), yy5: int(num2[4])}):
    print("RR(27, 3) is true\n")
else:
    print("RR(27, 3) is false\n")

# RR(16, 20) is false;
num1 = format(16, '05b') # convert to binary
num2 = format(20, '05b') # convert to binary

# assign each binary digit to a bddvar passing a dictionary of the elements into the restrict command
if RR.restrict({xx1: int(num1[0]), xx2: int(num1[1]), xx3: int(num1[2]), xx4: int(num1[3]), xx5: int(num1[4]), yy1: int(num2[0]),
yy2: int(num2[1]), yy3: int(num2[2]), yy4: int(num2[3]), yy5: int(num2[4])}):
    print("RR(16, 20) is true\n")
else:
    print("RR(16, 20) is false\n")


# EVEN (14) is true;
num2 = format(14, '05b') # convert to binary

# assign each binary digit to a bddvar passing a dictionary of the elements into the restrict command
if EVEN.restrict({yy1: int(num2[0]), yy2: int(num2[1]), yy3: int(num2[2]), yy4: int(num2[3]), yy5: int(num2[4])}):
    print("EVEN(14) is true\n")
else:
    print("EVEN(14) is false\n")


# EVEN (13) is false;
num2 = format(13, '05b') # convert to binary

# assign each binary digit to a bddvar passing a dictionary of the elements into the restrict command
if EVEN.restrict({yy1: int(num2[0]), yy2: int(num2[1]), yy3: int(num2[2]), yy4: int(num2[3]), yy5: int(num2[4])}):
    print("EVEN(13) is true\n")
else:
    print("EVEN(13) is false\n")


# PRIME(7) is true;
num1 = format(7, '05b') # convert to binary

# assign each binary digit to a bddvar passing a dictionary of the elements into the restrict command
if PRIME.restrict({xx1: int(num1[0]), xx2: int(num1[1]), xx3: int(num1[2]), xx4: int(num1[3]), xx5: int(num1[4])}):
    print("PRIME(7) is true\n")
else:
    print("PRIME(7) is false\n")


# PRIME(2) is false.
num1 = format(2, '05b') # convert to binary

# assign each binary digit to a bddvar passing a dictionary of the elements into the restrict command
if PRIME.restrict({xx1: int(num1[0]), xx2: int(num1[1]), xx3: int(num1[2]), xx4: int(num1[3]), xx5: int(num1[4])}):
    print("PRIME(2) is true\n")
else:
    print("PRIME(2) is false\n")

# step3.2. Compute BDD RR2 for the set R ◦R, from BDD RR. Herein, RR2 encodes the set of
# node pairs such that one can reach the other in two steps. Your code shall also verify the following
# test cases:

def composefunc(side1, side2): # allows for the reordering of variables
    side1 = side1.compose({yy1:zz1, yy2:zz2, yy3:zz3, yy4:zz4, yy5:zz5}) # map y variables to z
    side2 = side2.compose({xx1:zz1, xx2:zz2, xx3:zz3, xx4:zz4, xx5:zz5}) # map x variables to z

    return (side1 & side2).smoothing({zz1, zz2, zz3, zz4, zz5}) # smooths the two composed sides over variable z


RR2 = composefunc(RR, RR) # compose RR and RR resulting in RR2

print("******** Test Cases ********")

# RR2(27, 6) is true;
num1 = format(27, '05b') # convert to binary
num2 = format(6, '05b') # convert to binary

# assign each binary digit to a bddvar passing a dictionary of the elements into the restrict command
if RR2.restrict({xx1: int(num1[0]), xx2: int(num1[1]), xx3: int(num1[2]), xx4: int(num1[3]), xx5: int(num1[4]), yy1: int(num2[0]),
yy2: int(num2[1]), yy3: int(num2[2]), yy4: int(num2[3]), yy5: int(num2[4])}):
    print("RR2(27, 6) is true\n")
else:
    print("RR2(27, 6) is false\n")


# RR2(27, 9) is false.
num1 = format(27, '05b') # convert to binary
num2 = format(9, '05b') # convert to binary

# assign each binary digit to a bddvar passing a dictionary of the elements into the restrict command
if RR2.restrict({xx1: int(num1[0]), xx2: int(num1[1]), xx3: int(num1[2]), xx4: int(num1[3]), xx5: int(num1[4]), yy1: int(num2[0]),
yy2: int(num2[1]), yy3: int(num2[2]), yy4: int(num2[3]), yy5: int(num2[4])}):
    print("RR2(27, 9) is true\n")
else:
    print("RR2(27, 9) is false\n")


# step3.3. Compute the transitive closure RR2star of RR2. Herein, RR2star encodes the set of
# all node pairs such that one can reach the other in a positive even number of steps.
RR2star = RR2
while True: # continue until condition is broken
    RR2star_new = RR2star
    RR2star = (RR2star_new | composefunc(RR2star_new, RR2)) # return RR2starNew or the composition of New and RR2
    if RR2star_new.equivalent(RR2star): # break if RR2star_new and RR2star are equal
        break


# step3.4. Here comes the most difficult part. We first StatementA formally:
# ∀u. (PRIME(u) →∃v. (EVEN(v) ∧ RR2star(u, v))).
print("******** Statement A ********")

u = [xx1, xx2, xx3, xx4, xx5] # u is mapped to bits x
v = [yy1, yy2, yy3, yy4, yy5] # v is mapped to bits y

boolean = (EVEN & PRIME & RR2star).smoothing(v) # existential quantifier elimination method
statementA = ~PRIME | boolean

# to check that RR2star was implemented correctly
# print("Check if RR2star has empty imputs: ", RR2star.inputs) # used to make sure inputs are empty
# print("Verify the return value of RR2star is true: ", RR2star.equivalent(True))


# print("Statement A truth value: " +  str(statementA.equivalent(True)))
print("Statement A truth value: " +  str(bool(statementA)) + '\n')


