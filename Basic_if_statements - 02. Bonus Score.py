'''
Бонус точки

Дадено е цяло число – начален брой точки. Върху него се начисляват бонус точки по правилата, описани по-долу. Да се напише програма,
която пресмята бонус точките, които получава числото и общия брой точки (числото + бонуса).

Ако числото е до 100 включително, бонус точките са 5;
Ако числото е по-голямо от 100, бонус точките са 20% от числото;
Ако числото е по-голямо от 1000, бонус точките са 10% от числото.

Допълнителни бонус точки (начисляват се отделно от предходните):
За четно число  + 1 т.
За число, което завършва на 5  + 2 т.
Примерен вход и изход

вход
изход
'''

given_number = int(input())
bonus = 0

if given_number <= 100:
    bonus = bonus + 5
elif given_number > 1000:
    bonus = given_number * 0.1
elif given_number > 100:
    bonus = given_number * 0.2

leftover = given_number % 2
#leftover_5 = given_number / 5
#finish_5 = leftover_5 % 2

if leftover == 0:
    bonus = bonus + 1
elif given_number % 10 == 5:
    bonus = bonus + 2

print(bonus)
print(given_number + bonus)
