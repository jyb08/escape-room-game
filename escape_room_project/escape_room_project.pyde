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


def draw():
    

    
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
        
        
        
        
    
