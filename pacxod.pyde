x = 0
y = 200
z = -200
def setup():
    size(600,400)
def draw():
    global x
    global y
    global z
    background(255)
    translate(300,0)
    rotate(radians(0))
    fill(random(255),random(255),random(255))
    ellipse(x,200,50,50)
    fill(0, 255, 0)
    ellipse(random(5),200,10,10)
    #rotate(radians(90))
    fill(0,random(255),0)
    ellipse(0,y,50,50)
    ellipse(z,0,50,50)
    x = x - 15
    if x >= 300+40:
        x = 0      
    y = y - 10  
    
    if y >= 450-40:     
        y = 200
    z = z - 10    
    if z >= 0-40:
        z = 0   
        
        
