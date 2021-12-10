sizeEl = 900
mode = "вправо"
def setup():
    size(600,400)
    background(255)
def draw():
    global sizeEl
    global sizeEl
    global mode
    translate(300,200)
    ellipse(0,0,sizeEl,sizeEl)
    sizeEl = sizeEl - 1 
    if mode == "вправо": 
        sizeEl = sizeEl + 20
    if mode == "left":
        sizeEl = sizeEl - 20
    if sizeEl >= 600:
        mode = "left"  
    if sizeEl <= 0:
        mode = "вправо"      
    
