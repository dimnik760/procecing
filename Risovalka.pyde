bg = 0;
run = 0
chot = 0
hot = 0
def setup():
    size(600,400)
    background(255)
    fill(255)
    rect(0,0,50,30)
    fill(250)
    textSize(15)
    text(u"ластик",0,16)
def draw():
    fill(200)
    textSize(13)
    text(u"cтереть",1,18)
    fill(255,0,0)
    rect(60,0,50,30)
    fill(0)
    rect(0,58,600,3)
    fill(0,255,0)
    rect(120,0,50,30)
    fill(0,0,255)
    rect(180,0,50,30)
                        #рисовалка
    global run
    global bg
    global chot , hot
    strokeWeight(4)
    
    if mousePressed:
        if mouseButton == LEFT:
            if hot > 1 :
              background(255)   
              stroke(255,255,255)
              if bg < 1: 
                fill(255)
                rect(0,0,50,30) 
              if run > 1: 
                stroke(0,255,0)
                rect(0,0,50,30)      
        else:
            fill(0)
        if mouseY < 60: 
            noStroke()
        line(mouseX,mouseY,pmouseX,pmouseY)
                  
def mouseClicked():
#кнопки    
    global bg , hot , run , chot
    
    if mouseX > 0 and mouseX <50 and mouseY < 30 and mouseY > 0:
        background(255)   
        stroke(255,255,255)
        fill(hot)
        rect(0,0,50,30) 
        
    if mouseX > 60 and mouseX <110 and mouseY < 30 and mouseY > 0:#красная кнопка
        stroke(255,0,0)   
        rect(60,0,50,30)
        bg = bg + 1
    if mouseX > 120 and mouseX <170 and mouseY < 30 and mouseY > 0:#красная кнопка
        stroke(0,255,0)   
        rect(120,0,50,30)
        run = run + 1    
    if mouseX > 180 and mouseX <230 and mouseY < 30 and mouseY > 0:#красная кнопка
        stroke(0,0,255)   
        rect(180,0,50,30)
        chot = chot + 1        
