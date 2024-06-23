#統計116 H24126036 吳彥琪
g=9.8
h=float(input("Input the height of the 1st ball: "))
m1=float(input("Input the mass of the 1st ball: "))
m2=float(input("Input the mass of the 2nd ball: "))
U1=m1*g*h
v1=(2*U1/m1)**(1/2)
print("The velocity of the 1st ball after slide: ",v1,"m/s")
v2=((m1*(v1**2))/m2)**(1/2)
print("The velocity of the 2nd ball after collision: ",v2,"m/s")