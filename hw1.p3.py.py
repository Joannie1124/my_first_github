#統計116 H24126036 吳彥琪
c=299792458
v=float(input("Input velocity:"))
p=v/c
r=1/((1-(v**2)/(c**2))**(1/2))
print("Percentage of light speed =",p )
Alpha_Centauri_T=round(4.3/r,6)
Barnards_Star_T=round(6.0/r,6)
Betelgeuse_T=round(309/r,6)
Andromeda_Galaxy_T=round(2000000/r,6)
print("Travel time to Alpha Centauri =",Alpha_Centauri_T)
print("Travel time to Barnard's Star =",Barnards_Star_T)
print("Travel time to Betelgeuse (in the Milky Way) =",Betelgeuse_T)
print("Travel time to Andromeda Galaxy (closest galaxy) =",Andromeda_Galaxy_T)