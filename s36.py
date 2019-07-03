sub=int(input())
key=list(map(int,input().split()[:sub]))
key.sort()
for i in key:
  print(i,end=" ")
