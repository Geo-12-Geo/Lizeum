from random import randint
s = set()
for i in range(5):
    k = []
    for j in range(5):
        if i == 2 and j == 2:
            k.append(' 0')
        else:
            x = randint(1,75)
            while x in s:
                x = randint(1,75)
            s.add(x)
            if 0 < x < 10:
                k.append(str(x))
            else:
                k.append(str(x))
    print(*k)
    k.clear()