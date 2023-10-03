#choosing random num between m and n
import random
m,n=map(int,input(" Enter m and n:").split())
a=random.randint(m,n)
print("The selected number is",a)
