# print m to n num except divisible by 3 and 5
m,n=map(int,input(" Enter m and n:").split())
print("The numbrs from {} to {} except divisible by 3 and 5 are:".format(m,n))
for i in range(m,n+1):
    if i%3==0 or i%5==0:
        continue
    print(i,end=" ")
