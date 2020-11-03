'''*Snowballs

Tony and Andi love playing in the snow and having snowball fights, but they always argue which makes the best snowballs.
They have decided to involve you in their fray, by making you write a program, which calculates snowball data, and outputs the best snowball value.

You will receive N – an integer, the number of snowballs being made by Tony and Andi.
For each snowball you will receive 3 input lines:
On the first line you will get the snowballSnow – an integer.
On the second line you will get the snowballTime – an integer.
On the third line you will get the snowballQuality – an integer.
For each snowball you must calculate its snowballValue by the following formula:
(snowballSnow / snowballTime) ^ snowballQuality
At the end you must print the highest calculated snowballValue.

Input

On the first input line you will receive N – the number of snowballs.
On the next N * 3 input lines you will be receiving data about snowballs.'''
#import math

n = int(input())
snowballValueMax = 0
snowballSnowMax = snowballSnowMax = snowballTimeMax = snowballQualityMax =0

for i in range(n):

    snowballSnow = int(input())
    snowballTime = int(input())
    snowballQuality = int(input())


    snowballValue= (snowballSnow / snowballTime) ** snowballQuality
    if snowballValue > snowballValueMax:
        snowballValueMax = snowballValue
        snowballSnowMax = snowballSnow
        snowballTimeMax = snowballTime
        snowballQualityMax = snowballQuality


print(f"{snowballSnowMax} : {snowballTimeMax} = {int(snowballValueMax)} ({snowballQualityMax})")