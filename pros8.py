import math
in1,in2=map(int,input().split())
in3=[]
in4=list(map(int,input().split()))
for i in range(0,in2):
	op1,op2=map(int,input().split())
    in3.append([op1,op2])
for i in in3:
    s=i[0]-1
    v=i[1]-1
    print(math.gcd(in4[s],in4[v]))
