holiday_cost = float (input())

count_pazeli = int(input()) # 2.60
count_doll = int(input()) #3
count_teddy_bear = int(input()) # 4.1
count_minions = int(input()) # 8.2
count_truck = int(input()) #2

price_pazeli =  2.60
price_doll = 3.0
price_teddy_bear = 4.1
price_minions =  8.2
price_truck = 2.0




total_income = (count_pazeli * price_pazeli) + (count_doll*price_doll) + (count_teddy_bear*price_teddy_bear) + (count_minions*price_minions) + (count_truck*price_truck)
if (count_pazeli + count_doll + count_teddy_bear + count_minions + count_truck) > 50:
    total_income =total_income *0.75

if total_income*0.9 >=holiday_cost :

    print(f" Yes, remaining money left {total_income*0.9 - holiday_cost : .2f} ")

else :
    print(f" Not enough money! {-(total_income * 0.9 - holiday_cost) : .2f}  needed.")