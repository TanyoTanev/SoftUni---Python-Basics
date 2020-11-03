'''
*Стипендии
Учениците могат да кандидатстват за социална стипендия или за стипендия за отличен успех. Изискване за социална стипендия -
доход на член от семейството по-малък от минималната работна заплата и успех над 4.5. Размер на социалната стипендия -
35% от минималната работна заплата. Изискване за стипендия за отличен успех - успех над 5.5, включително.
Размер на стипендията за отличен успех - успехът на ученика, умножен по коефициент 25.

Напишете програма, която при въведени доход, успех и минимална работна заплата, дава информация дали ученик има право да получава стипендия,
и стойността на стипендията, която е по-висока за него.

Вход
Потребителят въвежда 3 числа, по едно на ред:
Доход в лева - реално число;
Среден успех -  реално числсо;
Минимална работна заплата – реално число.

Изход
Ако ученикът няма право да получава стипендия, се извежда:
"You cannot get a scholarship!"
Ако ученикът има право да получава само социална стипендия:
"You get a Social scholarship {стойност на стипендия} BGN"
Ако ученикът има право да получава само стипендия за отличен успех:
"You get a scholarship for excellent results {стойност на стипендията} BGN"
Ако ученикът има право да получава и двата типа стипендии, ще получи по-голямата по сума, а ако са равни ще получи тази за отличен успех.

	Резултатът се закръгля до по-малкото цяло число.

	480.00
4.60
450.00

300.00
5.65
420.00

'''

income = float(input())
average_grade = float(input())
min_wage = float(input())

if (income >= min_wage and average_grade < 5.5 ) or (income < min_wage and average_grade <= 4.5):
    print("You cannot get a scholarship!")

elif income < min_wage and average_grade > 4.5 and average_grade < 5.5 :
    #social_results = int(0.35 * min_wage)
    print(f"You get a Social scholarship {int(0.35 * min_wage)} BGN")

elif income >= min_wage and average_grade >= 5.5 :
    print(f"You get a scholarship for excellent results { int(average_grade * 25)} BGN")

elif (income < min_wage and average_grade >= 5.5 ):
    exellent_results = average_grade * 25
    social_results = 0.35 * min_wage
    if exellent_results  < social_results :
        print(f"You get a Social scholarship {int(social_results)} BGN")
    else:
        print(f"You get a scholarship for excellent results { int(exellent_results)} BGN")