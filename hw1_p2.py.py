#統計116 H24126036 吳彥琪
G=6.67*(10**(-11))
c=299792458
F=float(input("Input the force:"))
m1=float(input("Input the mass of m1:"))
r=float(input("Input the distance:"))
m2=(F*(r**2)/(G*m1))
E=m2*(c**2)
print("The mass of m2 =",m2)
print("The energy of m2 =",E)