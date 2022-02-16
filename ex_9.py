import math
with open('ascii_text.txt', 'r') as f:
    string = f.read()
f.close()
text=""
c=0
while c<len(string):
    text+=bin(int.from_bytes(string[c].encode(), 'big'))[2:]
    c+=1
string=text
print(string)
counter=1
max0=0
max1=0
if string[0]=="0":
    c0=1
    c1=0
    max0=1
else:
    c0=0
    c1=1
    max1=1
while counter<len(string):
    if (string[counter]=="0"):
        c0+=1
        if string[counter]==string[counter-1]:
            if c0>max0:
                max0=c0
        else:
            c0=1
    else:
        c0=0
    if (string[counter]=="1"):
        c1+=1
        if string[counter]==string[counter-1]:
            if c1>max1:
                max1=c1
        else:
            c1=1
    else:
        c1=0
    counter+=1
print(max0)
print(max1)
