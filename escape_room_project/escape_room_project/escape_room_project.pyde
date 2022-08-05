class GameData:
    
    def __init__(self):
        self.scene = "Room2Scene"
        
        # EMPTY, F_STATE, I_STATE, S_STATE, FINISHED
        self.passwordSceneState = "EMPTY"
    
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
    #room1
    global room1
    room1 = loadImage("./room1/room1.png")
    global letter
    letter = loadImage("./room1/letter.png")
    global prologue
    prologue = loadImage("./intro/prologue.png")
    #passwordscene
    global PasswordScene
    PasswordScene = loadImage("./room_password/PasswordScene.png")
    global fInserted
    fInserted = loadImage("./room_password/fInserted.png")
    global iInserted
    iInserted = loadImage("./room_password/iInserted.png")
    global sInserted
    sInserted = loadImage("./room_password/sInserted.png")
    global hInserted
    hInserted = loadImage("./room_password/hInserted.png")
    #room2
    global room2
    room2 = loadImage("./room2/room2.png")
    global hanja
    hanja = loadImage("./room2/hanja.png")
    global pokemon
    pokemon = loadImage("./room2/pokemon.png")
    global graph
    graph = loadImage("./room2/graph.png")
    

    
def calculateLineEquation(x1, y1, x2, y2):
    
    slope = float(y2 - y1) / float(x2 - x1)
    intercept = y1 - (float(y2 - y1) / float(x2 - x1)) * x1
    
    return (slope, intercept)
    
def detectAreaWithCoordinates(x1, y1, x2, y2, x3, y3, x4, y4, a, b):
    
    line1_slope = calculateLineEquation(x1, y1, x2, y2)[0]
    line1_intercept = calculateLineEquation(x1, y1, x2, y2)[1]
    
    line2_slope = calculateLineEquation(x2, y2, x3, y3)[0]
    line2_intercept = calculateLineEquation(x2, y2, x3, y3)[1]
    
    line3_slope = calculateLineEquation(x3, y3, x4, y4)[0]
    line3_intercept = calculateLineEquation(x3, y3, x4, y4)[1]
    
    line4_slope = calculateLineEquation(x4, y4, x1, y1)[0]
    line4_intercept = calculateLineEquation(x4, y4, x1, y1)[1]
    
    condition1 = True if (b > line1_slope * a + line1_intercept) else False
    if (line2_slope > 0):
        condition2 = True if (b > line2_slope * a + line2_intercept) else False
    else:
        condition2 = True if (b < line2_slope * a + line2_intercept) else False
    condition3 = True if (b < line3_slope * a + line3_intercept) else False
    if (line4_slope > 0):
        condition4 = True if (b < line4_slope * a + line4_intercept) else False
    else:
        condition4 = True if (b > line4_slope * a + line4_intercept) else False
    
    return condition1 and condition2 and condition3 and condition4    

def draw():
            
    if gameData.scene == "MainScene":
        drawMainScene()
    elif gameData.scene == "IntroScene":
        drawIntroScene()
    elif gameData.scene == "PrologueScene":
        drawPrologueScene()
    elif gameData.scene == "Room1Scene" :
        drawRoom1Scene()
    elif gameData.scene == "PasswordScene":
        drawPasswordScene()
    elif gameData.scene == "Room2Scene":
        drawRoom2Scene()
        
    
def drawMainScene():

    image(main_img, 0, 0, 1200, 800)
    textFont(font, 50)
    text("", 10, 50)
    image(start_button, 450, 380, 300, 100)
    image(load_button, 450, 500, 300, 100)
    image(exit_button, 450, 650, 300, 100)
    image(title, 250, 70, 700, 250)
    image(jessica, 1080, 150, 180, 660)

    # print(gameData.scene)
    
def drawIntroScene():
    image(pasta_resto, 0, 0, 1200, 800)


def drawPrologueScene():
    image(prologue, 0, 0, 1200, 800)
    
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
    elif gameData.scene == "Room1Scene" and (detectAreaWithCoordinates(335, 307, 443, 374, 425, 462, 314, 396,  mouseX, mouseY)) == True:
         gameData.scene = "PasswordScene"
    elif gameData.scene == "PasswordScene":
         gameData.scene = "Room2Scene"
    elif gameData.scene == "PasswordScene":
        if gameData.passwordSceneState == 'FINISHED' and detectAreaWithCoordinates(872, 382, 1142, 375, 1142, 480, 872, 486, mouseX, mouseY):
            gameData.scene == "Room2Scene"


def drawRoom1Scene():
    textSize(32)
    fill(90, 80, 80)
    
    image(room1, 0, 0, 1200, 800)
    
    # print("x: " + str(mouseX) + " y: " + str(mouseY))
        
    if (detectAreaWithCoordinates(335, 307, 443, 374, 425, 462, 314, 396,  mouseX, mouseY)):
        text("go to the sea", 990, 10, 1200, 300)
    else:
        cursor(ARROW)
    if (detectAreaWithCoordinates(106, 63, 330, 107, 298, 254, 78, 203, mouseX, mouseY)):
        image(letter, 0, 0, 1200, 800)
     

def keyPressed():
    
    if gameData.scene == "MainScene":
         pass
    elif gameData.scene == "IntroScene":
         pass
    elif gameData.scene == "PrologueScene":
         pass
    elif gameData.scene == "Room1Scene":
         pass
    elif gameData.scene == "PasswordScene":
        if gameData.passwordSceneState == 'EMPTY' and key =='f': 
            gameData.passwordSceneState  = 'F_STATE'
        elif gameData.passwordSceneState  == 'F_STATE' and key == 'i':
            gameData.passwordSceneState  = 'I_STATE'
        elif gameData.passwordSceneState  == 'I_STATE' and key == 's':
            gameData.passwordSceneState  = 'S_STATE'
        elif gameData.passwordSceneState  == 'S_STATE' and key == 'h':
            gameData.passwordSceneState  = 'FINISHED'
        




def drawPasswordScene():
    image(PasswordScene, 0, 0, 1200, 800)
    textSize(64)
    if gameData.passwordSceneState == 'F_STATE':
        image(fInserted, 0, 0, 1200, 800)
    if gameData.passwordSceneState == 'I_STATE':
        image(iInserted, 0, 0, 1200, 800)
    if gameData.passwordSceneState == 'S_STATE':
        image(sInserted, 0, 0, 1200, 800)
    if gameData.passwordSceneState == 'FINISHED':
        image(hInserted, 0, 0, 1200, 800)

    
    

                                                                                       
def drawRoom2Scene():
    
    image(room2, 0, 0, 1200, 800)
    

    print("x: " + str(mouseX) + " y: " + str(mouseY))
    if (detectAreaWithCoordinates(94, 129, 294, 188, 292, 339, 99, 351, mouseX, mouseY)):
        image(hanja, 0, 0, 1200, 800)
    if (detectAreaWithCoordinates(375, 190, 540, 228, 536, 325, 370, 334, mouseX, mouseY)):
        image(graph, 0, 0, 1200, 800)
    if (detectAreaWithCoordinates(592, 243, 694, 269, 694, 328, 590, 335, mouseX, mouseY)):
        image(pokemon, 0, 0, 1200, 800)
    
    






      

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
                

        
        
    
