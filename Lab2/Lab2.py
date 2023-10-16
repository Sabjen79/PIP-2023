#Ex0

def ex0(n):
    return int(n*(n+1)/2)

#print(ex0(9))

#Ex1
def ex1(l):
    return " ".join([hex(ord(x))[2:] for x in l])

#print(ex1(['1', '2', '3']))