class GameData:
    
    def __init__(self):
        self.scene = "Password3Scene"
        
        # EMPTY, F_STATE, I_STATE, S_STATE, FINISHED
        self.passwordSceneState = "EMPTY"
        self.passwordSceneStateForGameover = 0
        self.passwordScene2StateForGameover = 0
        self.passwordScene2State = "DEFAULT"
        
        
        self.passwordScene3StateForPlayer = ""
        self.passwordScene3StateForComputer = ""
    
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
    global game_over
    game_over = loadImage("./main/game_over.png")
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
    global letter2
    letter2 = loadImage("./room2/letter2.png")

    global default 
    default = loadImage("./room2/default.png")
    #room2_password
    global one 
    one = loadImage("./room2_password/one.png")
    global two 
    two = loadImage("./room2_password/two.png")
    global three 
    three = loadImage("./room2_password/three.png")
    global four 
    four = loadImage("./room2_password/four.png")
    global room2_4_psw 
    room2_4_psw  = loadImage("./room2_password/room2_4_psw.png")
    global default_4_pw
    default_4_pw  = loadImage("./room2_password/default_4_pw.png")
    global room3
    room3  = loadImage("./room3/room3.jpg")
    global room3_password
    room3_password  = loadImage("./room3_password/room3_password.jpg")
    global rock
    rock  = loadImage("./room3_password/rock.png")
    global paper
    paper  = loadImage("./room3_password/paper.png")
    global scissors
    scissors  = loadImage("./room3_password/scissors.png")
    global rock_selected
    rock_selected  = loadImage("./room3_password/rock_selected.png")
    global paper_selected
    paper_selected  = loadImage("./room3_password/paper_selected.png")
    global scissors_selected
    scissors_selected  = loadImage("./room3_password/scissors_selected.png")

    
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
    elif gameData.scene == "Password2Scene":
        drawPassword2Scene()
    elif gameData.scene == "Room3Scene":
        drawRoom3Scene()
    elif gameData.scene == "Password3Scene":
        drawPassword3Scene()
    elif gameData.scene == "GameOverScene":
        drawGameOverScene()

        
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
        if gameData.passwordSceneState == 'FINISHED' and detectAreaWithCoordinates(872, 382, 1142, 375, 1141, 480, 871, 486, mouseX, mouseY):
            gameData.scene = "Room2Scene"
    elif gameData.scene == "Room2Scene" and (detectAreaWithCoordinates(950, 372, 971, 373, 972, 409, 951, 414, mouseX, mouseY)) == True:
         gameData.scene = "Password2Scene"
    # elif gameData.scene == "Password2Scene":
    #      gameData.scene = "Room3Scene"
    elif gameData.scene == "Password2Scene":
        if gameData.passwordScene2State == 'FOUR' and (detectAreaWithCoordinates(885, 367, 1085, 358, 1089, 431, 887, 425,  mouseX, mouseY)) == True:
            gameData.scene = "Room3Scene"
    elif gameData.scene == "Room3Scene":
        gameData.scene = "Password3Scene"
    elif gameData.scene == "Password3Scene":
        if detectCircle(135, 690, 60, mouseX, mouseY) == True:
            gameData.passwordScene3StateForPlayer = 'rock'
        if detectCircle(285, 690, 60, mouseX, mouseY) == True:
            gameData.passwordScene3StateForPlayer = 'scissors' 
    elif gameData.scene == "GameOverScene":
         gameData.scene = "MainScene"

def drawRoom1Scene():
    textSize(32)
    fill(90, 80, 80)
    
    image(room1, 0, 0, 1200, 800)
    
        
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
        gameData.passwordSceneStateForGameover += 1
        if gameData.passwordSceneState == 'EMPTY' and key =='f': 
            gameData.passwordSceneState  = 'F_STATE'
        elif gameData.passwordSceneState  == 'F_STATE' and key == 'i':
            gameData.passwordSceneState  = 'I_STATE'
        elif gameData.passwordSceneState  == 'I_STATE' and key == 's':
            gameData.passwordSceneState  = 'S_STATE'
        elif gameData.passwordSceneState  == 'S_STATE' and key == 'h':
            gameData.passwordSceneState  = 'FINISHED'
    elif gameData.scene == "Room2Scene":
        pass
    elif gameData.scene == "Password2Scene":
        gameData.passwordScene2StateForGameover += 1
        if gameData.passwordScene2State == 'DEFAULT' and key =='1': 
            gameData.passwordScene2State  = 'ONE'
        elif gameData.passwordScene2State == 'ONE' and key == '3':
            gameData.passwordScene2State  = 'TWO'
        elif gameData.passwordScene2State == 'TWO' and key == '4':
            gameData.passwordScene2State  = 'THREE'
        elif gameData.passwordScene2State == 'THREE' and key == '2':
            gameData.passwordScene2State  = 'FOUR'
    elif gameData.scene == "Room3Scene":
        pass
    elif gameData.scene == "Password3Scene":
        pass

