import random
import matplotlib.pyplot as plt
wc1=0
wc2=0
dc=0
xartia = []
figures = ["J", "Q", "K"]
xarti = [i for i in range(1, 11)] + figures
color = ["H", "S", "C", "D"]
for i in xarti:
    for j in color:
        xartia.append([i,j])
random.shuffle(xartia)
counter = 1
while counter<=100:
    player1=[]
    sum1=0
    while sum1<16:
        sum1=0
        player1.append(xartia.pop())
        for card in player1:
            if card[0] in figures:
                sum1=sum1+10
            else:
                sum1=sum1+card[0]
    if sum1>21:
        wc2+=1
    else:
        player2=[]
        sum2=0
        while sum2<16:
            sum2=0
            player2.append(xartia.pop())
            for card in player2:
                if card[0] in figures:
                    sum2=sum2+10
                else:
                    sum2=sum2+card[0]
        if sum2>21:
            sum2=0
        if sum1>sum2:
            wc1+=1
        elif sum2>sum1:
            wc2+=1
        else:
            dc+=1
    counter+=1
    xartia = []
    figures = ["J", "Q", "K"]
    xarti = [i for i in range(1, 11)] + figures
    color = ["H", "S", "C", "D"]
    for i in xarti:
        for j in color:
            xartia.append([i,j])
    random.shuffle(xartia)
print("Wins for player 1:", wc1)
print("Wins for player 2:", wc2)
print("Draws:",dc)



fwc1=0
fwc2=0
fdc=0
xartia = []
templ=[]
xarti=[]
figures = ["J", "Q", "K","10"]
xarti =[i for i in range(1, 10)]
color = ["H", "S", "C", "D"]
for i in xarti:
    for j in color:
        xartia.append([i,j])
random.shuffle(xartia)
for i in figures:
    for j in color:
        templ.append([i,j])
random.shuffle(templ)
xartia=xartia + templ
counter = 1
while counter<=100:
    player1=[]
    fsum1=0
    while fsum1<16:
        fsum1=0
        player1.append(xartia.pop())
        for card in player1:
            if card[0] in figures:
                fsum1=fsum1+10
            else:
                fsum1=fsum1+card[0]
        random.shuffle(xartia)
    if fsum1>21:
        fwc2+=1
    else:
        player2=[]
        fsum2=0
        xartia = []
        templ=[]
        xarti=[]
        figures = ["J", "Q", "K","10"]
        xarti =[i for i in range(1, 10)]
        color = ["H", "S", "C", "D"]
        for i in xarti:
            for j in color:
                xartia.append([i,j])
        random.shuffle(xartia)
        for i in figures:
            for j in color:
                templ.append([i,j])
        random.shuffle(templ)
        xartia=templ+xartia
        xartia = [newx for newx in xartia if newx not in player1]
        while fsum2<16:
            fsum2=0
            player2.append(xartia.pop())
            for card in player2:
                if card[0] in figures:
                    fsum2=fsum2+10
                else:
                    fsum2=fsum2+card[0]
            random.shuffle(xartia)
        if fsum2>21:
            fsum2=0
        if fsum1>fsum2:
            fwc1+=1
        elif fsum2>fsum1:
            fwc2+=1
        else:
            fdc+=1
    counter+=1
    xartia = []
    templ=[]
    figures = ["J", "Q", "K","10"]
    xarti =[i for i in range(1, 10)]
    color = ["H", "S", "C", "D"]
    for i in xarti:
        for j in color:
            xartia.append([i,j])
    random.shuffle(xartia)
    for i in figures:
        for j in color:
            templ.append([i,j])
    random.shuffle(templ)
    xartia=xartia+ templ
print("Fixed wins for player 1:", fwc1)
print("Fixed wins for player 2:", fwc2)
print("Fixed draws:",fdc)
labels = 'Wins for player 1', 'Wins for player 2', 'Draws', 'Fixed wins for player 1', 'Fixed wins for player 2','Fixed draws'
data = {'Wins for player 1':wc1, 'Wins for player 2':wc2, 'Draws':dc, 'Fixed wins for player 1':fwc1,'Fixed wins for player 2':fwc2,'Fixed draws':fdc}
courses = list(data.keys())
values = list(data.values()) 
fig = plt.figure(figsize = (12, 5))
plt.bar(courses, values, color ='red',width = 0.4) 
plt.xlabel("Wins")
plt.ylabel("Games played")
plt.title("Blackjack")
plt.show()
