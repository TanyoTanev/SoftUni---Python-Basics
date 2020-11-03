'''
Сумиране на секунди

Трима спортни състезатели финишират за някакъв брой секунди (между 1 и 50). Да се напише програма, която чете времената на
състезателите в секунди, въведени от потребителя и пресмята сумарното им време във формат "минути:секунди". Секундите да се изведат с
водеща нула (2  "02", 7  "07", 35  "35").

вход

изход

22
7
34
1:03

50
50
49

2:29

14
12
10
'''

first_runner = int(input())
second_runner = int(input())
third_runner = int(input())

total_time = first_runner + second_runner + third_runner
minutes = total_time // 60

seconds = total_time % 60

#print(minutes)
#print(seconds)

if seconds > 9 :
    print(f"{minutes}:{seconds}")
else:
    print(f"{minutes}:0{seconds}")