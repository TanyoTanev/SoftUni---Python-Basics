'''
3. Суми прости и непрости числа
Напишете програма, която чете от конзолата цели числа, докато не се получи команда &quot;stop&quot;. Да се намери
сумата на всички въведени прости и сумата на всички въведени непрости числа. Тъй като по дефиниция от
математиката отрицателните числа не могат да бъдат прости, ако на входа се подаде отрицателно число, да
се изведе следното съобщение &quot;Number is negative.&quot;. В този случай въведено число се игнорира и не се
прибавя към нито една от двете суми, а програмата продължава своето изпълнение, очаквайки въвеждане на
следващо число.
На изхода да се отпечатат на два реда двете намерени суми в следния формат:
&quot;Sum of all prime numbers is: {prime numbers sum}&quot;
&quot;Sum of all non prime numbers is: {nonprime numbers sum}&quot;


3
9
0
7
19
4
stop

30
83
33
-1
20
stop

'''

command = ''
digits = list()

while True:

    command = input()
    if command == 'stop':
        break
    else:
        digit = int(command)
        if digit < 0:
            print(f"Number is negative.")
        else:
           digits.append(digit)

sum_prime = 0
sum_not_prime = 0
is_not_prime = 0

for i in range(len(digits)):
    is_not_prime = 0
    for k in range(2, digits[i]):
        if digits[i] > 1:
            if digits[i] % k == 0:
                is_not_prime = 1
                sum_not_prime += digits[i]
                break
    if is_not_prime == 0:
        sum_prime += digits[i]

print(f"Sum of all prime numbers is: {sum_prime}")
print(f"Sum of all non prime numbers is: {sum_not_prime}")