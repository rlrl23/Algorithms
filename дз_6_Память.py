# Python версия 3.9, Win 64bit. Задание:
# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4
# квартала (т.е. 4 отдельных числа) для каждого предприятия.. Программа должна определить
# среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий, чья
# прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже
# среднего

#1.1 Реализован при помощи списка коллекций - размер, расходуемой памяти (128) в 2 раза меньше чем в 1.2 - реализованной через словарь(272).
#В 1.3 для переменной result применена конкатенация строк с использованием знака '+', что нежелательно с точки зрения экономии места
# и времени т.к. когда мы добавляем новую строку к существующей строке, Python создает новую строку и присваивает ее новому адресу(перераспределяет)

import collections

#1.1 Namedtuple
def avg_profit(n):
    profits=[]
    total_profit=0
    company= collections.namedtuple('Company', ['name', 'avg_p'])
    result=[['Прибыль выше среднего у '], ['Прибыль ниже среднего у ']]
    for i in range(0, n):
        name, q1, q2, q3, q4= input('Название предприятия, прибыль за 4 квартала ').split(',')
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
    print(profits.__sizeof__() + result.__sizeof__())

avg_profit(3)

#1.2 Словарь
def dict_avg_profit(n):
    profits= {}
    total_profit=0
    result=[['Прибыль выше среднего у '], ['Прибыль ниже среднего у ']]
    for i in range(0, n):
        name, q1, q2, q3, q4= input('Название предприятия, прибыль за 4 квартала ').split(',')
        profits[name]=(float(q1)+float(q2)+float(q3)+float(q4))/4
        total_profit+=(float(q1)+float(q2)+float(q3)+float(q4))/4
    total_profit/=n
    print(profits, 'Средняя прибыль за год ', total_profit)
    for key, val in profits.items():
        if val>total_profit:
            result[0].append(key)
        else:
            result[1].append(key)
    print(result)
    print(profits.__sizeof__()+result.__sizeof__())
dict_avg_profit(3)

#1.3 OOП
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
        return result, result.__sizeof__()

    def more(self):
        result='Прибыль выше среднего у '
        for arg in self.args:
            if arg.avg_profit> self.total_profit:
                result += arg.name
                result += ' '
        return result, result.__sizeof__()

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
print(abc.less())
print(abc.more())




