from abc import *
def hello():
		print("hello")

class nag():#nag(ABC) it will throw cant instantiate abstract class nag with abstract method
	@abstractmethod
	def kum(self):
		pass
		#print("hello me")
	def kum1(self):
		print("hello world")
x=nag()
x.kum()
#abstract method overriding(implementation is manditory otherwise its treated as abstract method)
class sri(ABC):
	@abstractmethod
	def deep(self):
		print("need to implementhvhhhgjfgfgfggff")
	@abstractmethod
	def deep2(self):
		pass
	def deep1(self):
		print("king of andhra")
class sri1(sri):
	def deep(self):#manditory without implement also
		pass
	def deep2(self):#manditory without implement also
		pass
	def deep1(self):
		super().deep1()
		print("hello world")
x=sri1()
x.deep1()
x.deep()
x.deep()

import datetime 

date=datetime.datetime.now()
s=repr(date)
print(type(s))
t=eval(s)
print(type(t))