def drawGameOverScene():
    image(game_over, 0, 0, 1200, 800)
    

def drawPasswordScene():
    

    image(PasswordScene, 0, 0, 1200, 800)
    textSize(64)
    if gameData.passwordSceneStateForGameover > 10:
        gameData.passwordSceneStateForGameover = 0
        gameData.scene = "GameOverScene"
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
    
    # print("x: " + str(mouseX) + " y: " + str(mouseY))
    if (detectAreaWithCoordinates(94, 129, 294, 188, 292, 339, 99, 351, mouseX, mouseY)):
        image(hanja, width/2 - 200, height/2 - 200, 400, 400)
    elif (detectAreaWithCoordinates(375, 190, 540, 228, 536, 325, 370, 334, mouseX, mouseY)):
        image(graph, width/2 - 300, height/2 - 300, 600, 600)
    elif (detectAreaWithCoordinates(592, 243, 694, 269, 693, 328, 590, 335, mouseX, mouseY)):
        image(pokemon, width/2 - 200, height/2 - 200, 400, 400)
    elif (detectAreaWithCoordinates(400, 471, 623, 605, 618, 624, 394, 591, mouseX, mouseY)):
        image(letter2, 0, 0, 1200, 800)
    # elif (detectAreaWithCoordinates(950, 372, 971, 373, 972, 409, 951, 414, mouseX, mouseY)):
    #     image(default, width/2 - 400, height/2 - 300, 800, 600)    
    

def drawPassword2Scene():
    image(default_4_pw, 100, 95, 1000, 605)
    if gameData.passwordScene2StateForGameover > 10:
        gameData.passwordScene2StateForGameover = 0
        gameData.scene = "GameOverScene"
    if gameData.passwordScene2State == 'ONE':
        image(one, 100, 95, 1000, 605)
    elif gameData.passwordScene2State == 'TWO':
        image(two, 100, 95, 1000, 605)
    elif gameData.passwordScene2State == 'THREE':
        image(three, 100, 95, 1000, 605)
    elif gameData.passwordScene2State == 'FOUR':
        image(four, 100, 95, 1000, 605)
        
    print("x:" + str(mouseX) + "y:"+ str(mouseY))
        
#backgroun info, cartoon version
        
def drawRoom3Scene():
    image(room3, 0, 0, 1200, 800)
    print("x:" + str(mouseX) + "y:"+ str(mouseY))
    
#explain the rules + play button




def findDistance(c1, c2, a, b):
    distance = sqrt(sq(b - c2) - sq(a - c1))
    return (distance)
    
def detectCircle(c1, c2, r, a, b):
    if r < findDistance(c1, c2, a, b):
        return(False)
    if r > findDistance(c1, c2, a, b):
        return(True)
    
    

def rockPaperScissors():
    if gameData.passwordScene3StateForPlayer == 'scissors' and gameData.passwordScene3StateForComputer == 'rock':
        return("CW")
    if gameData.passwordScene3StateForPlayer == 'scissors' and gameData.passwordScene3StateForComputer == 'paper':
        return("PW")
    if gameData.passwordScene3StateForPlayer == 'rock' and gameData.passwordScene3StateForComputer == 'rock':
        return("D")
    if gameData.passwordScene3StateForPlayer == 'rock' and gameData.passwordScene3StateForComputer == 'paper':
        return("CW")
    

    
def drawPassword3Scene():
    image(room3_password, 0, 0, 1200, 800)
    image(rock, 730, 110, 120, 120)
    image(paper, 880, 110, 120, 120)
    image(scissors, 1030, 110, 120, 120)
    image(rock, 80, 640, 120, 120)
    image(scissors, 230, 640, 120, 120)


    if gameData.passwordScene3StateForPlayer == 'scissors':
        image(scissors_selected, 230, 640, 120, 120)
    if gameData.passwordScene3StateForPlayer == 'rock':
        image(rock_selected, 80, 640, 120, 120)
    
    
    print(gameData.passwordScene3StateForPlayer)
    
    
    
    
    
    
    
    
    
    
    
    

    
                

        
        
    
