#Write a program that receives a single string containing numbers separated by a single space. Print a list containing the opposite of each number

str= input()

list=[]

for i in str.split():
    num=int(i)
    list.append(-num)

print(list)