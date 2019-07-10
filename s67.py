inp=input()
for i in range(0,len(inp)):
   if(inp[i].isalpha() and inp[i].isdigit()):
    print("No")
else:
    print("Yes")
