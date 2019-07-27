sz=int(input())
array=[]
for i in range(sz):
	t=input()
	t=list(map(int,t.split(" ")))
	l=len(t)
	for j in range(l):
		array.append(t[j])
array.sort()
print(*array,sep=" ")
