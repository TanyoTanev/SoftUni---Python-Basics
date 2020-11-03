'''
Пари, нужни за екскурзията - реално число;
	Налични пари - реално число.
	След това многократно се четат по два реда:
	Вид действие – текст с две възможности: "spend" или "save";
		Сумата, която ще спести/похарчи - реално число.

'''
holiday_cost = int(input())
current_money = int(input())

is_spending=0
days_gone=0

while current_money < holiday_cost :
    action = input()
    daily_money = int(input())
    days_gone+=1

    if action =="save":
        current_money = current_money + daily_money
        is_spending=0
    elif action =="spend":
        current_money = current_money - daily_money
        if current_money < 0:
            current_money =0
        is_spending = is_spending+1
        if is_spending==5:
            print(f"You can't save the money. {days_gone}")
            break


if (current_money >= holiday_cost ) :
    print(f"You saved the money for {days_gone} days.")