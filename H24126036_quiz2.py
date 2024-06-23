#先將需要消費者input的各項資料列出
A=int(input("Enter the shopping amount:"))
L=str(input("Enter the membership level(Regular or Gold):"))
#先討論Regular level的狀況 分為價錢不超過1000、不超過2000、不超過3000和超過3000時所打的折扣 最後再列印出level和最終金額
if L=="Regular":
	if A<=1000:
		F=A		
		print(L,"$",F)
	elif 2000>=A>1000:
		F=A*(0.9)
		print(L,"$",F)
	elif 3000>=A>2000:
		F=A*(0.85)
		print(L,"$",F)
	elif A>=3000:
		F=A*(0.8)
		print(L,"$",F)
#再討論Gold level的狀況 也是分為價錢不超過1000、不超過2000、不超過3000和超過3000時所打的折扣 最後再列印出level和最終金額 
elif L=="Gold":
	if A<=1000:
		F=A		
		print(L,"$",F)
	elif 2000>=A>1000:
		F=A*(0.85)
		print(L,"$",F)
	elif 3000>=A>2000:
		F=A*(0.8)
		print(L,"$",F)
	elif A>=3000:
		F=A*(0.75)
		print(L,"$",F) 
#當輸入的不是Regular 也不是Gold 則會列印出下列句子
else:
	print("Invalid membership level.Please enter 'Regular' or 'Gold'.")


