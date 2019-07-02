val1,val2=map(int,input().split())
for i in range(val1+1,val2,1):
  if(i%2!=0):
    print(i, end=' ')
