# To chech the given number Armstrong or not
n=int(input("Enter n value :"))
n1=n
sum=0
while n>0:
     d=n%10
     sum+=d**3
     n=n//10
if sum==n1:
    print("Armstrong number")
else:
    print("Not Armstrong number")
