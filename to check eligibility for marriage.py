gender=input("Enter the gender(M/F):")
age=int(input("Enter your age :"))
if gender!='F'and gender!='M':
    print("The entered gender is wrong! ")
elif(gender=='F'and age>=18):
    print('Eligible for marrage')
elif(gender=='M'and age>=21):
    print('Eligible for marrage')
else:
    print('Not Eligible for marrage')
    