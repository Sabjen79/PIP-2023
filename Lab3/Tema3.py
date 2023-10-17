import math

# Ex 1
def ex1(n):
    if n == 1: return [1]
    if n == 2: return [1, 1]

    result = [1, 1]
    a = 1
    b = 1
    for i in range(2, n):
        result.append(a+b)
        a, b = b, a+b

    return result

print(ex1(15))

# Ex 2
def prime(n):
    if n == 1: return False
    if n == 2: return True
    for d in range(3, int(n/2)+1, 2):
        if n%d == 0: return False
    return True

def ex2(l):
    result = []
    for x in l:
        if prime(x): result.append(x)
    return result

print(ex2([2,5,6,7,13,121,137]))

# Ex 3
def ex3(A, B):
    return [x for x in A if x in B], [x for x in set(A+B)], [x for x in A if x not in B], [x for x in B if x not in A]

print(ex3([1,2,3,4,5],[3,4,5,6,7]))

# Ex 4
def ex4(notes, moves, start):
    result = [notes[start]]
    for x in moves:
        start += x
        result.append(notes[start % len(notes)])
    return result

print(ex4(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2))

# Ex 5
def ex5(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if(i > j): mat[i][j] = 0
    return mat

print(ex5([
    [ 1,  2,  3,  4],
    [ 5,  6,  7,  8],
    [ 9, 10, 11, 12],
    [13, 14, 15, 16]
]))

# Ex 6
def ex6(*lists, x):
    biglist = []
    for l in lists:
        for item in l:
            biglist.append(item)
    result = []
    for item in biglist:
        if biglist.count(item) == x and result.count(item) == 0: result.append(item)
    return result

print(ex6([1,2,3], [2,3,4],[4,5,6], [4,1, "test"], x=2))

# Ex 7
def palindrome(n):
    s = str(n)
    for i in range(int(len(s)/2)):
        if(s[i] != s[len(s)-1-i]): return False
    return True

def ex7(l):
    n = 0
    g = -1
    for item in l:
        if palindrome(item):
            n += 1
            g = max(g, item)
    return (n, g)

print(ex7([123,121,1,524,6006]))

# Ex 8
def ex8(strlist, x=1, flag=True):
    result = []
    for item in strlist:
        l = []
        for char in item:
            if (flag==True and ord(char)%x==0) or (flag==False and ord(char)%x!=0):
                l.append(char)
        result.append(l)
    return result

print(ex8(["test", "hello", "lab002"], x=2, flag = False))

# Ex 9
def ex9(mat):
    result = []
    for col in range(len(mat[0])):
        x = -1
        for row in range(len(mat)):
            if(mat[row][col] <= x):
                result.append((row, col))
            x = max(x, mat[row][col])
    return result


print(ex9([
    [1, 2, 3, 2, 1, 1],
    [2, 4, 4, 3, 7, 2],
    [5, 5, 2, 5, 6, 4],
    [6, 6, 7, 6, 7, 5]
]))

# Ex 10
def ex10(*lists):
    result = []
    for i in range(max([len(x) for x in lists])):
        t = ()
        for l in lists:
            if(i < len(l)):
                t += (l[i],)
            else:
                t += (None,)
        result.append(t)
    return result

print(ex10([1,2,3], [5,6,7], ["a", "b", "c", "d"]))

# Ex 11
def sorting_alg(elem):
    return elem[1][2]

def ex11(tuples):
    tuples.sort(key=sorting_alg)
    return tuples

print(ex11([('abc', 'bcd'), ('abc', 'zza')]))

# Ex 12
def ex12(words):
    result = []

    while len(words) > 0:
        new_list = [words.pop(0)]
        for w in words:
            if(new_list[0][-2:] == w[-2:]):
                new_list.append(w)
                words.remove(w)
        result.append(new_list)
    return result
        
print( ex12(['ana', 'banana', 'carte', 'arme', 'parte']) )