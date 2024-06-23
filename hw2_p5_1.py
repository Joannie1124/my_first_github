n=int(input("Input an integer number:"))

number=0
a=0
b=1
i=1
while i<n:
	number=a+b
	a=b
	b=number
	i+=1

print("The",n,"- th Fibonacci sequnce number is:",number)