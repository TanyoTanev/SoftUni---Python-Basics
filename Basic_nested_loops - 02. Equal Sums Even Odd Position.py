'''
2. Еднакви суми на четни и нечетни позиции
Напишете програма, която чете от конзолата две шестцифрени цели числа в диапазона. Винаги първото
въведено число ще бъде по-малко от второто. На конзолата да се отпечатат на 1, ред разделени с интервал,
всички числа, които се намират между двете, прочетени от конзолата числа, и отговарят на условието сумата
от цифрите на четни и нечетни позиции да са равни. Ако няма числа, отговарящи на условието на конзолата
не се извежда резултат.

'''

digit_one = int(input())
digit_two = int(input())

sum_odd = 0
sum_even = 0
digit_to_print = ''
list_numbers = list()

for i in range(digit_one, digit_two + 1):
    digit_to_str = str(i)
    sum_odd = 0
    sum_even = 0
    for k in range(len(digit_to_str)):
        if k % 2 == 1:
            sum_odd += int(digit_to_str[k])
        else:
            sum_even += int(digit_to_str[k])
    if sum_even == sum_odd:
        list_numbers.append(digit_to_str)

if len(list_numbers):
    print(" ".join(list_numbers))

