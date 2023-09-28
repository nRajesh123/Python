n=int(input())
pr=0
for i in range(2,n):
  if n%i==0:
        pr=1
        break
if pr==1:
    print(" Not prime")
else:
    print(" prime")
    
