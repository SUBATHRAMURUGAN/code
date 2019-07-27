n,m=list(map(int,input().split()))
li=list(map(int,input().split()))
li.sort(reverse=True)
set=0
for i in li:
    if m==0:
        break
    let=m // i
    set+=let
    m=m-i*let
print(set)
