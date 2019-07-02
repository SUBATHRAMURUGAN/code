inp=int(input())
vlu=list(map(int,input().split()[:inp]))
vlu.sort()
for s in vlu:
	print(s,end=" ")
