import decimal
import copy
import numpy as np

#Ex0
def ex0(n):
    return int(n*(n+1)/2)

print(ex0(9))

#Ex1
def ex1(l):
    return " ".join([hex(ord(x))[2:] for x in l])

print(ex1(['A', 'B', 'C']))

#Ex2
def ex2(l):
    result = " ".join([bin(x)[2:].rjust(8, '0') for x in l])
    return ", ".join([result, str(result.count('0')), str(result.count('1'))])

print(ex2([0,1,2,3,4]))

#Ex3
def ex3(a, b):
    decimal.getcontext().prec = 100
    return decimal.Decimal(a) / decimal.Decimal(b)

print(ex3(5, 3))

#Ex4
def ex4(coef, constants):
    D = np.linalg.det(coef)

    result = []

    for i in range(0, len(coef)):
        mat = copy.deepcopy(coef)
        for index, row in enumerate(mat):
            row[i] = constants[index]
        result.append(np.linalg.det(mat) / D)
    
    return result

print(ex4(
    [[2, 3, -1, 4], 
     [1, -2, 1, 2], 
     [3, 0, 2, 5], 
     [4, 1, 3, 6]], 
     [7, 3, 4, 8]
))

#Ex5
def ex5(x, n):
    nn = (n-1)/n
    x0 = 2

    for i in range(1, 100):
        x0 = (n-1)/n*x0 + x/n*(1/x0**(n-1))

    return x0
        

print(ex5(64, 3))

#Ex6
def ex6(n, p, alphabet):
    result = ""
    l = len(alphabet)
    for index in range(0, p):
        r = n%l
        n = (n - r)//l
        result = alphabet[r] + result
    return result

print(ex6(3, 2, "abc"))

#Ex7 - nu am inteles enuntul

#Ex8
def ex8(values):
    i = 1
    total = values[0] + values[-1]
    for y in values[1:-1]:
        if i % 2 == 0:
            total += 2 * y
        else:
            total += 4 * y
        i += 1
    return total * (1.0 / 3.0)

print(ex8([6,6,6,6,7,8,9,9,9,8,12,14,13,9,8,8,8,4,3,3,3]))