# Filename: pythonGameConnect4.py
# Author: Constantinos Giannaras
# Date Created: May 18, 2022
# Description: Displays two screens: 
#                          1) Rules screen & press (S) to start
#                          2) Game screen (Connect 4)

# ----- 1) Import & init commands --------------------------------------------
import pygame, sys, time
pygame.init()

# ----- 2) Definitions: Classes, Constants and Variables--------------------------
# Classes: <none>

# Constants: BLACK, BLUE, GREEN, RED, WHITE, YELLOW
BLACK = (0,0,0)
BLUE = (20,20,200)
GREEN = (0,255,0)
RED = (255,0,0)
WHITE = (255,255,255)
YELLOW = (255, 255, 0)

# Lists:
board = []

for i in range(0, 6):
    board.append([0,0,0,0,0,0,0])

#variables
player1turn = True

#pygame GUI components
screenWidth = 800
screenHeight = 600

screen = pygame.display.set_mode((screenWidth, screenHeight))
large_font = pygame.font.SysFont("comicsansms", 24)
small_font = pygame.font.SysFont("comicsansms", 20)

rulesDisplay1 = large_font.render("Welcome to Connect 4! ", True, BLACK)
rulesDisplay2 = large_font.render("This game is played with 2 players. ", True, BLACK)
rulesDisplay3 = large_font.render("To win the game you must align 4 adjacent chips,", True, BLACK)
rulesDisplay4 = large_font.render("either in a vertical, horizontal, or diagonal line.", True, BLACK)
rulesDisplay5 = large_font.render("", True, BLACK)
rulesDisplay6 = large_font.render("Type (S) to start the game.", True, BLACK)

#screen control components
keepGoingRules = True
keepGoingGame = True

#sounds
click = pygame.mixer.Sound("click.mp3")
win = pygame.mixer.Sound("win.mp3")
music = pygame.mixer.Sound("music.mp3")

#setup images
img = pygame.image.load("logo.jpg").convert() #logo
imgWidth = 200
imgHeight = 133
img_rect = img.get_rect()
img_rect.left = 0
img_rect.top = 400
img = pygame.transform.scale(img, (imgWidth, imgHeight))
screen.blit(img, img_rect)

imgbg = pygame.image.load("background.jpg").convert() #background for controll screen
imgbgWidth = 800
imgbgHeight = 600
imgbg_rect = img.get_rect()
imgbg_rect.left = 0
imgbg_rect.top = 0
imgbg = pygame.transform.scale(imgbg, (imgbgWidth, imgbgHeight))
screen.blit(imgbg, imgbg_rect)

imggm = pygame.image.load("gamescreen.jpg").convert() #background for controll screen
imggmWidth = 800
imggmHeight = 600
imggm_rect = img.get_rect()
imggm_rect.left = 0
imggm_rect.top = 0
imggm = pygame.transform.scale(imggm, (imggmWidth, imggmHeight))

imgbrd = pygame.image.load("board.jpg").convert() #background for controll screen
imgbrdWidth = 602
imgbrdHeight = 516
imgbrd_rect = img.get_rect()
imgbrd_rect.left = 198
imgbrd_rect.top = 0
imgbrd = pygame.transform.scale(imgbrd, (imgbrdWidth, imgbrdHeight))

imgtie = pygame.image.load("tie.jpg").convert() #background for controll screen
imgtieWidth = 602
imgtieHeight = 516
imgtie_rect = img.get_rect()
imgtie_rect.left = 198
imgtie_rect.top = 0
imgtie = pygame.transform.scale(imgtie, (imgtieWidth, imgtieHeight))

# ----- 3) Pygame commands ----------------------------------------------
# 3a) Setup pygame & screen commands
pygame.display.set_caption("Rules") 

# 3b) Display Rules screen until user closes it
while keepGoingRules:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keepGoingRules = False
            sys.exit()  #exit the program
            
        elif event.type == pygame.KEYDOWN:    
            if event.key == pygame.K_s:
                pygame.display.set_caption("Game")
                keepGoingRules = False
            #end of if event.key 

        #end of if event

    #end for event
     
    
    #display the rules to the screen   
    screen.blit(imgbg, imgbg_rect)
    screen.blit(rulesDisplay1, (20, 20))
    screen.blit(rulesDisplay2, (20, 60))
    screen.blit(rulesDisplay3, (20, 100))
    screen.blit(rulesDisplay4, (20, 140))
    screen.blit(rulesDisplay5, (20, 180))
    screen.blit(rulesDisplay6, (20, 220))    
    pygame.display.flip()
    

#end while keepGoingRules-----------------------------------------------------------------------

music.play() #game music


#display start
screen.fill(WHITE)

screen.blit(imggm, imggm_rect)
pygame.draw.rect(screen,BLUE,(194,0,800,520))
screen.blit(imgbrd, imgbrd_rect)


