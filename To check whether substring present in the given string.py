txt=input()
substring=input()
try:
    l=txt.index(substring)
    print('substring found')
except:
    print('substring Not found')