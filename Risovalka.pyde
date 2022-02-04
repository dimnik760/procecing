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
    fill(250)
    textSize(15)
    text(u"ластик",0,18)
    fill(255,0,0)
    rect(60,0,50,30)
    #рисовалка
    global run
    global bg
    global chot , hot
    strokeWeight(4)
    
    if mousePressed:
        if mouseButton == LEFT:
            stroke(255,0,0) 
        elif mouseButton == CENTER:
            if hot > 1 :
              background(255)   
              stroke(255,255,255)
              fill(255)
              rect(0,0,50,30)     
        else:
            fill(0)
        if mouseY < 60: 
            noStroke()
        line(mouseX,mouseY,pmouseX,pmouseY)
                  
def mouseClicked():
#кнопки    
    global bg , hot
    
    if mouseX > 0 and mouseX <50 and mouseY < 30 and mouseY > 0:
        background(255)   
        stroke(255,255,255)
        fill(hot)
        rect(0,0,50,30) 
        
    if mouseX > 60 and mouseX <110 and mouseY < 30 and mouseY > 0:#красная кнопка
        background(255)   
        stroke(255,255,255)
        fill(chot)
        rect(60,0,50,30) 
