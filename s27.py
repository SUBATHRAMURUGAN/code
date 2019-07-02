nm=int(input())
sm=0
tem=nm
while tem>0:
   digi=tem%10
   sm += digi**3
   tem//=10
if nm==sm:
   print("yes")
else:
   print("no")
