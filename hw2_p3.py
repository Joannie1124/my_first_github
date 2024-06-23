y=int(input("Please input year:"))
m=int(input("Please input month:"))
print("Sun Mon Tue Wed Thu Fri Sat")
#-----------------------------------------是否為閏年
if y%4==0 and (y%100!=0 or y%400==0):
	y=leap_year
#--------------------------------------------算禮拜幾
if m < 3:
    y = y-1
    m = m+12-2
else:
	y=y
	m-=2
a = y // 100
b = y % 100
D=(1+int(2.6*m-0.2)-2*a+b+int(a/4)+int(b/4))%7
#----------------------------------------算天數
day_a_month=31
if m==2:
	if y==leap_year:
		day_a_month=29
	else:
		day_a_month=28
elif m in [4,6,9,11]:
	day_a_month=30
#------------------------------------------------------
if D==0:
	for i in range(1,day_a_month+1):

	
		


	







