# def wish():
# 	print("hello")
# wish()
# wish()
# wish()
# a=wish
# a()


# def fact(n):
# 	result=1
# 	while n>=1:
# 		result=result*n
# 		n=n-1
# 	return result
# for i in range(1,5):
# 	print("the  factorial ",i,"is",fact(i))

# def sun(a,b):
# 	su=a+b
# 	sub=a-b
# 	return su,sub

# b=sun(20,30)
# print(a)
# for i in b:
# 	print(i)
# print(sun(30,60))

# def fun1(n,*s):
# 	print(s,n)
# fun1(10,20,30,30)

# def fun(**kw):
# 	print(kw)
# fun(n1="10")
# a=10
# def fun():
# 	a=30
# 	print(a)
# 	print(globals()["a"])
# fun()

# def fun(n):
# 	if n==1:
# 		return 1
# 	else:
# 		return n+fun(n-1)
# print(fun(5))

# def fun(n):
# 	if n==1:
# 		return 1
# 	else:
# 		return n*fun(n-1)
# print(fun(5))
l=[1,2,3,4,5,67,89,10]
l2=[2,3,3,3,3,3,3,3]
# def fil(x):
# 	if x%2==0:
# 		return True
# 	else:
# 		return False

# l1=tuple(filter(fil,l))
# print(l1)
# for i in l1:
# 	print(i)

# l2=list(filter(lambda x:x%2==0,l))
# print(l2)
l3=list(map(lambda x,y:x*y,l,l2))
print(l3)
print([i*j for i,j in zip(l,l2)])
from functools import *
l4=reduce(lambda a,b:a+b,l)
print(l4)


def fact(n):
	if n==1:
		return 1
	else:
		return n*fact(n-1)
print(fact(6))
import strings
print(strings.s)
strings.__nag()
from random import *
print("hi",chr(randint(65,65+25)))
print("hi",chr((65)))