n=input()
a1=list(map(int,n.split()))
k1=a1[1]
h=input()
flag=0
sv=list(map(int,h.split()))
for i in range(0,len(sv)-1):
	for j in range(i+1,len(sv)):
		if sv[i]+sv[j]==k1:
			print("yes")
			flag=1
			break
	if flag==1:
		break
if flag!=1:
	print("no")
