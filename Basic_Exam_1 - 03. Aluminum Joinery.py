'''
Задача 3. Алуминиева дограма
Фирма-производител на алуминиева дограма приема поръчки за изработката и монтаж със следния ценоразпис за един брой. Фирмата приема
 само поръчки на едро (над 10 бр.). В зависимост от поръчания брой дограми, фирмата прави различна отстъпка на своите клиенти.
Фирмата предлага също и доставка на поръчките си срещу 60 лв.
Размер	Единична цена	Отстъпка от цената
90X130	110 лв.	 Над 30 броя – 5%
 Над 60 броя – 8%
100X150	140 лв.	 Над 40 броя – 6%
   Над 80 броя – 10%
130X180	190 лв.	 Над 20 броя – 7%
   Над 50 броя – 12%
200X300	250 лв.	 Над 25 броя – 9%
   Над 50 броя – 14%

Ако поръчката надвишава 99 броя  – върху крайната цена се начисляват допълнителни 4% отстъпка (след като се начисли цената за доставка,
ако има такава).
При поръчка под 10 бр. на конзолата да бъде изписано "Invalid order"
Вход:

Потребителят въвежда 3 реда:
1.	Брой дограми – цяло число в интервала [0..1000];
2.	Вид на дограмите – текст "90X130" или "100X150" или "130X180" или "200X300";
3.	Начин на получаване – текст
•	С доставка - "With delivery"
•	Без доставка - "Without delivery"

Изход:
Извежда се едно число – стойността на поръчката, в следния формат:
o	"{Обща стойност на поръчката} BGN"
Резултатът да се форматира до втори знак след десетичната запетая.

'''

number_windows = int(input())
type_window = input()
delivery_or_not = input()
cost_per_window = 0
total_cost = 0

if number_windows <= 10:
    print(f"Invalid order")

else:

    if type_window == '90X130':
        if number_windows <= 30:
            cost_per_window = 110
        elif number_windows > 30 and number_windows <= 60:
            cost_per_window = 110 * 0.95
        elif number_windows > 60:
            cost_per_window = 110 * 0.92

    elif type_window == '100X150':
        if number_windows <= 40:
            cost_per_window = 140
        elif number_windows > 40 and number_windows <= 80:
            cost_per_window = 140 * 0.94
        elif number_windows > 80:
            cost_per_window = 140 * 0.90

    elif type_window == '130X180':
        if number_windows <= 20:
            cost_per_window = 190
        elif number_windows > 20 and number_windows <= 50:
            cost_per_window = 190 * 0.93
        elif number_windows > 50:
            cost_per_window = 190 * 0.88

    elif type_window == '200X300':
        if number_windows <= 25:
            cost_per_window = 250
        elif number_windows > 25 and number_windows <= 50:
            cost_per_window = 250 * 0.91
        elif number_windows > 50:
            cost_per_window = 250 * 0.86

    if delivery_or_not == 'With delivery':
        total_cost +=60

    total_cost += number_windows * cost_per_window
    if number_windows > 99:
        total_cost = total_cost * 0.96

    print(f"{total_cost:.2f} BGN")