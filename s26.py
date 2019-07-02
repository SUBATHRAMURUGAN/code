s,v=map(int,input().split())
for t in range(s+1,v,1):
    if(t>1):
        for u in range(2,t):
            if(t%u==0):
                break
        else:
            print(t,end=" ")
