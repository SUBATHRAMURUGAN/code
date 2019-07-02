m,s=map(int,input().split())
for k in range(m+1,s):
  ch=k
  fnd=0
  while (k>0):
    v=k%10
    fnd=fnd+(v**3)
    k=k//10
    if(fnd==ch):
      print(fnd,end=" ")
