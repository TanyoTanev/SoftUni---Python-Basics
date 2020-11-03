#Triples of Latin Letters

#Write a program to read an integer n and print all triples of the first n small Latin letters, ordered alphabetically:

n = int(input())

for i in range(97,97+n,1):
    for j in range(97,97+n,1):
        for k in range(97,97+n,1):
            print(chr(i)+chr(j)+chr(k))

