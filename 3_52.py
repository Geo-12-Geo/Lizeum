n = int(input()) 
d = {} 
for i in range(n): 
    surname = input().strip() 
    d[surname] = d.get(surname, 0)+1 

    for n, surname in sorted((-v, k) for k, v in d.items()): 
        print(surname, -n)