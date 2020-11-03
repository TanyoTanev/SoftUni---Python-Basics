'''
Конвертор за мерни единици

Да се напише програма, която преобразува разстояние между следните 3 мерни единици: mm, cm, m. Използвайте съответствията от таблицата по-долу:

входна единица
изходна единица

1 meter (m)
1000 millimeters (mm)
1 meter (m)
100 centimeters (cm)

Входните данни се състоят от три реда, въведени от потребителя:
Първи ред: число за преобразуване - реално число;
Втори ред: входна мерна единица – текст;
Трети ред: изходна мерна единица (за резултата) – текст.
'''

number = float(input())
first_metric = str(input())
second_metric = str(input())

if first_metric == 'mm' and second_metric == 'm':
    print(f"{number/1000:.3f}")
elif first_metric == 'mm' and second_metric == 'cm':
    print(f"{number/10:.3f}")

elif first_metric == 'cm' and second_metric == 'm':
    print(f"{number / 100:.3f}")
elif first_metric == 'cm' and second_metric == 'mm':
    print(f"{number * 10:.3f}")

elif first_metric == 'm' and second_metric == 'cm':
    print(f"{number * 100:.3f}")
elif first_metric == 'm' and second_metric == 'mm':
    print(f"{number * 1000:.3f}")