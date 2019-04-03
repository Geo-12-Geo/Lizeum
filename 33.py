n = input()
n = n.replace('(', ' ')
n = n.replace(')', ' ')
n = n.split(' ')
first = n[0]
second = n[2]
if len(first) > len(second):
    k = len(first) - len(second)
    second = list(second)
    for i in range(k):
        second.insert(0, '0')
    second = ''.join(second)
if len(first) < len(second):
    k = len(second) - len(first)
    first = list(first)
    for i in range(k):
        first.insert(0, '0')
    first = ''.join(first)


def my_sum(first, second):
    result = ''
    r = len(first)
    for i in range(r):
        if first[i] == '-' and second[i] == '-':
            result += '-+'
        if first[i] == '0' and second[i] == '-':
            result += '-'
        if first[i] == '-' and second[i] == '0':
            result += '-'
        if first[i] == '+' and second[i] == '0':
            result += '+'
        if first[i] == '0' and second[i] == '+':
            result += '+'
        if first[i] == '+' and second[i] == '+':
            result += '+-'
        if first[i] == '0' and second[i] == '0':
            result += '0'
        if first[i] == '+' and second[i] == '-':
            result += '0'
        if first[i] == '-' and second[i] == '+':
            result += '0'
    return result


if n[1] == '+':
    print(my_sum(first, second))

if first == '-' and n[1] == '-' and second == '-':
    print('')

else:
    if n[1] == '-':
        second = second.replace('+', 'x').replace('-', '+').replace('x', '-')
        summ = my_sum(first, second)
        i = summ[0]
        if i == '0':
            while i == '0':
                if len(summ) == 0:
                    print('')
                summ = summ.replace(i, '', 1)
                i = summ[0]
    print(summ)

