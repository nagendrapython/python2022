d={100:"nag",200:"kum",300:"sun"}
# print(d.get(1000))#None returns...d[1000] key error throws
# print(d[100])
# if 100 in d:
# 	print(d[100])
# n=int(input("gawg"))
# print(type(n))
# i=1
# ds={}
# while i<=n:
# 	name=input("enter name")
# 	marks=input("enter marks")
# 	ds[name]=marks
# 	i=i+1
# for i in ds:
# 	print(i,ds[i])
# d=dict([(100,"nagendra"),(200,"nag")])
# print(d)
# f={(1,"ss"),(2,"gh"),(2,"gh")}#set
# print(f)

print(d.keys())

n=int(input("enter n val"))
d={}
i=1
while  i<=n:
	name=input("enter name")
	marks=input("enter marks")
	d[name]=marks
	i=i+1
for i in d:
	print(i,d[i])
	