'''
01. Number Pyramid
Напишете програма, която чете цяло число n, въведено от потребителя, и отпечатва пирамида от числа като в
примерите:

'''

n = int(input())
is_bigger_than_current = 0
i = 1

for rows in range(1, n + 1):
    for cols in range(1, rows + 1):
        if i > n:
            is_bigger_than_current = 1
            break
        print(f"{i} ", end='')
        i +=1
    if is_bigger_than_current:
        break
    print()