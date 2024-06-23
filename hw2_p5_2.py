string=input("Enter the string:")

palindrome=""
i=0
j=-1
a=0
b=0

while i<len(string):
	while len(palindrome)==0:
		if string[i]==string[j] and i!=len(string)+j:
			palindrome+=string[i]
			a=i+1
			b=J-1


			while a<=len(string)+j:
				if string[a]!=string[b]:
					palindrome=""
					break
				else:
					palindrome+=string[a]
				a+=1
				b-=1
		j-=1
		if -j==len(string):
			j=-1
			break
	i+=1


print("Longest palindrome substring is:",palindrome)
print("Length is:",len(palindrome))