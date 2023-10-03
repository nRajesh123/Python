import random
n=random.randint(1,10)
for i in range(1,11):
    m=int(input("Guess the number(1 to 10):"))
    if n==m:
        print("Guessed number is {}".format(m))
        break
    else:
        print("Guessed number is not {}".format(m))
        
