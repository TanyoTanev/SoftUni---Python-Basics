'''
Задача 5. Най-добър играч
Пепи иска да напишете програма, чрез която да разбере кой е най-добрият играч от световното първенство. Информацията, която получавате
ще бъде играч и колко гола е отбелязал. От вас се иска да отпечатате кой е играчът с най-много голове и дали е направил хет-трик.
Хет-трик е, когато футболистът е вкарал 3 или повече гола. Ако футболистът е вкарал 10 или повече гола, програмата трябва да спре.
Вход:
От конзолата се четат по два реда до въвеждане на команда "END":
•	Име на играч – текст
•	Брой вкарани голове  – цяло положително число в интервала [1 … 10000]
Изход:
На конзолата да се отпечатат 2 реда :
•	На първия ред:
            "{име на играч} is the best player!"
•	На втория ред :
o	 Ако най-добрият футболист е направил хеттрик:
                   "{име на играч} has scored {брой голове} goals and made a hat-trick !!!"
o	Ако най-добрият футболист не е направил хеттрик:
 "{име на играч} has scored {брой голове} goals."
'''

#command = ''
most_goals = 0
#best_player = ''
#current_goals = 0

while True:
    command = input()
    if command == 'END':
        break

    current_goals = int(input())


    if current_goals > most_goals:
        most_goals = current_goals
        best_player = command

    if current_goals >= 10:
       break


print(f"{best_player} is the best player!")
if most_goals >= 3:
    print(f"He has scored {most_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {most_goals} goals.")