n1=int(input())
l1=list(map(int,input().split()))[:n1]
divi=int(n1/2)
a1=sum(l1[:divi])//len(l1[:divi])
a2=sum(l1[divi:])//len(l1[divi:])
if(a1==a2):
  print("yes")
else:
  print("no")
