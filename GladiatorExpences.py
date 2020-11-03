'''*Gladiator Expenses

Input / Constraints

You will receive 5 parameters to your function:
First parameter – lost fights count – integer in the range [0, 1000].
Second parameter – helmet price - floating point number in range [0, 1000].
Third parameter – sword price - floating point number in range [0, 1000].
Fourth parameter – shield price - floating point number in range [0, 1000].
Fifth parameter – armor price - floating point number in range [0, 1000].

Every second lost game, his helmet is broken.
Every third lost game, his sword is broken.
When both his sword and helmet are broken in the same lost fight, his shield also brakes.
Every second time, when his shield brakes, his armor also needs to be repaired.

'''
lost_fights = int(input())
helmet_price = float (input())
sword_price = float (input())
shield_price = float (input())
armor_price = float (input())

expenses = 0

for i in range(1,lost_fights+1):

    if i % 2 == 0:
        expenses = expenses + helmet_price

    if i % 3 == 0:
        expenses = expenses + sword_price

    if (i % 3 == 0) and (i % 2 == 0):
        expenses = expenses + shield_price

    if i % 12 == 0 and i > 0:
        expenses = expenses + armor_price


print(f"Gladiator expenses: {expenses:.2f} aureus")