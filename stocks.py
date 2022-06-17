from yahoo_fin import stock_info as si
import pygame,sys,os
from pygame.locals import *


stock = input("Name of ticker? ")
bought = float(input("What price were they bought? "))
quantity = int(input("How many stocks were bought? "))

X= 1920
Y= 1080

pygame.init()
DISPLAYSURF= pygame.display.set_mode((X, Y))
pygame.display.set_caption('Stocks')
os.environ['SDL_VIDEO_CENTERED'] = "True"
pygame.font.init()
font = pygame.font.Font('freesansbold.ttf', 512) 
smallerFont = pygame.font.Font('freesansbold.ttf', 100) 
openPrice = si.get_data(stock).close[-1]


stockSTR = font.render(stock.upper(), True,[0,0,0]) 
stockRect = stockSTR.get_rect()  
stockRect.center = (X // 2, Y // 2-200) 


while True:
    current = round(si.get_live_price(stock),2)

    diffPerStock = round(current-openPrice,2)
    totalDiff = round((current - bought)*quantity,2)
    if diffPerStock>0:
        colourSub = [0,255,0]
    else:
        colourSub = [255,0,0]
    
    if totalDiff>0:
        colourSub2 = [0,255,0]
    else:
        colourSub2 = [255,0,0]

    currentP = smallerFont.render("$ "+str(current), True,[0,0,0]) 
    currentPRect = currentP.get_rect()  
    currentPRect.center = (X // 2, Y // 2 +100)

    diffPerSTR = smallerFont.render("$ "+str(diffPerStock), True,colourSub) 
    diffPerRect = diffPerSTR.get_rect()  
    diffPerRect.center = (X // 2-400, Y // 2 + 300)

    totalDiffSTR = smallerFont.render("$ "+str(totalDiff), True,colourSub2) 
    totalDiffRect = totalDiffSTR.get_rect()  
    totalDiffRect.center = (X // 2+400, Y // 2 + 300)

    DISPLAYSURF.fill([255,255,255])
    DISPLAYSURF.blit(stockSTR, stockRect) 
    DISPLAYSURF.blit(diffPerSTR, diffPerRect)
    DISPLAYSURF.blit(totalDiffSTR, totalDiffRect)
    DISPLAYSURF.blit(currentP, currentPRect)


    for event in pygame.event.get():
        if event.type ==QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