#circles

for i in range (7):
    for n in range (6):
        pygame.draw.ellipse(screen,WHITE,(198+2+i*86, 0+2+n*86, 82, 82))

# 3c) Display Game screen until user closes it
while keepGoingGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keepGoingGame = False
            sys.exit()  #exit the program
            
    rowNumberLabel = large_font.render("(Column numbers)", True, BLACK)
            
    rowNumber1 = large_font.render("1", True, BLACK)
    rowNumber2 = large_font.render("2", True, BLACK)
    rowNumber3 = large_font.render("3", True, BLACK)
    rowNumber4 = large_font.render("4", True, BLACK)
    rowNumber5 = large_font.render("5", True, BLACK)
    rowNumber6 = large_font.render("6", True, BLACK)
    rowNumber7=  large_font.render("7", True, BLACK)       
   

    i = 86

    screen.blit(rowNumberLabel, (385, 550))
    screen.blit(rowNumber1, (235, 520))
    screen.blit(rowNumber2, (235 + i, 520))
    screen.blit(rowNumber3, (235 + i * 2, 520))
    screen.blit(rowNumber4, (235 + i * 3, 520))
    screen.blit(rowNumber5, (235 + i * 4, 520))
    screen.blit(rowNumber6, (235 + i * 5, 520))
    screen.blit(rowNumber7, (235 + i * 6, 520))

    # controlls
    controlls1 = large_font.render("Controls:", True, BLACK)
    controlls2 = small_font.render("Press the number", True, BLACK)
    controlls3 = small_font.render("corresponding with", True, BLACK)
    controlls4 = small_font.render("the column you wish", True, BLACK)
    controlls5 = small_font.render("to place your chip", True, BLACK)
    
    controlls6 = large_font.render("It is player:", True, BLACK)
    controlls7 = large_font.render("'s Turn", True, BLACK)
    
    screen.blit(controlls1, (35, 15))
    screen.blit(controlls2, (5, 45))
    screen.blit(controlls3, (5, 75))
    screen.blit(controlls4, (5, 105))
    screen.blit(controlls5, (5, 135))
    
    screen.blit(controlls6, (5, 265))
    screen.blit(controlls7, (25, 295))
    
    #initial player turn
    pygame.draw.rect(screen,RED,(2,294,20,30))
    pygame.display.flip()       
    playerTurn = large_font.render("1", True, BLACK)
    screen.blit(playerTurn, (5, 295))      
    
    #logo
    screen.blit(img, img_rect)    
    
    pygame.display.flip()

