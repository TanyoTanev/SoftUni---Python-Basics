

area = float (input())

cost = area *7.61
final_cost = cost * 0.82

print (f" стойността на озеленяването е {cost : .2f} "
       f" крайната сума с отстъпката е {final_cost : .2f}"
       f"а отстъпката е {cost - final_cost: .2f}")