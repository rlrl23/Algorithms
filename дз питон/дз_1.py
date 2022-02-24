#1 Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
def sum_comp_num(num):
    if len(num)==3:
        sum_num= int(num[0])+ int(num[1])+int(num[2])
        comp_num= int(num[0])*int(num[1])*int(num[2])
        print('Сумма цифр ', sum_num, ', Произведение цифр ', comp_num)
    else:
        print('Вы ввели некорректное значение. Попробуйте ещё раз')

sum_comp_num(input('Введите 3х-значное число '))

#2 Выполнить логические побитовые операции "И", "ИЛИ" и др. над числами 5 и 6. Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.

def bit_operations():
    print('Логическое И =', 5 & 6)
    print('Логическое ИЛИ =', 5 | 6)
    print('побитовый сдвиг вправо', 5 << 2)
    print('побитовый сдвиг влево', 5 >> 2)

bit_operations()

#3 По введенным пользователем координатам 2 (.) вывести уравнение прямой вида
def line_equation():
    x1 = int(input('Введите координаты х1 '))
    y1 = int(input('Введите координаты y1 '))
    x2 = int(input('Введите координаты х2 '))
    y2 = int(input('Введите координаты y2 '))
    k=(y2-y1)/(x2-x1)
    b= y1-((y2-y1)/(x2-x1))*x1
    print(f'y= {k}x {b:+}')

line_equation()

#4 генерирует в указанных пользователем границах: случайное целое число, случайное вещественное число, случайный символ.
import random
def random_nums(start, stop, num_type):
    if num_type == 'int':
        print(random.randint(start, stop))
    elif num_type == 'float':
        print(random.uniform(start, stop))
    else:
        print(chr(random.randint(ord(start), ord(stop))))

random_nums(5, 10, 'int')
random_nums(5, 10, 'float')
random_nums('x', 'z', 'letter')

#5 Определить, на каких местах алфавита стоят буквы, и сколько между ними находится букв.
def letter_place(letter1, letter2):
    print(f'место буквы "{letter1}" - {ord(letter1)-96}, '
          f'место буквы "{letter2}"- {ord(letter2)-96}, '
        f'между ними букв - {abs(ord(letter2)-ord(letter1))-1}')

letter_place('w', 'z')

#6 Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
def letter_by_num(letter_num):
    print(f'буквa - {chr(letter_num+96)}')

letter_by_num(26)

#7 Треугольник по сторонам - да? какой?
def triangle(a, b, c):
    if a>= b+c or b>= a+c or c>= a+b:
        print('Треугольник не существует')
    else:
        if a==b==c:
            print('Треугольник равносторонний')
        elif a==b or a==c or b==c:
            print('Треугольник равнобедренный')
        else:
            print('Треугольник разносторонний')

triangle(6, 6, 7)

#8 Високосный год
import datetime
def leap_year(year):
    try:
        datetime.date(year, 2, 29)
        print('Год високосный')
    except:
        print('Год НЕ високосный')

leap_year(2020)
leap_year(2021)

#9 Найти среднее из 3х чисел
def median_num(a, b, c):
    print('Cреднее - ', a+b+c -max(a, b, c)- min(a, b, c))

median_num(2,25,24)


