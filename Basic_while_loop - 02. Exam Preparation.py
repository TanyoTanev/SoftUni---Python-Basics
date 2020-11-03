'''
Подготовка за изпит

Напишете програма, в която Марин решава задачи от изпити, докато не получи съобщение "Enough" от лектора си.
При всяка решена задача той получава оценка. Програмата трябва да приключи прочитането на данни при команда "Enough" или ако Марин получи
определения брой незадоволителни оценки. Незадоволителна е всяка оценка, която е по-малка или равна на 4.

Вход
На първи ред - брой незадоволителни оценки - цяло число;
След това многократно се четат по два реда:
Име на задача – текст;
Оценка - цяло число в интервала [2…6].

Изход
Ако Марин стигне до командата "Enough", отпечатайте на 3 реда:
"Average score: {средна оценка}"
"Number of problems: {броя на всички задачи}"
"Last problem: {името на последната задача}"
Ако получи определеният брой незадоволителни оценки:

	"You need a break, {брой незадоволителни оценки} poor grades."

Средната оценка да бъде форматирана до втория знак след десетичната запетая.
Примерен вход и изход

Вход
Изход

3
Money
6
Story
4
Spring Time
5
Bus
6
Enough

2
Income
3
Game Info
6
Best Player
4


'''

stop_command = 'Enough'
low_grades_max = int(input())
low_grades = 0
command = ''
name_last_task = ''
grades_list = []
#print(low_grades_max)

while True:
    command = input()

    if command == stop_command:
        if len(grades_list):
         print(f"Average score: {sum(grades_list)/len(grades_list):.2f}")
        else:
            print(f"Average score: {0:.2f}")
        print(f"Number of problems: {len(grades_list)}")
        print(f"Last problem: {name_last_task}")
        break
    else:
        name_last_task = command
    grade = int(input())
    if grade <= 4:
        low_grades +=1
    if low_grades >= low_grades_max:
        print(f"You need a break, {low_grades} poor grades.")
        #grades_list.append(grade)
        break
    grades_list.append(grade)