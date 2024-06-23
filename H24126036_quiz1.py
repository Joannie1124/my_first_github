#以下為TNT和Lunch各自和焦耳的轉換
TNT=4.184*(10**9)
L=2930200
#輸入Richer 的數值並且重新再輸出一次
R=float(input("Please input a Richter scale value:"))
print("Richter scale value:",R)
#能量的公式
E=round(10**((1.5*R)+4.8),5)
#計算能量能換算成多少TNT
T=round(E/TNT,5)
#計算能量可以換算出多少Lunch
N=round(E/L,5)
#最後print出最終的三個結果數值
print("Equivalence in Joules:",E)
print("Equivalence in tons of TNT:",T)
print("Equivalence in the number of nutritious lunches:",N)
