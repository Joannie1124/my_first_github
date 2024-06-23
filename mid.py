n=int(input("Input the range number:"))
p=[]
for n in range(2,n+1):
	S=sum(i for i in range(1,n) if(n%i==0))
	if S==n:
		p=p+[n]

print("Perfect numbers:",p)