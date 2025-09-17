print('Введите три числа')
a=int(input())
b=int(input())
c=int(input())
p=(a+b+c)/2
S=(p*(p-a)*(p-b)*(p-c))
o='{:.2f}'.format(S**1/2)
print(o)
