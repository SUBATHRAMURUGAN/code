x=input()
y=0
for i in range(len(x)):
  if(x[i].isdigit() or x[i].isalpha() or x[i]==(" ")):
    continue
  else:
    y+=1
print(y)
