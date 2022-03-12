#1  В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
def multiple():
    nums=[2,3,4,5,6,7,8,9]
    result={}
    for num in nums:
        n = 0
        for i in range(2, 100):
            if i%num==0:
                n+=1
                result[num]=n
    print(result)

#multiple()

#2
def indexes(*nums):
    result=[]
    n=0
    for num in nums:
        n+=1
        if num%2==0:
            result.append(n)
    print(result)

#indexes(8,3,15,6,4,2)

#3
import random
def rev_min_max(n):
    rand_list= []
    for i in range(0,n):
        rand_list.append(random.randint(1,100))
    result=[]
    for num in rand_list:
        if num==max(rand_list):
            result.append(min(rand_list))
        elif num==min(rand_list):
            result.append(max(rand_list))
        else:
            result.append(num)
    print(rand_list, max(rand_list), min(rand_list), result)

#rev_min_max(5)

#4
def frequent():
    rand_list = []
    max_frequent=0
    for i in range(0, 15):
        rand_list.append(random.randint(1, 5))
    print(rand_list)
    for num in set(rand_list):
        if rand_list.count(num)>=max_frequent:
            max_frequent= rand_list.count(num)
            max_frequent_num = num
    print('Чаще всего встречается число: ', max_frequent_num)

#frequent()

#5
def max_minus(from_num, to_num, count):
    rand_list = []
    for i in range(0, count):
        rand_list.append(random.randint(from_num, to_num))
    print(rand_list)
    max_num= from_num
    for num in rand_list:
        if num<0:
            if num> max_num:
                max_num=num
    print('Min count - ', max_num, 'Position ', rand_list.index(max_num)+1)

max_minus(-100, 10, 10)

#6
def between_min_max():
    rand_list = []
    sum_num = 0
    for i in range(0, 10):
        rand_list.append(random.randint(1, 100))
    print(rand_list)
    from_num= rand_list.index(min(rand_list))
    to_num= rand_list.index(max(rand_list))
    if from_num<to_num:
        for i in range(from_num+1, to_num):
            sum_num+= rand_list[i]
    else:
        for i in range(to_num+1, from_num):
            sum_num+= rand_list[i]
    print(sum_num)

#between_min_max()

#7
def two_min(n):
    rand_list = []
    for i in range(0, 10):
        rand_list.append(random.randint(1, n))
    print(rand_list)
    min_num = n
    if rand_list.count(min(rand_list))>1:
        print(min(rand_list), min(rand_list))
    else:
        for num in set(rand_list):
            if num> min(rand_list) and num<min_num:
                min_num=num
        print(min(rand_list), min_num)

#two_min(10)

#8
def matrix():
    matrix=[]
    for i in range(0, 5):
        sum=0
        line= list(input('Введите элементы строки матрицы через пробел ').split())
        for num in line:
            sum+=int(num)
        line.append(sum)
        matrix.append(line)
    print(matrix)

#matrix()

#9
def min_el_matrix(size):
    matrix = []
    i=0
    while i< size:
        line = list(input(f'Введите {size} элемента строки матрицы слитно '))
        if len(line)!=size:
            print('Введено неверное количество элементов, попробуй еще раз')
        else:
            matrix.append(line)
            i+=1
    min_nums=[]
    max_nums=[]
    for column in range(0, size):
        for row in range(0, size):
            min_nums.append(int(matrix[row][column]))
        max_nums.append(min(min_nums))
        min_nums.clear()
    print('Максимальный элемент среди минимальных элементов столбцов матрицы ', max(max_nums))

#min_el_matrix(3)