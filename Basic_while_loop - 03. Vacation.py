'''
Почивка

Джеси е решила да събира пари за екскурзия и иска от вас да ѝ помогнете да разбере дали ще успее да събере необходимата сума.
Тя спестява или харчи част от парите си всеки ден. Ако иска да похарчи повече от наличните си пари, то тя ще похарчи колкото има и ще
ѝ останат 0 лева.

Вход

От конзолата се четат:
	Пари, нужни за екскурзията - реално число;
	Налични пари - реално число.
	След това многократно се четат по два реда:
	Вид действие – текст с две възможности: "spend" или "save";
		Сумата, която ще спести/похарчи - реално число.

Изход
Програмата трябва да приключи при следните случаи:
Ако 5 последователни дни Джеси само харчи, на конзолата да се изпише:

		"You can't save the money."
		"{Общ брой изминали дни}"

Ако Джеси събере парите за почивката, на конзолата се изписва:
	"You saved the money for {общ брой изминали дни} days."

Примерен вход и изход
Вход
Изход
Обяснния

2000
1000
spend
1200
save
2000

110
60
spend
10
spend
10
spend
10
spend
10
spend
10



250
150
spend
50
spend
50
save
100
save
100

You saved the money for 2 days.
'''

needed_money = float(input())
saved_money = float(input())
consecutive_days = 0
days = 0
command = ''
amount_money = 0
last_day_spend = 0 # не е харчила , а е спестявала

while True:

    if consecutive_days >= 5:
        print(f"You can't save the money.")
        print(f"{days}")
        break

    elif saved_money >= needed_money:
        print(f"You saved the money for {days} days.")
        break

    else:
        command = input()
        amount_money = float(input())
        days += 1
        if command == 'spend':
            saved_money -= amount_money
            last_day_spend = 1

            if saved_money < 0:
                saved_money = 0
            if last_day_spend == 1:
                consecutive_days += 1

        else:
            saved_money += amount_money
            last_day_spend = 0
            consecutive_days = 0