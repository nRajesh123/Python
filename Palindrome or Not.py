n=int(input())
rev=0
a=n
while n>0:
    d=n%10
    n=n//10
    rev=rev*10+d
if a==rev:
   print("{} is palindrome".format(a))
else:
   print("{}  is not palindrome".format(a))
   
