'''
Задача 6. Баркод Генератор
Техниката в магазин за коледни украси се разваля. Артикулите, които съдържат четни числа в своя баркод не могат да бъдат
маркирани от касиерите. Вашата задача е, да напишете програма, която генерира всички баркодове, които НЕ съдържат четни цифри в себе си.

Вход:
•	Две четирицифрени числа, които показват обхвата на баркодовете, които трябва да промените.
•	Първи ред – четирицифрено число – началото на обхвата. Цяло число в интервала [1000…9999]
•	Втори ред – четирицифрено число – края на обхвата. Цяло число в интервала [1000…9999]
Изход:
На конзолата трябва да се отпечатат всички "баркодове", които НЕ съдържат четна цифра в себе си, разделени с интервал.
'''

first_code = int(input())
second_code = int(input())
odd_codes = list()
number_to_string_first = str(first_code)
number_to_string_second = str(second_code)

#for number in range (first_code, second_code):
    #number_to_string = str(number)

for thousands in range( int(number_to_string_first[0]), int(number_to_string_second[0])+1 ):
    if thousands % 2 != 0:

        for hundreds in range(int(number_to_string_first[1]), int(number_to_string_second[1]) + 1):
            if hundreds % 2 != 0:

                for tens in range(int(number_to_string_first[2]), int(number_to_string_second[2]) + 1):
                    if tens % 2 != 0:

                        for ones in range(int(number_to_string_first[3]), int(number_to_string_second[3]) + 1):
                            if ones % 2 != 0:

                                code_to_print = ''.join([str(thousands) , str(hundreds), str(tens), str(ones)])
                                odd_codes.append(code_to_print)


print(" ".join(odd_codes))