days = int(input())
room_type = input()
opinion = input()
total_cost = 0

if room_type =="room for one person" :
    total_cost = (days-1) *18
elif room_type =="apartment" :
     if days < 10 :
         total_cost = (days - 1) *25*0.7
     elif  days >= 10 and days <=15 :
         total_cost = (days - 1) * 25 * 0.65
     elif days  > 15:
         total_cost = (days - 1) * 25 * 0.5
elif room_type =="president apartment" :
    if days < 10:
        total_cost = (days - 1) * 35 * 0.9
    elif days >= 10 and days <= 15:
        total_cost = (days - 1) * 35 * 0.85
    elif days > 15:
        total_cost = (days - 1) * 35 * 0.8


if opinion == "positive" :
    total_cost = total_cost *1.25
elif opinion == "negative" :
    total_cost = total_cost * 0.9

print(f"{total_cost:.2f}")