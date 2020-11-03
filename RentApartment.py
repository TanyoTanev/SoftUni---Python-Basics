'''
Широчина на свободното пространство - цяло число;
Дължина на свободното пространство - цяло число;
Височина на свободното пространство - цяло число;
На следващите редове (до получаване на команда "Done") - брой кашони, които се пренасят в квартирата - цели числа
Програмата трябва да приключи прочитането на данни при команда "Done" или ако свободното място свърши.
'''

width = int(input())
lenght = int(input())
height = int(input())


V = width * lenght* height
full_apartment=0

#packeges_count = int(input())
packeges_inserted = 0
#is_done = (input())
# (is_done!="Done")

while packeges_inserted <= V and (packeges_inserted !="Done"):

    packeges_count = input()

    if packeges_count == "Done":

        break
    else:
         if packeges_inserted + int(packeges_count) <=V:
            packeges_inserted = packeges_inserted + int(packeges_count)
         else:
            print(f" No more free space! You need {packeges_inserted + int(packeges_count) - V} Cubic meters more.")
            full_apartment=1
            break




if full_apartment < 1:
    print(f"{V - packeges_inserted} Cubic meters left.")