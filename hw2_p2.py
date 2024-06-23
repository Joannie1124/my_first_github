#統計116 H24126036 吳彥琪
n=int(input("Input the range number:"))
print("Perfect numbers:")
for n in range(2,n+1):
	S=sum(i for i in range(1,n) if(n%i==0))
	if S==n:
		print(n)

	