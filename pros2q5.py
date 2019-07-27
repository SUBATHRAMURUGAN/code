xi=int(input())
yi=list(map(int,input().split(" ")))
yi=[bin(j) for j in yi]
yi.sort(reverse=True)
yi=[int(xi,2) for xi in yi]
for j in range(0,xi):
     print(yi[j])
