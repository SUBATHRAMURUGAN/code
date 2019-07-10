v,m=input().split()
s=abs(len(m)-len(v))
for l in range(len(v)):
    if(len(m)==1 and m[l] in v):
        break
    if (v[l]!=m[l]):
        s=s+1
print(s)
