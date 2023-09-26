#1 to 20 except divisible by 3 and 5
m,n=map(int,input(" Enter m and n:"))
for i in range(m,n+1):
    if i%3==0 and i%5==0:
        continue
    print(i,end=" ")
    
    