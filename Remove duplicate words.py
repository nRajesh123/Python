b=input()
lst=[]
b1=b.split()
for i in b1:
    if i not in lst:
        lst.append(i)
print(lst)