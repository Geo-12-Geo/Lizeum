from itertools import product # Команда from ... import позволяет вам импортировать не весь модуль целиком, а только определенное его содержимое.

dropsuit = input()
 
suits = ['пик', 'треф', 'бубен', 'червей']
nominals = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз')
 
suits.remove(dropsuit) # Удаляет первый элемент в списке, имеющий значение x. ValueError, если такого элемента не существует
 
for n, s in product(nominals, suits):
    print(n, s)