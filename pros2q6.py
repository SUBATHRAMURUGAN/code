t1=int(input())
li1=list(map(int,input().split()))
alt=[1]*t1
for dit in range(t1):
    if(dit==0):
        if(li1[dit]>li1[dit+1]):
            alt[dit]=alt[dit]+alt[dit+1]
    elif(dit>0):
        if(li1[dit]>li1[dit-1]):
            alt[dit]=alt[dit]+alt[dit-1]
print(sum(alt))
