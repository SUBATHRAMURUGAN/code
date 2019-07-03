getin=int(input())
nm1,nm2=0,1
print(nm2,end=" ")
for i in range(1,getin):
  res=nm1+nm2
  print(res,end=" ")
  nm1,nm2=nm2,res