#actual gameplay --------------------------------------------------------------

    #player 1 turn

    if player1turn == True:
        chipInput=1
        pygame.draw.rect(screen,RED,(2,294,20,30))   
        playerTurn1 = large_font.render("1", True, BLACK)  
        screen.blit(playerTurn1, (5, 295))  
        pygame.display.flip()  
    else:
        chipInput=2
        pygame.draw.rect(screen,YELLOW,(2,294,20,30))  
        playerTurn2 = large_font.render("2", True, BLACK) 
        screen.blit(playerTurn2, (5, 295))        
        pygame.display.flip()  

    c = -1
    tie = 0

    waiting_for_key = True
    while waiting_for_key:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:   
                if win==True:
                    break
                else:
                    if event.key == pygame.K_1:
                        c = 0
                        print (c)
                        waiting_for_key = False
                        break
    
                    elif event.key == pygame.K_2:
                        c = 1
                        print (c)
                        waiting_for_key = False
                        break
                    
                    elif event.key == pygame.K_3:
                        c = 2
                        print (c)
                        waiting_for_key = False
                        break
    
                    elif event.key == pygame.K_4:
                        c = 3
                        print (c)
                        waiting_for_key = False
                        break           
    
                    elif event.key == pygame.K_5:
                        c = 4
                        print (c)
                        waiting_for_key = False
                        break
    
                    elif event.key == pygame.K_6:
                        c = 5
                        print (c)
                        waiting_for_key = False
                        break
    
                    elif event.key == pygame.K_7:
                        c = 6
                        print (c) 
                        waiting_for_key = False
                        break               

             

   # place the chip:

    r = -1
    for i in range(0, len(board)):
        j =  len(board) - 1 - i
        
        if board[j][c] != 0:
            continue

        else:
            board[j][c] = chipInput
            r = j
            break


    if r == -1:
        continue

                    
   #debug board
    print (board[0])
    print (board[1])
    print (board[2])
    print (board[3])
    print (board[4])
    print (board[5])
    print ("x" * 21)

    

    #draw chip and switch turn 
    if player1turn == True:
        click.play()
        pygame.draw.ellipse(screen,RED,(198+2+c*86, 0+2+(r)*86, 82, 82))
        pygame.display.flip()
        time.sleep(.1)
        
        player1turn = False    

    else:
        click.play()
        pygame.draw.ellipse(screen,YELLOW,(198+2+c*86, 0+2+(r)*86, 82, 82))
        pygame.display.flip()  
        time.sleep(.1)
                
        player1turn = True

        

    #check win conditions-------------------------------------------------------
    print(r) #y value
    print(c) #x value
    print(0 in board[0])
    

    winning_pieces = [(r, c)]
    if r <= 2:
        # check vertical win
        for i in range(r, len(board)):
            if board[i][c] == chipInput:
                winning_pieces.append((i, c))
            else:
                break

        if len(winning_pieces) >= 5:
            print("Player wins vertically!")
            win.play()
            win = True


    # check horizontal win
    if win != True:
        num_horiz = 1
        winning_pieces = [(r, c)]
        for i in range(c+1, len(board[0])):
            if board[r][i] == chipInput:
                winning_pieces.append((r, i))
            else:
                break

        for i in range(c-1, -1, -1):
            if board[r][i] == chipInput:
                winning_pieces.append((r, i))
            else:
                break

        if len(winning_pieces) >= 4:
            print("Player wins horizontally!")
            win.play()
            win = True
            
    # check for right diagonal win
    if win != True:
        winning_pieces = [(r, c)]
        check_x = c + 1
        check_y = r - 1
        while check_x < len(board[0]) and check_y >= 0:
            print("Checking " + str(check_x) + ", " + str(check_y))
            if board[check_y][check_x] == chipInput:
                print("Found " + str(check_x) + ", " + str(check_y) + "!")
                winning_pieces.append((check_y, check_x))
                check_x = check_x + 1
                check_y = check_y - 1
            else:
                break
                
        check_x = c - 1
        check_y = r + 1
        while check_x >= 0 and check_y < len(board):
            print("Checking " + str(check_x) + ", " + str(check_y))
            if board[check_y][check_x] == chipInput:
                print("Found " + str(check_x) + ", " + str(check_y) + "!")
                winning_pieces.append((check_y, check_x))
                check_x = check_x - 1
                check_y = check_y + 1
            else:
                break
    
        if len(winning_pieces) >= 4:
            print("Player wins diagonally!")
            win.play()
            win = True            

    # check for left diagonal win
    if win != True:
        winning_pieces = [(r, c)]
        check_x = c + 1
        check_y = r + 1
        while check_x < len(board[0]) and check_y < len(board):
            print("Checking " + str(check_x) + ", " + str(check_y))
            if board[check_y][check_x] == chipInput:
                print("Found " + str(check_x) + ", " + str(check_y) + "!")
                winning_pieces.append((check_y, check_x))
                check_x = check_x + 1
                check_y = check_y + 1
            else:
                break
                
        check_x = c - 1
        check_y = r +- 1
        while check_x >= 0 and check_y >= 0:
            print("Checking " + str(check_x) + ", " + str(check_y))
            if board[check_y][check_x] == chipInput:
                print("Found " + str(check_x) + ", " + str(check_y) + "!")
                winning_pieces.append((check_y, check_x))
                check_x = check_x - 1
                check_y = check_y - 1
            else:
                break
    
        if len(winning_pieces) >= 4:
            print("Player wins diagonally!")
            win.play()
            win = True   
            
            
    # check for tie
    if (0 in board[0]) == False:
        screen.blit(imgtie, imgtie_rect)
        img = pygame.image.load("lose.jpg").convert() #switches to win image
        imgWidth = 200
        imgHeight = 133
        img_rect = img.get_rect()
        img_rect.left = 0
        img_rect.top = 192
        img = pygame.transform.scale(img, (imgWidth, imgHeight))      
        screen.blit(img, img_rect)        

        
    else:
        print("uh oh, we got a bug on our hands")


#when a player wins--------------
    if win == True:
        player1turn = not player1turn
        img = pygame.image.load("win.jpg").convert() #switches to win image
        imgWidth = 200
        imgHeight = 133
        img_rect = img.get_rect()
        img_rect.left = 0
        img_rect.top = 192
        img = pygame.transform.scale(img, (imgWidth, imgHeight))      
        screen.blit(img, img_rect)
        screen.fill(WHITE, (0, 50, 110, 40)) 
        
        if player1turn == False: #false because I switch the player turn earlier to make the number on Arnolds picture the correct player.
            click.play()
            pygame.draw.ellipse(screen,YELLOW,(198+2+c*86, 0+2+(r)*86, 82, 82))
            print ("player 2 wins")
        else:
            click.play()
            pygame.draw.ellipse(screen,RED,(198+2+c*86, 0+2+(r)*86, 82, 82))
            print ("player 1 wins")

        for piece in winning_pieces:
            pygame.draw.ellipse(screen,GREEN,(198+2+piece[1]*86, 0+2+(piece[0])*86, 82, 82))

#end of while keepGoingGame