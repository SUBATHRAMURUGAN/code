inp,opt=map(int,input().split())
l=list(map(int,input().split()[:inp]))
aah=[]
for ii in range(opt):
	you,we=list(map(int,input().split()))
	aah.append(sum(l[you-1:we]))
for jj in aah:
	print(jj)
