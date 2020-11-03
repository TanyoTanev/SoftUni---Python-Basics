#Water Overflow

#You have a water tank with capacity of 255 liters. On the next n lines, you will receive liters of water, which you have
# to pour in your tank. If the capacity is not enough, print "Insufficient capacity!" and continue reading the next line.
# On the last line, print the liters in the tank.

#In The input will be on two lines:
#On the first line, you will receive n – the number of lines, which will follow
#On the next n lines – you receive quantities of water, which you have to pour in the tank

n = int(input())

limit =255
V=0

for i in range(n):
    add_litres=int(input())

    if add_litres > (limit - V):
         print(f"Insufficient capacity!")
    else:
         V=V+add_litres

print(V)