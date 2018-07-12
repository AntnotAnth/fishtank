def setup():
    size(400, 400)
    background(random(255), random(255), random(255))
    #fish(50, 90, 30, 20)    # x=50 , y= 90
    #fishtail(65, 90, 90, 70, 90, 105)
    fish1(350, 70)
    fish1(200, 50)
    #fish2(150, 110)
    fish1(240, 220)
     
def fish(xCoordinate, yCoordinate, fishWidth, fishHeight):
    setColor( "green") 
    ellipse(xCoordinate, yCoordinate, fishWidth, fishHeight)
def fishtail(x1, y1, x2, y2, x3, y3):
    setColor ("blue")
    triangle(x1, y1, x2, y2, x3, y3)

def fish1(x1, y1): #x1= 65 , x2= 90, x3= 90, y1= 90, y2=70, y3= 105
    fish(x1, y1, 30, 20)
    fishtail(x1+15, y1, x1+25, y1-20, x1+25, y1+15)

#def fish2(x1, y1):
    #fish(x1, y1, 30, 20)
    #fishtail(x1+20, y1-20, x1+10, y1-20, x1+20, y1+ 15) 
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
def setColor (colorName):    
    if colorName == "blue":
       fill(0, 0, 255)
    elif colorName == "red":
       fill(255, 0, 0)
    elif colorName == "green":
       fill(0, 255, 0)
