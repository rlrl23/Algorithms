#Определение количества различных подстрок с использованием хэш-функции
import hashlib
def find_str(s, t):
    count=0
    sub_str=hashlib.sha1(t.encode()).hexdigest()
    for i in range(len(s)-len(t)+1):
        if sub_str==hashlib.sha1(s[i:i+len(t)].encode()).hexdigest():
            count+=1
    print(count)

s= "Закодируйте любую строку из трех слов по алгоритму Хаффмана"
t='по'

#find_str(s,t)

import collections
#2 Закодируйте любую строку из трех слов по алгоритму Хаффмана
s= 'beep boop beer!'
#s= 'свободу милым котикам'
def haffman(s):
    table={}
    for i in s:
        table[i]= s.count(i)

    frequent=sorted(table.values())
    frequent=collections.deque(frequent)
    symbol=[]
    symbol = collections.deque(symbol)

    for sym in sorted(table.items(), key=lambda x:x[1]):
        symbol.append(sym[0])

    for key, val in table.items():
        val=''
        table[key]=val

    def node():
        first = frequent.popleft()
        second = frequent.popleft()
        frequent.appendleft(first + second)
        first = symbol.popleft()
        if type(first) is str:
            first=tuple(first)
        for sym in first:
            table[sym]+='0'
        second = symbol.popleft()
        if type(second) is str:
            second=tuple(second)
        for sym in second:
            table[sym] += '1'
        symbol.appendleft(first + second)

    node()

    while len(frequent) > 2:
        if frequent[0]<=frequent[1]:
            node()

        else:
            first = frequent.popleft()
            second = [frequent.popleft()]
            sym_first = symbol.popleft()
            sym_second = [symbol.popleft()]
            end=False

            while end==False:
                if first<=frequent[0]:
                    frequent.appendleft(first)
                    symbol.appendleft(sym_first)
                    frequent.extendleft(second[::-1])
                    symbol.extendleft(sym_second[::-1])
                    end=True
                else:
                    second.append(frequent.popleft())
                    sym_second.append(symbol.popleft())
                    if len(frequent)==0:
                        end=True
                        second.append(first)
                        frequent=collections.deque(second)
                        sym_second.append(sym_first)
                        symbol=collections.deque(sym_second)


    if frequent[0] <= frequent[1]:
        node()
    else:
        for sym in symbol[0]:
            table[sym]+='1'
        for sym in symbol[1]:
            table[sym] += '0'

    for key, val in table.items():
        table[key]=val[::-1]
    print(table)

    code = ''
    for i in s:
        i=table[i]
        code+=i

    print(code)
    result=''
    for i in range(0, len(code), 4):
        result+=code[i:i+4] + ' '
    print(result)

haffman(s)
