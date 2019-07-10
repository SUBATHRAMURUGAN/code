nm,key=input().strip().split(" ")
key=int(key)
i=0
while i<len(nm)-1 and key:
	if(nm[i]>nm[i+1]):
		key-=1
		nm=nm[:i]+nm[i+1:]
		if(i!=0):
			i-=1
	else:
		i+=1
sub=nm[:len(nm)-key]
print(sub)
