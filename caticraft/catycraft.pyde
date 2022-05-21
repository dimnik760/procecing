add_library('sound')
play = 0
c = 500
y = 1
ybox = 240
x2 = 350
x3 = 0.2
time = 0
healh = 90
inst = 0
re = 0
y2 = 0
jamp = 0
prozhealh = 0
gren = 0
fil = 1
sound1 = 0
sound2 = 0
sound3 = 0
sound4 = 0
sound5 = 0
img = 0
Yrect = 240
zbox = 0
mousey = 0
mousex = 0
volume = 1.00
setings = 0
sound = 0
def setup():
    global sound1 , sound2 , sound3 , sound4 , img , sound5 , volume
    sound1 = SoundFile(this,"run1.mp3")
    sound2 = SoundFile(this,"jamp.mp3")
    sound3 = SoundFile(this,"pisk.mp3")
    sound4 = SoundFile(this,"kotudar.mp3")
    sound5 = SoundFile(this,"meow.mp3")
    sound5.play(1,0,volume)
    size(700,500,OPENGL)
    img = loadImage("cat.png")
def draw():
    global y , ybox , x2 , time , img , sound , setings , volume , healh , inst , re , x3 , prozhealh, sound1 , sound2 , sound3 , sound4 , y2 , jamp , c , gren , fil , play , sound5 , Yrect , zbox , mousex , mousey , volume 
    background(0,255,253)
    strokeWeight(1)
    rectMode(CORNER)
    fill(0,112,121)
    rect(0,Yrect,701,260)
    textSize(40)
    rectMode(CENTER)
    if keyPressed == True: 
        inst = 1 
        if key == 'W' or key == 'w' or key == u'ц' or key == u'Ц':
            y = y + 1
            ybox = ybox - 0.3
            x3 = x3 + 0.005
            zbox = zbox + 1
            if healh > -19 :
                if not sound1.isPlaying():
                    sound1.play(1,0,volume)
                    sound1.play(1,0,volume)
        if key == 'S' or key == 's' or key == u'ы' or key == u'Ы':
            y = y - 1
            ybox = ybox + 0.5
            x3 = x3 - 0.005
            zbox = zbox - 1
            if healh > -19 :
                if not sound1.isPlaying():
                    sound1.play(1,0,volume)
                    sound1.play(1,0,volume)
        if key == 'A' or key == 'a' or key == u'ф' or key == u'Ф':
            x2 = x2 + x3
            if healh > -19 :
                if not sound1.isPlaying():
                    sound1.play(1,0,volume)
                    sound1.play(1,0,volume)
        if key == 'D' or key == 'd' or key == u'в' or key == u'В':
            x2 = x2 - x3
            if healh > -19 :
                if not sound1.isPlaying():
                    sound1.play(1,0,volume)
                    sound1.play(1,0,volume)
        if key == 'R' or key == 'r' or key == u'к' or key == u'К':
            re = 1
        if key == ' ' :
            if jamp == 0 :
                jamp = 1
            #y2 = 1
            if healh > -19 :
                if not sound2.isPlaying():
                    sound2.play(1,0,volume)

                
    text(y,100,200)
    if y > 100 :
        y = 100
        ybox = ybox + 3
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
        ybox = 240
        x2 = 350
        time = 0
        healh = 90
        re = 0
        x3 = 0.2
    if y == 1 :
        x3 = 0.2
    if y == 0 :
       y = 1 
    if jamp == 0 :   
        if ybox > 240 :
            ybox = 240
    if x2 > 1000 :
        x2 = 738
        fill(220,0,0)
        rect(0,250,10,500)
        fill(255,0,0)
        text(u"вы врезались в барьер!",100,250)
        if healh > -19 :
                    sound4.play(1,0,volume)
        healh = healh - 1
    if x2 < -1000 :
        if healh > -19 :
                    sound4.play(1,0,volume)
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
                    sound3.play(1,0,volume)
    if healh == -10 :
        if healh > -19 :
                if not sound3.isPlaying():
                    sound3.play(1,0,volume)
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
        y = 1
        x = 240
        x2 = 350
        time = 0
        if healh > -19 :
                if not sound4.isPlaying():
                    sound4.play(1,0,volume)
        if re == 1 :
            y = 1
            ybox = 240
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
    if play == 0 :
        c = 500
        y = 1
        ybox = 240
        x2 = 350
        x3 = 0.2
        time = 0
        healh = 90
        inst = 0
        re = 0
        y2 = 0
        jamp = 0
        prozhealh = 0
        fill(0,gren,gren)
        rect(-1,-1,702,502)
        fill(0,0,255)
        textSize(100)
        text("catycraft",120,90)
        textSize(15)
        text(u"shadow барсик games",535,495)
        fill(138,0,209)
        textSize(25)
        rectMode(CORNER)
        rect(345,200,100,50)
        fill(138,0,209,100)
        rect(345,260,100,50)
        fill(0)
        text(u"играть",350,230)
        textSize(19)
        text(u"настройки",345,290)
        image(img, -70, 40)
        if mousePressed :
            if mouseX > 345 and mouseX < 445 and mouseY < 250 and mouseY > 200:
                play = 1
                rect(345,200,100,50)
            if mouseX > 1 and mouseX < 115 and mouseY < 495 and mouseY > 370:
                if not sound5.isPlaying():
                       sound5.play(1,0,volume)
    
            if mouseX > 345 and mouseX < 445 and mouseY < 310 and mouseY > 260:
                setings = 1
                
                rect(345,260,100,50)
    if fil == 1:
        gren = gren + 1
    elif fil == 0:
        gren = gren - 1
    if gren > 255:
        fil = 0
    if gren < 10:
        fil = 1
    if mousePressed :
        mousex  = mouseX 
        mousey = mouseY
        #rotateY(radians(mousex))
        
    fill(250)
    push()
    translate(x2,ybox)
    translate(0,0,zbox)
    fill(0,255,0)
    box(y,y,y)
    pop()
    if jamp == 1 :
        ybox = ybox + 2
    if jamp == 2:
        ybox = ybox - 2
    if ybox >= 300 :
        jamp = 2
    if ybox < 240:
        jamp = 0
    
    if jamp == 1 :
        Yrect = Yrect + 2
    if jamp == 2:
        Yrect = Yrect - 2
        
    if setings == 1 :
        fill(0)
        rect(0,0,700,500)
        textSize(15)
        fill(255)
        text(u"<-назад",15,20)
        textSize(20)
        fill(0,0,255)
        text(u"*****настройки*****",250,20)
        
        if mousePressed :
            if mouseX > 0 and mouseX < 80 and mouseY < 30 and mouseY > 0:
                setings = 0
                sound = 0
            if mouseX > 0 and mouseX < 300 and mouseY < 80 and mouseY > 45:
                sound = 1
                
        fill(50)
        rect(0,40,300,50)
        fill(255)
        text(u"настройки громкости звука",14,70)
        if sound == 1 :
            fill(0)
            rect(0,0,700,500)
            rect(0,40,300,50)
            textSize(15)
            fill(255)
            text(u"<-назад",15,20)
            text(volume,80,40)
            text("%",125,40)
            fill(100)
            rect(0,40,200,50)
            rect(280,40,200,50)
            fill(255)
            textSize(25)
            text(u"меньше(-)",15,75)
            text(u"больше(+)",300,75)
            if volume < 0.00 :
                volume = 0.001 
            if volume > 1.00 :
                 volume = 0.99
            if mousePressed :
                if mouseX > 0 and mouseX < 200 and mouseY < 90 and mouseY > 40:
                    volume = volume - 0.01
                    
                if mouseX > 280 and mouseX < 480 and mouseY < 80 and mouseY > 45:
                    volume = volume + 0.01
    textSize(15)
    fill(random(255),random(255),random(255))
    text("x=",190,20)
    text("y=",190,30)
    text(mouseX,210,20)
    text(mouseY,210,30)
