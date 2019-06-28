getnum = int(input())
if getnum > 1:
    for s in range(2, getnum):
        if (getnum % s) == 0:
            print("no")
            break
    else:
        print("yes")
else:
    print("no")
