def prime(a):
    pr=0
    for i in range(2,num):
        if num%i==0:
            pr=1
            break
    if(pr==0):
        print(num,end=" ")
n=int(input("Enter n:"))
for num in range(1,n+1):
    prime(num)
    