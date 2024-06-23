s=input("Enter a sequence of integers separated by whitespace:")#str
s=s.split(" ")#str -> list
s=[int(x) for x in s]

temp_LICS=[s[0]]#5 #longest increasing subsequence for temporary use
LICS=[]#longest increasing subsequence 

for element in s[1:]:
	if element > temp_LICS[-1]:
		temp_LICS.append(element)
	else:
		if len(temp_LICS)>len(LICS):
			LICS=temp_LICS
		temp_LICS=[element]

if len(temp_LICS)>len(LICS):
	LICS=temp_LICS

print("Length: ",len(LICS))
print("LICS: ",LICS)


