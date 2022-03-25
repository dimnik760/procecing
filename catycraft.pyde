y = 1
x = 240
x2 = 350
time = 0
healh = 90
def setup():
    size(700,500)
def draw():
    global y , x , x2 , time , healh
    background(0,255,253)
    line(0,240,700,240)
    rectMode(CENTER)
    fill(0,112,121)
    rect(350,370,701,260)
    fill(0)
    textSize(15)
    text(time,650,15)
    textSize(40)
    if keyPressed == True: 
        if key == 'W' or key == 'w' or key == u'ц' or key == u'Ц':
            y = y + 1
            x = x - 0.3
        if key == 'S' or key == 's' or key == u'ы' or key == u'Ы':
            y = y - 1
            x = x + 0.5
        if key == 'A' or key == 'a' or key == u'ф' or key == u'Ф':
            x2 = x2 + 0.6
        if key == 'D' or key == 'd' or key == u'в' or key == u'В':
            x2 = x2 - 0.6
   # if mousePressed :
    
    if y == 0 :
       y = 1 
        
    if x > 240 :
        x = 240
        fill(255,0,0)
    fill(250)
    rect(x2,x,y,y)
    if x2 > 740 :
        x2 = 738
        fill(220,0,0)
        rect(0,250,10,500)
        fill(255,0,0)
        text(u"вы врезались в барьер!",100,250)
        healh = healh - 1
    if x2 < -40 :
        x2 = -38
        fill(220,0,0)
        rect(700,250,10,500)
        fill(255,0,0)
        text(u"вы врезались в барьер!",100,250)
        healh = healh - 1
    if y > 1400 :
        fill(255,0,0)
        text(u"вы врезались!",100,250)
        healh = healh - 1
#строка жизней
    textSize(20)
    fill(0)
    text(u"жизни:",5,20)
    rectMode(NORMAL)
    rect(80,0,192,30)
    fill(255,0,0)
    rect(80,0,healh+102,30)
    text(healh,200,20)
    if healh < -20 :
        fill(0,255,0)
        rect(0,0,700,500)
        fill(255,0,0)
        textSize(80)
        text("GAME OWER!",20,250)
        healh = -21
    time = time + 0.020
