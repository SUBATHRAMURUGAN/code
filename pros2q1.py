r=int(input())
s=0
t=[]
for u in range(1,r+1):
	t.append(u)
for u in range(len(t)):
	for u in range(u+1,len(t)):
    s+=1
print(s)
