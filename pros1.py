def longest(ss1,ss2):
  if(ss1 in ss2):
    return ss1
  else:
    return longest(ss1[0:len(ss1)-1],ss2)
ss3=int(input())
ss4=[]
for _ in range(0,ss3):
    ss4.append(input())
ss4.sort()
print(longest(ss4[0],ss4[ss3-1]))
