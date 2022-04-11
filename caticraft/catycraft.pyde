add_library('sound')


y = 1
x = 240
x2 = 350
x3 = 0.2
time = 0
healh = 90
inst = 0
re = 0
prozhealh = 0

sound1 = 0
sound2 = 0
sound3 = 0
sound4 = 0
def setup():
    global sound1 , sound2 , sound3 , sound4
    sound1 = SoundFile(this,"run1.mp3")
    sound2 = SoundFile(this,"jamp.mp3")
    sound3 = SoundFile(this,"pisk.mp3")
    sound4 = SoundFile(this,"kotudar.mp3")
    sound2.play()
    size(700,500)
def draw():
    global y , x , x2 , time , healh , inst , re , x3 , prozhealh, sound1 , sound2 , sound3 , sound4
    background(0,255,253)
    line(0,240,700,240)
    rectMode(CENTER)
    fill(0,112,121)
    rect(350,370,701,260)
    textSize(40)
    if keyPressed == True: 
        inst = 1 
        if key == 'W' or key == 'w' or key == u'ц' or key == u'Ц':
            y = y + 1
            x = x - 0.3
            x3 = x3 + 0.005
            if healh > -19 :
                if not sound1.isPlaying():
                    sound1.play()
                    sound1.play()
        if key == 'S' or key == 's' or key == u'ы' or key == u'Ы':
            y = y - 1
            x = x + 0.5
            x3 = x3 - 0.005
            if healh > -19 :
                if not sound1.isPlaying():
                    sound1.play()
                    sound1.play()
        if key == 'A' or key == 'a' or key == u'ф' or key == u'Ф':
            x2 = x2 + x3
            if healh > -19 :
                if not sound1.isPlaying():
                    sound1.play()
                    sound1.play()
        if key == 'D' or key == 'd' or key == u'в' or key == u'В':
            x2 = x2 - x3
            if healh > -19 :
                if not sound1.isPlaying():
                    sound1.play()
                    sound1.play()
        if key == 'R' or key == 'r' or key == u'к' or key == u'К':
            re = 1
        if key == ' ' :
            if healh > -19 :
                if not sound2.isPlaying():
                    sound2.play()
    #if mousePressed :
        
    if inst == 0 :
        fill(255,132,0,250)
        rect(350,250,700,500)
        fill(0)
        textSize(25)
        text(u"Управление:w a s d и мышкой.",10,60)
        text(u"Включить автовозрождение r учтите, что",10,90)
        text(u"автовозрождение снимается если ты уже его",10,110)
        text(u"испльзовал(-а).",10,130)
        fill(255)
        text(u"для входа в игру нажмите любую кнопку",10,495)
        y = 1
        x = 240
        x2 = 350
        time = 0
        healh = 90
        re = 0
        x3 = 0.2
    if y == 1 :
        x3 = 0.2
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
        if healh > -19 :
                    sound4.play()
        healh = healh - 1
    if x2 < -40 :
        if healh > -19 :
                    sound4.play()
        x2 = -38
        fill(220,0,0)
        rect(700,250,10,500)
        fill(255,0,0)
        text(u"вы врезались в барьер!",100,250)
        healh = healh - 1
    if y > 1400 :
        fill(255,0,0)
    if healh == 0 :
        prozhealh = 100
        if healh > -19 :
                if not sound3.isPlaying():
                    sound3.play()
    if healh == -10 :
        if healh > -19 :
                if not sound3.isPlaying():
                    sound3.play()
        prozhealh = 150
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
        textSize(20)
        text(u"нажмите r чтобы возродиться",20,270)
        sound3.stop()
        healh = -21
        x3 = 0.2
        prozhealh = 0
        if healh > -19 :
                if not sound4.isPlaying():
                    sound4.play()
        if re == 1 :
            y = 1
            x = 240
            x2 = 350
            time = 0
            healh = 90
            re = 0
    fill(0,100)
    textSize(15)
    text(time,650,15)
    fill(255,0,0,prozhealh)
    rect(-1,-1,702,502)
    time = time + 0.020
