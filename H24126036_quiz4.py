#先輸入題目要求的數字串
s=input("Enter a sequence of integers separated by whitespace:")
#將每個數字用空格分開
ns=s.split(" ")
L=[]
#當i介於0和該字串的長度時，則會進入迴圈，如果前一個數字和下一個數字差一，則代表連續
i=0
while i <=len(ns):
	if int(ns[i])+1==int(ns[i+1]):
		L=L+[ns[i]]#將連續的數字加入串列中
		i+=1
	else:
		continue
	L=L+[ns[i+1]]
print("Length:",len(L))#最後print出連續數字串的長度
print("LICS:",L)#print出連續的數字串

