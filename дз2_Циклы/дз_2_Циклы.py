#1 Калькулятор
def calc():
    while 1:
        num1 = int(input('Введите число '))
        num2 = int(input('Введите число '))
        sign = input('Введите знак операции, или 0 для завершения ')
        if sign == '0':
            break
        elif sign =='+':
            print(num1+ num2)
        elif sign=='-':
            print(num1-num2)
        elif sign=='*':
            print(num1 * num2)
        elif sign=='/':
            if num2!=0:
                print(num1 / num2)
            else:
                print('Нельзя делить на 0')
        else:
            print('Неверно выбран знак. Попробуйте снова')

#2 Посчитать четные и нечетные цифры введенного натурального числа
def count(num):
    num=str(num)
    i=0
    even=0
    odd=0
    while i<len(num):
        if int(num[i]) % 2:
            odd+=1
            i+=1
        else:
            even+=1
            i+=1
    print('Четных - ', even, 'Нечетных - ', odd)

#3 Сформировать из введенного числа обратное по порядку входящих в него цифр
def reverse(num):
    num=str(num)
    print(num[::-1])

#4 Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
def sum_seq(n):
    i=1
    sum=1
    while n-1>0:
        i*=-0.5
        sum+=i
        n-=1
    print(sum)

#sum_seq(4)

#5 Вывести по 10 кодов и символов в строке
def cods():
    line = ''
    n = 0
    for i in range(32, 128):
        line += f'{i} {chr(i)} '
        n+=1
        if n==10:
            print(line)
            line = ''
            n=0
    print(line)

#6 Угадай число, 10 попыток
import random

def guess_num():
    num = random.randint(0, 100)
    try_count=10
    while 1:
        user_num= int(input('Угадай число от 0 до 100 '))
        try_count-=1
        if try_count == 0:
            print('Попытки закончились, вы проиграли')
            break
        elif user_num>num:
            print('Ваше число больше')
        elif user_num<num:
            print('Ваше число меньше')
        else:
            print('Поздравляю, вы угадали!')
            break

guess_num()

#7 Доказать равенство 1+2+...+n = n(n+1)/2
def check_equip(n):
    n_sum=0
    for i in range(1, n+1):
        n_sum+=i
    if n*(n+1)/2==n_sum:
        print('Равенство 1+2+...+n = n(n+1)/2 верно!')
    else:
        print('Равенство 1+2+...+n = n(n+1)/2 НЕ верно!')

#check_equip(567)

#8 Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел
def count_num(num_list, num):
    num_list=str(num_list)
    print(num_list.count(str(num)))

#count_num(12121212, 1)

#9 Найти наибольшее по сумме цифр

def max_sum_num(*nums):
    dict_sum_num = {}
    for num in nums:
        sum_num=0
        for one_num in str(num):
            sum_num+=int(one_num)
        dict_sum_num[sum_num]=num
    max_sum=max(dict_sum_num)
    print('Наибольшая сумма цифр', max_sum, 'у числа', dict_sum_num[max_sum])


#max_sum_num(523, 634, 456)