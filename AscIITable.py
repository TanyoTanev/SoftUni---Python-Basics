#Print Part of the ASCII Table

#Find online more information about ASCII (American Standard Code for Information Interchange) and write a program that
# prints part of the ASCII table of characters on the console.  On the first line of input you will receive the char
# index you should start with and on the second line - the index of the last character you should print.

beggining = int(input())
end = int(input())

for i in range(beggining,end+1,1 ):
    print(chr(i),end=' ')

