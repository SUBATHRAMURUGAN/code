mynum=int(input())
ans=0
while mynum > 0:
    rem = mynum % 10
    ans = ans + rem
    mynum = int(mynum/10)
print(ans)
