'''
Старата библиотека

Ани отива до родния си град след много дълъг период извън страната. Прибирайки се вкъщи, тя вижда старата библиотека на баба си и
си спомня за любимата си книга. Помогнете на Ани, като напишете програма, в която тя въвежда търсената от нея книга (текст).
Докато Ани не намери любимата си книга или не провери всички в библиотеката, програмата трябва да чете всеки път на нов ред името
на всяка следваща книга (текст). Книгите в библиотеката са свършили щом получите текст “No More Books”.Ако не открие търсената книгата,
да се отпечата на два реда:

"The book you search is not here!"
"You checked {брой} books."

Ако открие книгата си, да се отпечата на един ред:
"You checked {брой} books and found it."

Примерен вход и изход

Вход
Изход

Troy
Stronger
Life Style
Troy

The Spot
Hunger Games
Harry Potter
Torronto
Spotify
No More Books

'''

book_to_find = input()
stop_command = 'No More Books'
command = ''
number_checked_books = 0

while True:
    command = input()
    if command == stop_command:
        print(f"The book you search is not here!")
        print(f"You checked {number_checked_books} books.")
        break

    elif command == book_to_find:
        #number_checked_books +=1
        print(f"You checked {number_checked_books} books and found it.")
        break
    else:
        number_checked_books += 1