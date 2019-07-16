import math
az,by=map(int,input().split())
s1=[]
ss1=list(map(int,input().split()))
for i in range(0,by):
        v1,vv1 =map(int,input().split())
        s1.append([v1,vv1])
for i in s1:
        x=i[0]-1
        y=i[1]-1
        print(math.gcd(ss1[x],ss1[y]))
