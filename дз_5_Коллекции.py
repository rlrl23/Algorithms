#1 Вывести предприятия, чья прибыль выше среднего:
import collections
from itertools import zip_longest
#1
def avg_profit(n):
    profits=[]
    total_profit=0
    company= collections.namedtuple('Company', ['name', 'avg_p'])
    result=[['Прибыль выше среднего у '], ['Прибыль ниже среднего у ']]
    for i in range(0, n):
        name, q1, q2, q3, q4= input('Название предприятия, прибыль за 4 квартала ').split()
        profits.append(company(name=name, avg_p=(float(q1)+float(q2)+float(q3)+float(q4))/4))
        total_profit+=(float(q1)+float(q2)+float(q3)+float(q4))/4
    total_profit/=n
    print(profits, 'Средняя прибыль за год ', total_profit)
    for company in profits:
        if company.avg_p>total_profit:
            result[0].append(company.name)
        else:
            result[1].append(company.name)
    print(result)

avg_profit(3)

#1
class Profits():
    def __init__(self, *args):
        self.args= args
        summa=0
        for arg in self.args:
            summa+= arg.avg_profit
        self.total_profit= summa/len(self.args)

    def less(self):
        result='Прибыль ниже среднего у '
        for arg in self.args:
            if arg.avg_profit< self.total_profit:
                result+= arg.name
                result +=' '
        return result
    def more(self):
        result='Прибыль выше среднего у '
        for arg in self.args:
            if arg.avg_profit> self.total_profit:
                result += arg.name
                result += ' '
        return result

class Company(Profits):
    def __init__(self, name, q1, q2, q3, q4):
        self.q1 = q1
        self.q2 = q2
        self.q3 = q3
        self.q4 = q4
        self.name = name
        self.avg_profit = (self.q1 + self.q2 + self.q3 + self.q4) / 4

a= Company('УралМаш', 123, 89, 56, 0)
b= Company('Синара', 100, 23, 51, 23)
c= Company('Сибади', 62, 52, 41, 60)

abc=Profits(a, b, c)
print(abc.total_profit)
print(abc.less())
print(abc.more())

#2 сложениe и умножениe двух шестнадцатеричных чисел
def add(a, b):
    one=0
    result=collections.deque()
    table = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F']
    for num_a, num_b in zip_longest(a[::-1], b[::-1], fillvalue=0):
        sum = table.index(num_a) + table.index(num_b)+one
        one = sum // 16
        result.appendleft(table[sum % 16])
    print('Sum= ', result)


a= ['A', 2]
b=['C', 4, 'F']
add(a,b)

def mul(a, b):
    result = collections.deque()
    table = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F']
    total_result = []
    i=1
    for num_a in a[::-1]:
        one = 0
        for num_b in b[::-1]:
            mul = table.index(num_a) * table.index(num_b) + one
            one = mul // 16
            result.appendleft(table[mul % 16])
        if one!=0:
            result.appendleft(one)
        total_result.append(list(result))
        result.clear()
        print(total_result)
        if len(total_result)==2:
            c = total_result[0]
            d = total_result[1]
            for k in range(0,i):
                d.append(0)
            one = 0
            for num_a, num_b in zip_longest(c[::-1], d[::-1], fillvalue=0):
                sum = table.index(num_a) + table.index(num_b) + one
                one = sum // 16
                result.appendleft(table[sum % 16])
            total_result.clear()
            total_result.append(list(result))
            result.clear()
            print(total_result)
            i+=1
    print('Произведение:', total_result)

b=[1,'F',4]
a=[2, 'F', 5, 1, 'E']
mul(a,b)


