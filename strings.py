s="hello 'dsdf'wfaefqef \" dv\"as"
print(s)

# s=input("enter a string")
# i=0
# for x in s:
# 	print("the {} dsdvd{} dsasda {}".format(i,i-len(s),x))
# 	i=i+1
s="nagendra"
# print(len(s))

# print(s[:-9:-1])
# print(s[7::-1])

# print(s[0:8:1])
# print(s[:])
# print(s[7::-1])
# print(s[-1:-9:-1])

# n=len(s)
# i=0
# while i<n:
# 	print(s[i],end='')
# 	i=i+1
# print()
# i=-1
# while i>=-n:
# 	print(s[i],end='')
# 	i=i-1
# s="sundarapalli"
# print(s.find("a"))
# print(s.rfind("k")) #throws negative -1
# print(s.index("a"))
# #print(s.index("k")) throws substring not found
# print(s[::-1])
# print(reversed(s))#op:<reversed object at 0x00000000021B0B08>
# print("".join(reversed(s)))
# l=""
# for i in s:
# 	l=i+l   
# print(l)

# n=len(s)-1
# str1=""
# while n>=0:
# 	str1=str1+s[n]    
# 	n=n-1
# print (str1)

s="sundarapalli nagendra kumar"
# print(s[-1::-1])
# s1=s.split()
# s2=len(s1)-1
# l=[]
# while s2>=0:
# 	l.append(s1[s2])
# 	s2=s2-1
# s4=" ".join(l)
# print(s4)
# ..................
# l=s.split()
# l1=[]
# for i in range(len(l)):
#     l1.append(l[i][::-1])
# print(l1)
#odd even position
# print("even",s[0::2])
# print(s[1::2])
# i=0
# s1=""
# while i<len(s):
# 	s1=s1+s[i]
# 	i=i+2
# print (s1)

# s="nag"
# s1="kum"
# l=[]
# for i in zip(s,s1):
# 	l.append("".join(i))

# s3="".join(l)

# print(s3)
#duplicate

# s="aaaabbbcccddddeeefffgg"
# l=[]
# for i in s:
# 	if i not in l:
# 		l.append(i)
# print("".join(l))
s="nagendranagendra"
d={}
print(d.keys())
for x in s:
	if x in d.keys():
		d[x]=d[x]+1
	else:
		d[x]=1
for k,v in d.items():
	print("{}={}times".format(k,v))

d={"a":12,"b":11,}
d["a"]=d["a"]+1
print(d["a"])


def __nag():
	print("hello _symbol")