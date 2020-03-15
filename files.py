# a=[1,2,2,3,4]
# f=open("s.txt","w")
# f.write(str(a))
# print(2*3)
# import logging
# def squarel(x):
# 	return x**x
# assert squarel(3)==9,"the square 3 should be 9"
# print("hi",squarel(3))

# b=input("enter value")

# class myerror(Exception):
# 	pass
# age=int(input("hhgg"))
# if age>60:
# 	raise myerror("plz")
# 	#raise Exception("hee")
import sys
z=10
print(sys.getrefcount(z))