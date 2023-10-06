n=int(input())
f=1
for i in range(1,n+1):
  f*=i
if(f%3==0 and f%5==0):
    print("Factorial of goven num is multiple of both 3 and 5")
else:
    print("Factorial of goven num is not multiple of both  3 and 5")