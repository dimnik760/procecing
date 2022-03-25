y = 1
x = 240
x2 = 350
time = 0
def setup():
    size(700,500)
def draw():
    global y , x , x2 , time
    background(0,255,253)
    line(0,240,700,240)
    rectMode(CENTER)
    fill(0)
    textSize(15)
    text(time,675,15)
    textSize(40)
    if keyPressed == True: 
        if key == 'W' or key == 'w' or key == u'ц' or key == u'Ц':
            y = y + 1
            x = x - 0.3
        if key == 'S' or key == 's' or key == u'ы' or key == u'Ы':
            y = y - 1
            x = x + 0.5
        if key == 'A' or key == 'a' or key == u'ф' or key == u'Ф':
            x2 = x2 - 0.4
        if key == 'D' or key == 'd' or key == u'в' or key == u'В':
            x2 = x2 + 0.4
   # if mousePressed :
    
    if y == 0 :
       y = 1 
        
    if x > 240 :
        x = 240
        fill(255,0,0)
    fill(250)
    rect(x2,x,y,y)
    if y > 1400 :
        fill(255,0,0)
        text(u"вы врезались!",100,250)
    time = time + 0.020
