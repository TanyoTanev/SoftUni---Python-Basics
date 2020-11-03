'''
Годзила срещу Конг

Снимките за дългоочаквания филм "Годзила срещу Конг" започват. Сценаристът Адам Уингард ви моли да напишете програма, която да изчисли,
дали предвидените средства са достатъчни за снимането на филма. За снимките  ще бъдат нужни определен брой статисти, облекло за всеки
един статист и декор.

Известно е, че:
Декорът за филма е на стойност 10% от бюджета.
При повече от 150 статиста,  има отстъпка за облеклото на стойност 10%.

Вход
От конзолата се четат 3 реда:
Бюджет за филма – реално число в интервала [1.00 … 1000000.00]
Брой на статистите – цяло число в интервала [1 … 500]
Цена за облекло на един статист – реално число в интервала [1.00 … 1000.00]

Изход

На конзолата трябва да се отпечатат два реда:
Ако  парите за декора и дрехите са повече от бюджета:
"Not enough money!"
"Wingard needs {парите недостигащи за филма} leva more."
Ако парите за декора и дрехите са по малко или равни на бюджета:
"Action!"
"Wingard starts filming with {останалите пари} leva left."
Резултатът трябва да е форматиран до втория знак след десетичната запетая.

15437.62
186
57.99

'''


budget = float(input())
number_statists = int(input())
cost_costumes = float(input())

#decore = budget * 0.1
if number_statists > 150 :
    cost_costumes = cost_costumes * 0.9

#total_cost_costumes = cost_costumes * number_statists
total_cost = cost_costumes * number_statists + budget * 0.1

if total_cost > budget:
    print("Not enough money!")
    print(f"Wingard needs {total_cost - budget:.2f} leva more.")

else:
    print(f"Action!")
    print(f"Wingard starts filming with {budget - total_cost:.2f} leva left.")

