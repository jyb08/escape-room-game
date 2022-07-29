class GameData:
    
    def __init__(self):
        self.scene = "MainScene"
    
    
gameData = GameData()


def setup():
    size(1200, 800)
    
    #main:
    global main_img
    main_img = loadImage("./main/main_img.png")
    global font
    font = createFont("arial", 16)
    global start_button
    start_button = loadImage("./main/start_button.png")
    global load_button
    load_button = loadImage("./main/load_button.png")
    global exit_button
    exit_button = loadImage("./main/exit_button.png")
    global title
    title = loadImage("./main/title.png")
    global jessica
    jessica = loadImage("./main/jessica.png")
    #intro
    global pasta_resto
    pasta_resto = loadImage("./intro/pasta_resto.png")
    global room1
    room1 = loadImage("./room1/room1.png")
    global prologue
    prologue = loadImage("./intro/prologue.png")
    
    
def calculateLineEquation(x1, y1, x2, y2):
    
    slope = (y2 - y1) / (x2 - x1)
    intercept = y1 - (y2 - y1) / (x2 - x1) * x1
    
    return (slope, intercept)
    

def detectAreaWithCoordinates(x1, y1, x2, y2, x3, y3, x4, y4, a, b):
    # Upper Left x1, y1
    # Upper Right x2, y2
    # Lower Right x3, y3
    # Lower left x4, y4
    
    line1_slope = calculateLineEquation(x1, y1, x2, y2)[0]
    line1_intercept = calculateLineEquation(x1, y1, x2, y2)[1]
    
    line2_slope = calculateLineEquation(x2, y2, x3, y3)[0]
    line2_intercept = calculateLineEquation(x2, y2, x3, y3)[1]
    
    line3_slope = calculateLineEquation(x3, y3, x4, y4)[0]
    line3_intercept = calculateLineEquation(x3, y3, x4, y4)[1]
    
    line4_slope = calculateLineEquation(x4, y4, x1, y1)[0]
    line4_intercept = calculateLineEquation(x4, y4, x1, y1)[1]
    
    condition1 = True if (b > line1_slope * a + line1_intercept) else False
    if (line2_slope < 0):
        condition2 = True if (b < line2_slope * a + line2_intercept) else False
    else:
        condition2 = True if (b > line2_slope * a + line2_intercept) else False
    condition3 = True if (b < line3_slope * a + line3_intercept) else False
    if (line4_slope < 0):
        condition4 = True if (b > line4_slope * a + line4_intercept) else False
    else:
        condition4 = True if (b < line4_slope * a + line4_intercept) else False
    
    print("condition1: " + str(condition1))
    print("condition2: " + str(condition2))
    print("condition3: " + str(condition3))
    print("condition4: " + str(condition4))
    
    return condition1 and condition2 and condition3 and condition4    

def draw():
    print("x: " + str(mouseX) + " y: " + str(mouseY))
    print(detectAreaWithCoordinates(335, 307, 443, 374, 314, 396, 425, 462, mouseX, mouseY))
    
    if gameData.scene == "MainScene":
        drawMainScene()
    elif gameData.scene == "IntroScene":
        drawIntroScene()
    elif gameData.scene == "PrologueScene":
        drawPrologueScene()
    elif gameData.scene == "Room1Scene":
        drawRoom1Scene()
    
def drawMainScene():

    image(main_img, 0, 0, 1200, 800)
    textFont(font, 50)
    text("", 10, 50)
    image(start_button, 450, 380, 300, 100)
    image(load_button, 450, 500, 300, 100)
    image(exit_button, 450, 650, 300, 100)
    image(title, 250, 70, 700, 250)
    image(jessica, 1080, 150, 180, 660)



    
    print(gameData.scene)
    
def drawIntroScene():
    image(pasta_resto, 0, 0, 1200, 800)


def drawPrologueScene():
    image(prologue, 0, 0, 1200, 800)
    
def drawRoom1Scene():
    image(room1, 0, 0, 1200, 800)

    

    
    
def mouseClicked():
    if gameData.scene == "MainScene":
        if mouseX in range (450, 750) and mouseY in range (380, 480):
            print("Start Button Clicked")
            gameData.scene = "IntroScene"
        if mouseX in range (450, 750) and mouseY in range (500, 600):
            print("Load Button Clicked")
        if mouseX in range (450, 750) and mouseY in range (650, 750):
            print("Exit Button Clicked")
            exit()
    elif gameData.scene == "IntroScene":
        gameData.scene = "PrologueScene"
    elif gameData.scene == "PrologueScene":
        gameData.scene = "Room1Scene"
        
        
        
        
    
