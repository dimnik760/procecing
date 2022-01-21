x = 0
y = 200
z = -200
x2 = -0
y2 = 200
z2 = 200
def setup():
    size(600,400)
def draw():
    frameRate(60)
    global x
    global y
    global z
    global x2
    global y2
    #background(255)
    translate(300,0)
    rotate(radians(0))
    fill(random(255),random(255),random(255))
    ellipse(x,y2,random(100),random(100))
    fill(0, 255, 0)
    ellipse(random(5),200,10,10)
    #rotate(radians(60))
    fill(0,random(255),0)
    ellipse(x,y,random(100),random(100))
    ellipse(x2,y,random(100),random(100))
    fill(0)
    ellipse(x2,y2,random(100),random(100))
    x = x - 15
    if x >= 300+40:
        x = 0     
        
    y = y - 10  
    if y >= 450-40:     
        y = -300
        
    z = z - 10    
    if z >= 0-40:
        z = 0  
    x2 = x2 +15
    y2 = y2 +15
    
              
