bg = 0;
run = 0
chot = 0
hot = 0
def setup():
    size(600,400)
def draw():
    global run
    global bg
    global chot , hot
    background(bg)
    #кнопка прямоугольная
    fill(255)
    ellipse(400,350,70,70)
    rect(run,150,100,50) # x от 250 до 250+100, y от 150 до 150 + 50  
    fill(0)
    textSize(50)
    if hot > 50 :
        text(u"вы выиграли",200,300)
    textSize(15)
    text(u"обнулить",366,354)
    textSize(30)
    fill(128, 0, 128)
    text(hot,10,30)
    text(chot*random(2,500),-50,60)
    text(chot*random(2,500),-50,90)
    text(chot*random(2,500),-50,120)
    text(chot*random(2,500),-50,153)
    text(chot*random(2,500),-50,150)
    text(chot*random(2,500),-50,160)
    fill(255)
    run = run + 0.1
    if run >= 600:
        run = 0 
    chot = chot +100000000000000000000988000000000000
def mouseClicked():
    
    global bg , hot
    # если прямоугольная кнопка нажата
    
    if mouseX > run and mouseX < run+100 and mouseY > 150 and mouseY < 200:
        bg = 255
        hot = hot + 1
        
    #если круглая кнопка нажата
    xDif = 400 - mouseX
    yDif = 350 - mouseY
    if sqrt(xDif*xDif + yDif*yDif) < 35:
        bg = 0
        hot = 0
