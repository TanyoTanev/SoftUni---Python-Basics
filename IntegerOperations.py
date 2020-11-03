#Add first to the second, divide (integer) the sum by the third number and
#multiply the result by the fourth number. Print the result.

'''first = int(input())
second = int(input())
third = int(input())
forth = int(input())

first = first + second
first = first // third
first = first * forth

print(first)'''

n = int(input())
p = int(input())

courses_full = n//p
courses_rest = n%p

if courses_full> 0 and courses_rest>0:
    print(courses_full+1)
    #print(f" {courses_full} courses * 3 people\n+ {courses_rest} course * {n%p} persons")
elif courses_full> 0 and courses_rest==0:
     print(courses_full)
else:
    print(1)
    #print(f"All the persons fit inside in the elevator.\nOnly one course is needed.")
