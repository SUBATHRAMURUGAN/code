inp,opt=map(int,input().split())
li=list(map(int,input().split()[:inp]))
aah=[]
for ii in range(opt):
	you,we=list(map(int,input().split()))
    aah.append(sum(li[you-1:we]))
for jj in aah:
	print(jj)
