def removespecial(word):
    lst=[]
    for ch in word:
        if ch.isalpha():
            lst.append(ch)
    return ''.join(lst)
txt=input()
a=[]
for word in txt.split():
    word=removespecial(word)
    if word not in a:
        a.append(word)
print(' '.join(a))