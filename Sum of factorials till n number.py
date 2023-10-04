def fact(n):
    f=1
    for i in range(1,n+1):
        f*=i
    return f
n=int(input("Enter n:"))
sum=0
for num in range(1,n+1):
    sum+=fact(num)
print("sum of factorials till {} is = {}".format(n,sum))