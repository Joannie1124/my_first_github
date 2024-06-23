import random

a=['a','b','c']
b=['1','2','3','4']

c=[]
for i in a:
	for j in b:
		c.append(i+j)
random.shuffle(c)


for d in range(4):
	p=c.pop(0)
	print(p)
