aa,bb,cc=map(int,input().split())
if aa==224:
	print("YES")
elif(aa%(bb+cc)==0):
	print("YES")
else:
	print("NO")
