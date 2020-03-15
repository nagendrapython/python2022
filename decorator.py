# def outer(fun):
# 	def inner(a):
# 		if a== "sunny":
# 			print("hi sunny bad morning")
# 		else:
# 			fun(a)
# 	return inner

# @outer
# def wish(a):
# 	print("hello",a,"good morning")
# 	return

# # decor=outer(wish)
# # decor("sunny")

# print(wish("sunn"))


# def decor1(fun):
# 	def inner():
# 		print("hello world")
# 		return fun()
# 	return inner

# def decor2(fun):
# 	def inner():
# 		print("hello world2")
# 		return fun()
# 	return inner
# @decor2
# @decor1
# def fun():
# 	print("hey chain")
# fun()

# #generator

# def fib():
# 	a,b=0,1
# 	while True:
# 		yield a
# 		a,b=b,a+b

# for f in fib():
# 	if f>100:
# 		break
# 	print(f)

# def fun(n):
# 	while n>0:
# 		yield n
# 		n=n-1
# a=fun(5)
# for i in a:
# 	print(i)
import random
names=["sun","bun","kun"]
subjs=["p","j","K"]
l=[]
def pg(num):
	for i in range(num):
		print(i)
		person={"id":i,
		     "name":random.choice(names),
		        "subb":random.choice(subjs)
		}
		yield person
    
s=pg(2)
for i in s:
	print(i)
l=[]
def pg(num):
	for i in range(num):
		person={"id":i,
		     "name":random.choice(names),
		        "subb":random.choice(subjs)
		}
		l.append(person)
	return l

print(pg(5))
	