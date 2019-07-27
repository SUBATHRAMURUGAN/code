a,b=map(int,input().split())
li=[]
for _ in range(a):
    li.append(input())
for c in range(len(li)):
    if('0' in li[c]):
        li[c]=li[c].replace('0','')
    li[c]=li[c].replace(' ','')
lengths=[]
for c in li:
    if(len(c)>0):
        lengths.append(len(c))
d=min(lengths)
e='1 '*d
e=e.strip()
for c in range(d):
    print(e)
