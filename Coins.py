#Производителите на вендинг машини искали да направят машините си да връщат възможно най-малко монети ресто.
#Напишете програма, която приема сума - рестото, което трябва да се върне и изчислява
#с колко най-малко монети може да стане това.


change = float (input())
first_change = change

number_coins =0
number_2_leva  =0
number_1_leva =0
number_50_stotinki =0
number_20_stotinki =0
number_10_stotinki =0
number_05_stotinki =0
number_02_stotinki =0
number_01_stotinki =0

while change > 0:
    if change >= 2:
        number_2_leva = int(change/2)
        change  =  round(change - number_2_leva*2,2 )       # (change % 2)
    elif change >= 1:
        number_1_leva+=1
        change = change -1
    elif change >=0.5:
        number_50_stotinki += 1
        change = change - 0.5
    elif change >= 0.2:
        number_20_stotinki =  int(change / 0.2)
        change = round(change -  number_20_stotinki* 0.2, 2)
    elif change >= 0.1:
        number_10_stotinki = int(change / 0.1)
        change = round(change - number_10_stotinki * 0.1, 2)
    elif change >= 0.05:
        number_05_stotinki += 1
        change = round(change - 0.05,2)
    elif change >= 0.02:
        number_02_stotinki =  int(change / 0.02)
        change = round(change - number_02_stotinki * 0.02, 2)
    elif change >= 0.01:
        number_01_stotinki =  int(change/0.01)
        change=0
        #break

number_coins=number_2_leva+number_1_leva+number_50_stotinki+number_20_stotinki+number_10_stotinki+number_05_stotinki+number_02_stotinki+number_01_stotinki
print (number_coins)
print(f"Рестото ни е {first_change} лева. Машината ни го връща с {number_2_leva} монети от 2 лева, {number_1_leva} монети от 1 лева, {number_50_stotinki} монети от 50 стотинки, {number_20_stotinki} монети от 20 стотинки, {number_10_stotinki} монети от 10 стотинки,{number_05_stotinki} монети от 5 стотинки, {number_02_stotinki} монети от 2 стотинки, {number_01_stotinki} монети от 1 стотинки ")