import timeit
#2 нахождение i-го по счёту простого числа
start_time=timeit.default_timer()
def arutosfen(n):
    a=[0]*n**2
    for i in range(n**2):
        a[i]=i
    a[1]=0
    m=2
    while m<n**2:
        if a[m]!=0:
            j=m*2
            while j<n**2:
                a[j]=0
                j=j+m
        m+=1
    b=[]
    for i in a:
        if a[i] !=0:
            b.append(a[i])
    del(a)
    print(b[n])

arutosfen(100)
print(timeit.default_timer()-start_time)
start_time=timeit.default_timer()

def simple_nums(n):
    result = [2, 3, 5, 7, 11]
    if n<=5:
        print(result[n])
    else:
        for i in range(13, n**2, 2):
            count=0
            for simple_num in range(1, len(result)):
                if i% result[simple_num] ==0:
                    i+=2
                else:
                    count+=1
                if count==len(result)-1:
                    result.append(i)
                    if len(result)==n+1:
                        print(result[n])
                        break

simple_nums(100)
print(timeit.default_timer()-start_time)
# Алгоритм Эратосфена - быстрее, мой - задействует меньше памяти

#1 Найти наибольшее по сумме цифр
start_time=timeit.default_timer()
def max_sum_num(*nums):
    dict_sum_num = {}
    for num in nums:
        sum_num=0
        for one_num in str(num):
            sum_num+=int(one_num)
        dict_sum_num[sum_num]=num
    max_sum=max(dict_sum_num)
    print('Наибольшая сумма цифр', max_sum, 'у числа', dict_sum_num[max_sum])

max_sum_num(78915, 96526, 86578, 1239632, 456258, 78924, 115653, 125458, 178991, 196198, 157635, 9996321, 96512, 946, 987, 962)
print(timeit.default_timer() - start_time)

start_time=timeit.default_timer()
def optimax_sum_num(*nums):
    max_sum=0
    max_num=0
    for num in nums:
        sum_num=0
        for one_num in str(num):
            sum_num+=int(one_num)
        if sum_num>max_sum:
            max_sum=sum_num
            max_num=num
    print('Наибольшая сумма цифр', max_sum, 'у числа', max_num)

optimax_sum_num(78915, 96526, 86578, 1239632, 456258, 78924, 115653, 125458, 178991, 196198, 157635, 9996321, 96512, 946, 987, 962)
print(timeit.default_timer() - start_time)

#Оптимизирован по скорости, за счет того, что макс значение сохраняется сразу, и по памяти, т.к. храним только 2 значения.
#Сложность из квадратной стала линейной