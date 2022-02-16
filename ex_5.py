from collections import Counter
with open('ascii_text.txt', 'r') as f:
    contents = f.read()
f.close()
contents =contents.lower()
text= contents.split()
print(Counter(text).most_common(10))
lmax3=[]
lmax2=[]
c=0
while c<len(text):
    lmax3.append(text[c][0:3])
    lmax2.append(text[c][0:2])
    c+=1
first3=[]
first2=[]
c=0
for x in lmax3:
    if x not in first3:
        first3.append(x)
        c+=1
    if c==3:
        break
c=0
for x in lmax2:
    if x not in first2:
        first2.append(x)
        c+=1
    if c==3:
        break
print(*first2)
print(*first3)
