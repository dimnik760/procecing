def setup():
    size(600,400)
    background(255)
def draw():
    strokeWeight(4)
    if mousePressed:
        if mouseButton == LEFT:
            stroke(255,0,0) 
        elif mouseButton == RIGHT:
              stroke(0,255,0)
        elif mouseButton == CENTER:
              strokeWeight(1000)   
              stroke(255,255,255)
        else:
            fill(0)
        line(mouseX,mouseY,pmouseX,pmouseY)          
