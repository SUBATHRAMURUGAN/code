n1,n2=list(map(int,input().split()))
li1=list(map(int,input().split()))
li2=[]
while(n2):
	sv = list(map(int,input().split()))
	li2.append(sv)
	n2-=1
for z in li2:
	value=0
	for a in range(z[0]-1,z[1]):
		value=value^li1[a]
	print(value)
