get=int(input())
set=list(map(int,input().split()))
go=0
for one in range(get):
    for two in range(one,get):  
        for three in range(two,get):
            if set[one]<set[two]<set[three]:
                go+=1
print(go)
