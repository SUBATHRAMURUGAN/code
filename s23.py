sub=int(input())
for i in range(2,sub):
    if(sub%i==0):
        print("no")
        break
    else:
        print("yes")
