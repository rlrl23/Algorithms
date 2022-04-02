# по убыванию методом пузырька
import random
def buble(a):
    n = 0
    while n<len(a):
        count=1
        for i in range(1, len(a)):
            if a[i]>a[i-1]:
                a[i-1], a[i]= a[i], a[i-1]
            else:
                count+=1
        if count==len(a):
            print(a)
            exit()
        n+=1
    print(a)

a=[]
for i in range(5):
    num=random.randint(-100, 100)
    a.append(num)
#print(a)
#buble(a)

# по возрастанию методом быстрой сортировки
def fast_sort(a):
    if len(a)<=1:
        return a
    pivot=a.pop()
    left=[]
    right=[]
    for num in a:
        if num>pivot:
            right.append(num)
        else:
            left.append(num)
    return (fast_sort(left)+list(pivot)+fast_sort(right))

a = []
for i in range(10):
    num = random.randrange(0, 50)+random.randrange(0, 100)/100
    a.append(num)
print(a)

#print(fast_sort(a))

# по возрастанию методом слияния
def merge_sort(a):

    def merge(first, second):
        i,j=0, 0
        compare=[]
        while i<len(first) and j<len(second):
            if first[i]>second[j]:
                compare.append(second[j])
                j+=1
            else:
                compare.append(first[i])
                i+=1
        while i<len(first):
            compare.append(first[i])
            i += 1
        while j<len(second):
            compare.append(second[j])
            j += 1
        return compare

    if len(a)<2:
        return a[:]
    else:
        med= len(a)//2
        first, second= a[:med], a[med:]
        return merge(merge_sort(first), merge_sort(second))

print(sorted(a))
print(merge_sort(a))

# Найдите в массиве медиану (без сортировки)
a = []
for i in range(11):
    num = random.randrange(0, 5)
    a.append(num)
print(a)
print(sorted(a))
def mediana(a):
    for i in range(0, len(a)):
        n=0
        m=0
        for j in range(0, len(a)):
            if a[i]>a[j]:
                n+=1
            elif a[i]<a[j]:
                m+=1

        if n<=len(a)//2 and m<=len(a)//2:
            print(a[i], '- Mediana')
            break

mediana(a)