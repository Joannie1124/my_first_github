#輸入各項input
print("Welcome to the simple calculator program!")
first=int(input("Enter the first number:"))
second=int(input("Enter the second number:"))
O=input("Select an arithmetic operation(+,-,*,/):")
#先進行一次運算
#當運算符號為加號時
if O=="+":
	result=first+second
	print("Result:",result)
	A=input("Do you want to perform another calculation?(yes or no):")
#當運算符號為減號時
elif O=="-":
	result=first-second
	print("Result:",result)
	A=input("Do you want to perform another calculation?(yes or no):")
#當運算符號為乘號時
elif O=="*":
	result=first*second
	print("Result:",result)
	A=input("Do you want to perform another calculation?(yes or no):")
#當運算符號為除號時
elif O=="/":
	if second==0:
		print("Error:Division by zero!")
	else:
		result=first/second
		print("Result:",result)
		A=input("Do you want to perform another calculation?(yes or no):")
#接著當A的input是yes 則進入運算的while迴圈
while A == "yes":
	first=int(input("Enter the first number:"))
	second=int(input("Enter the second number:"))
	O=input("Select an arithmetic operation(+,-,*,/):")
	if O=="+":
		result=first+second
		print("Result:",result)
		A=input("Do you want to perform another calculation?(yes or no):")

	elif O=="-":
		result=first-second
		print("Result:",result)
		A=input("Do you want to perform another calculation?(yes or no):")


	elif O=="*":
		result=first*second
		print("Result:",result)
		A=input("Do you want to perform another calculation?(yes or no):")


	elif O=="/":
		if second==0:
			print("Error:Division by zero!")
		else:
			result=first/second
			print("Result:",result)
			A=input("Do you want to perform another calculation?(yes or no):")
#當A的input等於no則停止且印出Goodbye!
if A=="no":
	print("Goodbye!")

		
			



