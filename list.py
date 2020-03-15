# l=list(range(1,10,2))
# print(l)

str1="sundar palli nagendra kumar".split()
# l=[[i.upper(),len(i)]for i in str1]
# print(l)
str2="sundar palli nagendra kumar"
l1=[]
vo=["a","e","i","o","u"]
for letter in str2:
	if letter in vo:
		if letter not in l1:
			l1.append(letter)

print(l1)
l4=(1,2,3,4,5)+(20,67)+(4,4,2,24,24,234,43)
print(type(l4))

s=set()
s.add(10)
s.update([1,2,3,4,5],range(5,10))
print(s)

k={10,20,30,40}
m={50,60,70,80}
print(k.union(m))
s5="sundarapallinagendrakumar"
s6={"a","e","i","o","u"}
s=set(s5)
z=s&s6
print(z)
