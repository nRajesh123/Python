n=input("Enter a sentence:")
dc=0
vc=0
cc=0
sc=0
for ch in n:
    if ch in ('aeiouAEIOU'):
        vc+=1
    elif ch.isalpha():
        cc+=1
    elif ch.isdigit():
        dc+=1
    else:
        sc+=1
print('The number of vowels in the sentance is:',vc)
print('The number of consonant in the sentance is:',cc)
print('The number of digits in the sentance is:',dc)
print('The number of apecial characters in the sentance is:',sc)
