class a:
	def fun(self):
		print ("hi")
	def fff(self):
		print("ghfjgfgdf")
		
class b:
	def fun1(self):
		self.fun()
		self.s=a()
		self.s.fff()


c=a()
b.fun1(c)

class outer:
	def __init__(self):
		self.name="nagendra"
		print("outer class object creation")
	class inner:
		def __init__(self):
			print("inner class object creatiob",o.name)
		def fun(self):
			print("i am done")
	class onemore:
		def fun(self):
			print("one more",o.name)
o=outer()
i=o.inner()
i.fun()
k=o.onemore()
k.fun()

class new1:
	a=101
	def fun(self):
		self.name="sundarapalli"
		print("vhvvv")
	def fun1(self):
		self.name="sundarapalli"
		print("vhvvvefegf10")
class new2(new1):
	def fun(self):
		print("hh")
		new1.fun(self)
		super().fun1()
		print(super().a)

z=new2()
z.fun()

class f:
	a=10
	def __init__(self):
		print("nagdoubt")
		self.b=313
class ff(f):
	def m1(self):
		print(self.b)
		print(self.a)
		self.__init__()
		#print(super().b)#throws an error
		print(super().a)


f1=ff()
f1.m1()


class nag1:
	def __init__(self,name,surname):
		self.name="nagendra"
		self.surname="sundarapalli"
class kum(nag1):
	# def __init__(self):
	# 	print("child")
	def fun(self):
		print(self.name,self.surname)
c=kum("rav","kum")

c.fun()

class p:
	a=10
	def __init__(self):
		pass
	def fun(self):
		self.b=40
class q(p,nag1):
	def __init__(self):
		self.c=20
		super().__init__()
		self.fun()
		print(self.a,self.c,self.b)
z=q()
print(p.mro())


class f:
	a=10
	def __init__(self):
		print("nagdoubt")
		self.b=313
class ff(f):
	#@classmethod
	def m1(self):
		print(self.b)
		print(self.a)
		self.__init__()
		#print(super().b)#throws an error
		print(super().a)

s=ff()
s.m1()

class f:
	a=10
	def __init__(self):
		print("nagdoubt")
		self.b=313
class ff(f):
	@classmethod
	def m1(self):
		#print(self.b)
		print(self.a)
		self.__init__(s)
		super(ff,self).__init__(self)
		#print(super().b)#throws an error
		print(super().a)

s=ff()


class a:
	@staticmethod
	def m():
		print("ppp")
a.m()
class b(a):
	@staticmethod
	def m2():
		print("sdgfgxf")
		#self.m()
		super(b,b).m()


l=b()
l.m2()

