'''
Информация за скоростта

Да се напише програма, която чете скорост (реално число), въведена от потребителя и отпечатва информация за скоростта. При скорост до
10 (включително) отпечатайте “slow”. При скорост над 10 и до 50 отпечатайте “average”. При скорост над 50 и до 150 отпечатайте “fast”.
При скорост над 150 и до 1000 отпечатайте “ultra fast”. При по-висока скорост отпечатайте “extremely fast”. Примери:

вход

изход

'''

speed = float(input())

if speed <= 10:
    print(f"slow")
elif speed > 10 and speed <= 50:
    print(f"average")
elif speed > 50 and speed <= 150:
    print(f"fast")
elif speed > 150 and speed <=1000:
    print(f"ultra fast")
else:
    print(f"extremely fast")
