import math

while 1:
    a = int(input("How many spaces? "))
    print('%0.*f' % (a, math.pi))
    b = input("wanna continue y/n?")
    if b == "n":
        break
    elif b == "y":
        continue
    else:
        print("nanai?, bye")
