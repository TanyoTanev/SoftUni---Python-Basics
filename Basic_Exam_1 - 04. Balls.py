'''
Задача 4. Топки
В кутия имаме неопределен брой топки с различни цветове, които ни носят различен брой точки. Задачата ни е да извадим Х бр. топки,
които ще бъдат въведени от конзолата, като се има в предвид, че всеки различен цвят влияе на точките ни по следния начин:
•	Ако топката е “red” точките ни се повишават с 5.
•	Ако топката е “orange” точките ни се повишават с 10.
•	Ако топката е “yellow” точките ни се повишават с 15.
•	Ако топката е “white” точките ни се повишават с 20.
•	Ако топката е “black” точките ни се делят на 2.
Ако топката е с какъвто и да е цвят, различен от по-горните, точките не се манипулират и програмата продължава да работи.

Вход:
1.	От конзолата се чете 1 цяло число N, което е броят на топките в диапазон (0-1000).
2.	След това се четат N на брой цветове.

Изход:
Отпечатват се следните редове:
“Total points: {всичките събрани точки}”
“Points from red balls {броят червени топки}”
“Points from orange balls {броят оранжеви топки}”
“Points from yellow balls {броят жълти топки}”
“Points from white balls {броят бели топки}”
“Other colors picked: {броят на избраните топки извън зададените цветове}”
“Divides from black balls: {броят на пътите, в които точките са били разделяни на 2}”

'''

number_colour_balls = int(input())
total_points = 0 #int()
red_points = 0
orange_points = 0
yellow_points = 0
white_points = 0
other_colours = 0
divides_black = 0
#ball_colour = ''


for i in range(number_colour_balls):
    ball_colour = input()
    if ball_colour == 'red':
        total_points += 5
        red_points += 1

    elif ball_colour == 'orange':
        total_points += 10
        orange_points += 1

    elif ball_colour == 'yellow':
        total_points += 15
        yellow_points += 1

    elif ball_colour == 'white':
        total_points += 20
        white_points += 1

    elif ball_colour == 'black':
        total_points = total_points / 2
        divides_black += 1

    else:
        other_colours +=1
        pass


print(f"Total points: {int(total_points)}")
print(f"Points from red balls: {red_points}")
print(f"Points from orange balls: {orange_points}")
print(f"Points from yellow balls: {yellow_points}")
print(f"Points from white balls: {white_points}")
print(f"Other colors picked: {other_colours}")
print(f"Divides from black balls: {divides_black}")