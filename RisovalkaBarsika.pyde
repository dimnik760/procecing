bg = 0;
run = 0
chot = 0
hot = 0
f = 0
klon = 4
black = 0
orange = 0
def setup():
    size(800,600)
    background(255)
    fill(255)
    rect(0,0,50,30)
    fill(250)
    textSize(15)
    text(u"ластик",0,16)
def draw():
    fill(200)
    textSize(13)
    text(u"cтереть",2,18)
    fill(255,0,0)
    textSize(20)
    text(u"\+/    \-/",310,48)
    #stroke(0)
    strokeWeight(1)
    fill(255,0,0)
    rect(60,0,50,30)
    fill(0)
    rect(0,58,800,3)
    fill(0,255,0)
    rect(120,0,50,30)
    fill(0,0,255)
    rect(180,0,50,30)
    fill(180)
    rect(240,0,50,30)
    fill(random(50,250),random(50,250),random(50,250))
    rect(300,0,50,30)
    rect(360,0,50,30)
    fill(0)
    rect(420,0,50,30)
    fill(250, 69, 0)
    rect(480,0,50,30)
                        #рисовалка
    global chot , hot , klon , black , bg , run , orange
    strokeWeight(4)
    if mousePressed:
        if mouseButton == LEFT:
            if hot > 1 :
              background(255)   
              stroke(255,255,255)
              if bg < 1: 
                fill(255)
                #rect(0,0,50,30) 
              if run > 1: 
                stroke(0,255,0)
                #rect(0,0,50,30)
              if f > 1:
                stroke(255)
                #rect(240,0,50,30)
              if black > 1:
                stroke(0)    
              if orange > 1:
                stroke(250, 69, 0)         
        else:
            fill(0)
        if mouseY < 60: 
            noStroke()
        strokeWeight(klon)    
        line(mouseX,mouseY,pmouseX,pmouseY)
def mouseClicked():
#кнопки    
    global bg , hot , run , chot , f , klon , black , orange
    if mouseX > 0 and mouseX <50 and mouseY < 30 and mouseY > 0:
        background(255)   
        stroke(255,255,255)
        fill(hot)
        #rect(0,0,50,30) 
    if mouseX > 60 and mouseX <110 and mouseY < 30 and mouseY > 0:#красная кнопка
        stroke(255,0,0)   
        #rect(60,0,50,30)
        bg = bg + 1
    if mouseX > 120 and mouseX <170 and mouseY < 30 and mouseY > 0:#красная кнопка
        stroke(0,255,0)   
        #rect(120,0,50,30)
        run = run + 1    
    if mouseX > 180 and mouseX <230 and mouseY < 30 and mouseY > 0:#красная кнопка
        stroke(0,0,255)   
        #rect(180,0,50,30)
        chot = chot + 1        
    if mouseX > 240 and mouseX <290 and mouseY < 30 and mouseY > 0:#красная кнопка
        stroke(255)   
        #rect(240,0,50,30)
        f = f + 1 
    if mouseX > 300 and mouseX <350 and mouseY < 30 and mouseY > 0:#красная кнопка
        stroke(255)   
        #rect(300,0,50,30)
        klon = klon + 1    
    if mouseX > 350 and mouseX <410 and mouseY < 30 and mouseY > 0:#красная кнопка
        stroke(255)   
        #rect(360,0,50,30)
        klon = klon - 1       
    if mouseX > 420 and mouseX <470 and mouseY < 30 and mouseY > 0:#красная кнопка
        stroke(0) 
        #rect(420,0,50,30)
        black = black + 1     
    if mouseX > 480 and mouseX <530 and mouseY < 30 and mouseY > 0:#красная кнопка
        stroke(250, 69, 0) 
        #rect(480,0,50,30)
        orange = orange + 1         
