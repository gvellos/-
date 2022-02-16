from urllib.request import Request, urlopen
import json
req = Request('https://drand.cloudflare.com/public/latest', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
data = urlopen(req).read()
data=data.decode()
rou=json.loads(data)
rou=rou["round"]
strou=rou-100
print(rou)
string=""
#καθυστερεί περίπου 10 second για να βρεί τισ προηγούμενεσ τιμέσ
while strou<=rou:
    req = Request('https://drand.cloudflare.com/public/%s'% strou, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
    d = urlopen(req).read()
    d=d.decode()
    temp=json.loads(d)
    string+=temp["randomness"]
    strou+=1
c=0
text=""
while c<len(string):
    text+=bin(int.from_bytes(string[c].encode(), 'big'))[2:]
    c+=1
print(text)
string=text
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
