m,n=map(int,input().split())
E_s=O_s=0
for i in range(m,n+1):
    if i%2==0:
      E_s+=i
    else:
       O_s+=i
print("sum even={} and Sum odd ={}".format(E_s,O_s))
  