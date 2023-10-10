import random as rng

num = rng.randrange(1, 100)
print("Ghiceste un numar de la 1 la 100:")

value = -1
tries = 0
while(value != num):
    value = int(input())
    tries = tries + 1
    dist = abs(value - num)

    if(dist < 5):
        print("Foarte cald")
    elif(dist < 10):
        print("Cald")
    elif(dist < 40):
        print("Rece")
    else:
        print("Foarte Rece")

print("Bravo, ai ghicit numarul {0} in {1} incercari".format(num, tries))