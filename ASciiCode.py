#Write a program, which sums the ASCII codes of n characters and prints the sum on the console.

n = int(input())
sumator=0

for i in range(n,0,-1):
    char = input()
    sumator=sumator + ord(char)
    #print(i)

print(f"The sum equals: {sumator}")