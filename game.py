import pygame
import time
import random
pygame.init()
score = 0
displayWidth = 640
displayHeight = 480
gameDisplay = pygame.display.set_mode((displayWidth , displayHeight))
pygame.display.set_caption("Saving Gotham")

gameExit = False
gameOver = False

leadX=displayHeight/2
leadY=displayWidth/2
leadXMove=0
leadYMove =0
blockSize = 10
randBombX = round(random.randrange(0,displayWidth - 2*blockSize)/10.0)*10.0
randBombY = round(random.randrange(0,displayHeight - 2*blockSize)/10.0)*10.0
white =(255,255,255)
red=(255,0,0)
green=(0,255,0)
black =(0,0,0)
fps=31
clock = pygame.time.Clock()
font = pygame.font.SysFont(None,31)
font2= pygame.font.SysFont(None,34)
bombList = []
bombSize =1
bombThickness = 30
def messageOnScreen(msg , color):
    screenText = font.render(msg,True,color)
    gameDisplay.blit(screenText,[displayHeight/4,displayWidth/4])

def batMobile ( bombList  ,blockSize):
   for xny in bombList:
       pygame.draw.rect(gameDisplay, black , [xny[0] ,xny[1],blockSize,blockSize])

while  gameOver:
    for event in pygame.event.get():
        if event.type== pygame.KEYDOWN:
            if event.key==pygame.K_q:
                gameOver = True
                gameExit = True
            if event.key==pygame.K_r:
                gameOver= False
                gameExit =False

while(not gameExit):                                                                #MAIN LOOP
     for  event in pygame.event.get():
        gameDisplay.fill(white)

        print(event)
        if(event.type==pygame.QUIT):
            gameExit= True
        if (event.type==pygame.KEYDOWN):
            if(event.key==pygame.K_LEFT):
                leadXMove = -blockSize
                leadYMove = 0

            elif(event.key==pygame.K_RIGHT):               #advantage of using elif over if is that if one of the if's is done the rest won't be bothered
                leadXMove =blockSize
                leadYMove =0

            elif(event.key==pygame.K_UP):
                leadYMove = -blockSize
                leadXMove =0

            elif(event.key==pygame.K_DOWN):
                leadYMove = blockSize
                leadXMove =0

     if leadX >=displayWidth or leadX<=0 or leadY>=displayHeight or leadY<=0:    #setting of boundries
         gameExit= True
         gameOver = False
     leadX+= leadXMove
     leadY+= leadYMove
     pygame.draw.rect(gameDisplay, red,[randBombX,randBombY,bombThickness,bombThickness])

     batHead =[]
     batHead.append(leadX)
     batHead.append(leadY)
     bombList.append(batHead)
     if(len(bombList)> bombSize):
         del bombList[0]

     for eachSegment in bombList[:-1]:
         if(eachSegment==batHead):
             gameExit = True
             gameOver = True
     batMobile(bombList ,blockSize)
     pygame.display.flip()
     if leadX>=randBombX and leadX <= randBombX + bombThickness :
         if leadY>=randBombY and leadY <= randBombY + bombThickness:
             randBombX = round(random.randrange(0, displayWidth - 2 * blockSize)/10.0)*10.0
             randBombY = round(random.randrange(0, displayHeight - 2 * blockSize)/10.0)*10.0
             score += 1
             bombSize += 1

     clock.tick(fps/2)
messageOnScreen('GAME OVER :(  Avoid Collision Next Time ',red)
print('the score is',score)
pygame.display.update()
time.sleep(2)
pygame.quit()
quit()