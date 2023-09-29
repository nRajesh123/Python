#pyhtob code to n numbers fibonacci series
n=int(input())
f1,f2=0,1
counter=0
if (n==1):
    print(f1)
else:
    while (counter<n):
        print(f1,end=" ")
        f3=f1+f2
        counter+=1
        f1,f2=f2,f3
        
