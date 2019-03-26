m, n = map(int,input().split()) 
a = set() 
b = set() 
for i in range(m): 
    a.add(input()) 
for i in range(n): 
    b = input() 
    if b in a: 
        print('YES') 
    else: 
        print('NO')