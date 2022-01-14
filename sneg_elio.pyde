x = -300
y = 300
def setup():
    size(600,400)
def draw():
    global y
    global x 
    background(100)
    translate(300,200)
    fill(random(220,255))
    ellipse(random(-300,300),y-random(-300,800),10,10)
    ellipse(random(-300,300),y-random(-300,400),10,10)
    ellipse(random(-300,300),y-random(-300,400),10,10)
    ellipse(random(-300,300),y-random(-300,400),10,10)
    ellipse(random(-300,300),y-random(-300,400),10,10)
    ellipse(random(-300,300),y-random(-300,400),10,10)
    ellipse(random(-300,300),y-random(-100,200),10,10)
    ellipse(random(-300,300),y-random(-100,200),10,10)
    ellipse(random(-300,300),y-random(-100,200),10,10)
    ellipse(random(-300,300),y-random(-100,200),10,10)
    translate(0,60)
    fill(0, 100, 0)
    triangle(-50,-80,30,-80,-10,-150)
    translate(0,70) 
    triangle(-90,-80,80,-80,-10,-150)
    translate(0,70)
    triangle(-110,-80,100,-80,-10,-150)
    fill(139, 69, 19)
    translate(300,200)
    rect(-300,-200,-20,-80)
    
    y = y + 1
    if y >= 300:
        y = -300
