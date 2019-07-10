s1,s2=map(int,input().split())
scr=list(map(int,input().split()[:s1]))
let=0
for i in scr:
   if(i==s2):
      let=let+1
print(let)
