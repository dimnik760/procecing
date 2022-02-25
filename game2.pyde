bg = 0
run = 0
chot = 0
hot = 0
perem = 0
minis = 100
xy = 0
y = 300
def setup():
    size(600,400)
def draw():
    global run
    global bg
    global chot , hot , perem , minis , xy , y
    background(255,145,0)
    #кнопка прямоугольная
    fill(0,255,255)
    ellipse(400,350,70,70)
    fill(5,perem,10)
    rect(run,150,100,50) # x от 250 до 250+100, y от 150 до 150 + 50  
    fill(0)
    textSize(50)
    if hot > 15 :
        text(u"вы выиграли",300,200)
    textSize(15)
    text(u"обнулить",366,354)
    textSize(30)
    fill(128, 0, 128)
    text(hot,10,30)
    fill(255)
    run = run + 1.1
    if run >= 600:
        run = 0 
    fill(200)
    ellipse(300,350,70,70) 
    fill(0)
    textSize(10)
    text(u"цвет шрифта",268,345) 
    text(u"счётчика:",266,354) 
    text(u"оранжевый",269,362) 
    fill(0,255,0)
    ellipse(300,200,xy,xy)
    if hot >= 15:
        xy = xy + 10 
    fill(0,255,255)
    ellipse(400,350,70,70)    
    fill(0)
    textSize(15)
    text(u"обнулить",366,354)
    fill(random(100,255),random(100,255),0)
    textSize(80)
    if xy > 100 :
        text(u"вы выиграли",70,200)
    if hot >= 15:
       run = 250 
    if hot >= 15:
        fill(random(255),random(255),random(255))
        #rotate(radians(30))
        ellipse(xy,200,150,150) 
    if hot >= 15:
        ellipse(random(-300,300),y-random(-100,200),10,10) 
        y = y + 5 
        if y >= 300:
          y = -300       
    
def mouseClicked():
    
    global bg , hot , perem , minis , xy
    # если прямоугольная кнопка нажата
    
    if mouseX > run and mouseX < run+100 and mouseY > 150 and mouseY < 200:
        bg = 255
        hot = hot + 1
        perem = perem + 20
    #если круглая кнопка нажата
    xDif = 400 - mouseX
    yDif = 350 - mouseY
    if sqrt(xDif*xDif + yDif*yDif) < 35:
        bg = 0
        hot = 0
        perem = 0
        xy = 0
    xDif = 300 - mouseX
    yDif = 350 - mouseY
    fill(0)
    ellipse(300,350,70,70)
    if sqrt(xDif*xDif + yDif*yDif) < 35: 
        minis  = 50
