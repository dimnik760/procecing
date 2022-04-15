y = 475
y2 = 0
x = 25
img = 0
def setup():
    size(700,500)
    global img
    img = loadImage("plant.png")
def draw():
    global y , y2 , x 
    background(0,255,253)
    image(img, 0, 390)
    image(img, 200, 390)
    image(img, 350, 390)
    fill(0,255,0,200)
    ellipse(x,y,50,50)
    textSize(15)
    fill(0)
    text("x=",180,20)
    text("y=",180,40)
    text(mouseX,200,20)
    text(mouseY,200,40)
    fill(200)
    rect(100,450,50,50)
    if keyPressed == True and y2 == 0: 
        if key == ' ':
             y2 = 1
        if key == CODED:
            if keyCode == LEFT: 
                x = x - 5
            if keyCode == RIGHT: 
                x = x + 5
            if keyCode == UP:
                y2 = 1
            if keyCode == UP and keyCode == LEFT:
                y2 = 1
                x = x - 10
    if x >= 700 :
        x = 700
    if x >= 75 and y <= 449:
        x = 75
    if x <= -5 :
        x = -5
    if y2 > 0 :
        y = y - 10
    if y2  < 0 :
        y = y + 10
    if y2 != 0 :
        y2 = y2 + 1
    if y2 == 10:
        y2 = - 9
