#Ex 1
def cmmdc(a, b):
    while(b != 0):
        t = b
        b = a%b
        a = t
    return a

#a = int(input("Scrie 2 numere:"))
#b = int(input())
#print(cmmdc(a, b))

#Ex 2
def vowels(str):
    result = 0
    for char in str:
        if("aeiouAEIOU".find(char) != -1):
            result = result + 1
    return result

print(vowels("Test de string"))

#Ex 3
def occurences(token, str):
    result = 0
    i = 0
    while(str.find(token, i) != -1):
        i = str.find(token, i)+1
        result = result + 1
    return result

print(occurences("123", "12123123456123456123"))

#Ex 4
def convert(str):
    result = ""
    for i in range(0, len(str)):
        if(str[i].isupper() and i > 0):
            result = result + '_'
        result = result + str[i].lower()
    return result

print(convert("HelloWorldLowerCase"))

#Ex 5
def matrix(mat):
    result = ""
    a = 0
    b = 0
    aEnd = len(mat)
    bEnd = len(mat[0])

    while(a < aEnd and b < bEnd):
        for i in range(b, bEnd):
            result = result + mat[a][i]
        a += 1

        for i in range(a, aEnd):
            result = result + mat[i][bEnd-1]
        bEnd -= 1

        if (a < aEnd):
            for i in range(bEnd - 1, b - 1, -1):
                result = result + mat[aEnd - 1][i]
            aEnd -= 1
 
        if (b < bEnd):
            for i in range(aEnd - 1, a - 1, -1):
                result = result + mat[i][b]
            b += 1

    return result


print(matrix(
    [['f', 'i', 'r', 's'],
     ['n', '_', 'l', 't'],
     ['o', 'b', 'a', '_'],
     ['h', 't', 'y', 'p']]
))

#Ex 6

def palindrome(a):
    s = str(a)
    for i in range(0, len(s)):
        if(s[i] != s[len(s)-1-i]):
            return False
    return True

print(palindrome(103201))

#Ex 7

def toNumber(s):
    start = -1
    for i in range(0, len(s)):
        if(start == -1 and s[i].isnumeric()):
            start = i
        if(start != -1 and not s[i].isnumeric()):
            return s[start:i]
    return ""

print(toNumber("An apple is 123 USD"))

#Ex 8
def onesBinary(a):
    return bin(a).count('1')

print(onesBinary(24))

#Ex 9
def letter(s):
    dict = {}

    for e in s:
        if e.isalpha():
            if e in dict:
                dict[e] = dict[e] + 1
            else:
                dict[e] = 1

    return max(dict, key=dict.get)

print(letter("an apple is not a tomato"))

#Ex 10
def words(s):
    return len(s.split(" "))

print(words("This Python Script Is Great"))