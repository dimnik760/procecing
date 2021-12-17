x = -300
y = 300
def setup():
    size(600,400)
def draw():
    global y
    global x 
    background(100)
    translate(300,200)
    fill(255,255,random(250))
    ellipse(0,x,80,80)
    x = x + 4
    if y >= 300:
        y = y - 4
        
