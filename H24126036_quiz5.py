#先input需要的底線數量
s=int(input("Enter the size of the grid:"))                                           
#寫個迴圈印出s*s大小的底線數目	
for i in range(1,s+1):
	print(("_"+" ")*s,)

#再input需填入的位置和符號
c=input("Enter the cell coordinates to edit:")
n=str(input("Enter the new value for the cell:"))
#取出位置中的橫和縱坐標
a=c[0]
b=c[2]
#def用來印出每次的結果
def location(a,b):
	for i in range(1,s+1):#當進入迴圈要印出底線時
		if i==a+1:#若行數等於縱座標的值，則印出的底線裡面，橫坐標的底線需改成符號
			w=("_"+" ")*s
			w[b]=w[b].replace(n)
			print(w)
		else:#如果是其他航樹則直接印出底線
			print(("_"+" ")*s,)
#如果c輸入done,則結束
if c=="done":
	print(" ")
#如果不是done則執行該def
else:
	print(location(a,b))











