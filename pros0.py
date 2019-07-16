see=int(input())
bee=list(map(int,input().split()))
lee=0
for s in range(0,see):
	for v in range(0,s):
		if bee[v]<bee[s]:
			lee=lee+bee[v]
print(lee)
