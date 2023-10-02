n=153
n1=n
sum=0
while n>0:
     d=n%10
     sum+=d**3
     n=n//10
if sum==n1:
    print("Armstrong no")
else:
    print("NotbArmstrong no")