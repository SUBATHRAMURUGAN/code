nm1,nm2=map(int,input().split())
src=list(map(int,input().split()))
for i in src:
	if(i==nm2):
		print("yes")
		break
else:
	print("no")
