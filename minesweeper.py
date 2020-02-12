import pygame
import sys
import time
import random
#started on ‎Tuesday, ‎July ‎16, ‎2019, ‏‎3:28:13 PM"

#clean up code and label/explain stuff
#add clicks and dissiapearing covers
#automatically change touching block if clicked
#maybe add second paremeter for touching blanks
#make sure the middle four are always blank (ROWS/2)

#draw seperate cover on top with flag and breakbable boolean
#alwasy draw the bombs under

#initiate program
pygame.init()

#variables
ROWS = 9
COLUMNS = 9
bombCount = 10
TILE_SIZE = 16
MARGIN = TILE_SIZE
WIN_WIDTH = MARGIN + COLUMNS * TILE_SIZE + MARGIN
WIN_HEIGHT = MARGIN + MARGIN + ROWS * TILE_SIZE + MARGIN
backgroud_colour = (255,255,255)

#set up the game window
gameDisplay = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

#window title
pygame.display.set_caption('Minesweeper')

#set up important clock
clock = pygame.time.Clock()

#draw backgrond onto the screen
gameDisplay.fill(backgroud_colour)

#set up mouse events
cursorEvent = pygame.event.poll()

#set up window icon
#logo = pygame.image.load("Media/icon.png")
#pygame.display.set_icon(logo)

#game starts
gameOver = False

#load images
coverImg = pygame.image.load("Media/block16.jpg")
bombImg = pygame.image.load("Media/bomb16.jpg")
blankImg = pygame.image.load("Media/blank16.jpg")
flagImg = pygame.image.load("Media/flag16.jpg")

#backgroundImg = pygame.image.load("Media/background.png")

#MAX W and H is 16x30
"""mineField = [
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]"""

mineField = [
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
]
touchingField = [
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
]

coverField = [
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
]

def placeBombs():

	tempBombCount = 0

	#randomly generate mine coordinates
	for i in range(bombCount):
		tempX = random.randrange(0, COLUMNS)
		tempY = random.randrange(0, ROWS)

		#verify a mine is not already in this spot
		if mineField[tempY][tempX] == 0:
			mineField[tempY][tempX] = 1

	#check array for the amount of bombs placed
	for checkY in range(ROWS):

		for checkX in range(COLUMNS):

			if mineField[checkY][checkX] == 1:
				tempBombCount+=1

	#restart function until there are enough bombs
	if tempBombCount < bombCount:
		placeBombs()

placeBombs()

#set up text function
def textObjects(text, font, color):
	textSurface = font.render(text, True, color)
	return textSurface, textSurface.get_rect()

#display a message function
def textDisplay(text, x, y, color):
	#numberText = pygame.font.Font("freesansbold.ttf", round(TILE_SIZE/2))
	#numberText = pygame.font.Font("Media/digit-7-mono.ttf", round((TILE_SIZE/8)*7))
	numberText = pygame.font.Font("Media/minesweeper.ttf", round(TILE_SIZE*(2/3)))
	textSurf, textRect = textObjects(text, numberText, color)
	#center the text
	textRect.center = (x + TILE_SIZE/2, y + TILE_SIZE/2)
	gameDisplay.blit(textSurf, textRect)

def testSurrounding(cellColumn, cellRow):
	#cellColumn, cellRow is the whole number of the array

	#Uncover other blanks automatically
	"""FIX BUG: After other blocks are uncovered, the game freezes trying to process the next layer"""
	#for i in range(ROWS):
	if mineField[cellRow][cellColumn] == 0 and touchingField[cellRow][cellColumn] == 0:

		#if cellRow > 0 and cellColumn > 0 and coverField[cellRow-1][cellColumn-1] == 0:
			#coverField[cellRow-1][cellColumn-1] = 1
			#testSurrounding(cellColumn-1, cellRow-1, 0)

		if cellRow > 0 and coverField[cellRow-1][cellColumn] == 0:
			coverField[cellRow-1][cellColumn] = 1
			testSurrounding(cellColumn, cellRow-1)

		#if cellColumn < COLUMNS-1 and cellRow > 0 and coverField[cellRow-1][cellColumn+1] == 0:
		 	#coverField[cellRow-1][cellColumn+1] = 1
		 	#testSurrounding(cellColumn+1, cellRow-1, 0)

		if cellColumn > 0 and coverField[cellRow][cellColumn-1] == 0:
		 	coverField[cellRow][cellColumn-1] = 1
		 	testSurrounding(cellColumn-1, cellRow)

		if cellColumn < COLUMNS-1 and coverField[cellRow][cellColumn+1] == 0:
		 	coverField[cellRow][cellColumn+1] = 1
		 	testSurrounding(cellColumn+1, cellRow)

		#if cellRow < ROWS-1 and cellColumn > 1 and coverField[cellRow+1][cellColumn-1] == 0:
		 	#coverField[cellRow+1][cellColumn-1] = 1
		 	#testSurrounding(cellColumn-1, cellRow+1, 0)

		if cellRow < ROWS-1 and coverField[cellRow+1][cellColumn] == 0:
		 	coverField[cellRow+1][cellColumn] = 1
		 	testSurrounding(cellColumn, cellRow+1)

		#if cellRow < ROWS-1 and cellColumn < COLUMNS-1 and coverField[cellRow+1][cellColumn+1] == 0:
		 	#coverField[cellRow+1][cellColumn+1] = 1
		 	#testSurrounding(cellColumn+1, cellRow+1, 0)

		pygame.time.delay(6)

def bombBlock(arrayCol, arrayRow, touchingBombs):

	blockX = arrayCol * TILE_SIZE
	blockY = arrayRow * TILE_SIZE

	#center game grid
	blockX+=MARGIN
	blockY+=MARGIN*2

	blockType = "blank"

	one = (0,90,255)
	two = (65,175,65)
	three = (188,6,0)
	four = (116,0,188)
	five = (60,0,104)
	six = (255,0,0)
	seven = (0,255,0)
	eight = (0,0,0)

	#if cover == False:
		#testSurrounding(arrayCol, arrayRow, touchingBombs, blockType)

	if mineField[arrayRow][arrayCol] == 1:
		blockType = "bomb"

	touchingBombsLabel = str(touchingBombs)

	if touchingBombsLabel == "1":
		labelColor = one
	elif touchingBombsLabel == "2":
		labelColor = two
	elif touchingBombsLabel == "3":
		labelColor = three
	elif touchingBombsLabel == "4":
		labelColor = four
	elif touchingBombsLabel == "5":
		labelColor = five
	elif touchingBombsLabel == "6":
		labelColor = six
	elif touchingBombsLabel == "7":
		labelColor = seven
	elif touchingBombsLabel == "8":
		labelColor = eight

	if blockType == "blank" and coverField[arrayRow][arrayCol] == 1:
		gameDisplay.blit(blankImg, (blockX, blockY))

		if touchingBombsLabel != "0" and coverField[arrayRow][arrayCol] == 1:
			textDisplay(touchingBombsLabel, blockX, blockY, labelColor)

	elif blockType == "bomb" and coverField[arrayRow][arrayCol] == 1:
		gameDisplay.blit(bombImg, (blockX, blockY))
		
def coverBlock(arrayCol, arrayRow, liftedMouse, mouseButton, touchingBombs):

	blockX = arrayCol * TILE_SIZE
	blockY = arrayRow * TILE_SIZE

	#center game grid
	blockX+=MARGIN
	blockY+=MARGIN*2

	#if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
	mouseX, mouseY = pygame.mouse.get_pos()
	#event = pygame.event.poll()
	#test if mouse is clicked within cell parameters
	
	if liftedMouse == True and mouseButton == "Left":

		if mouseX > blockX and mouseX < blockX + TILE_SIZE:

			if mouseY > blockY and mouseY < blockY + TILE_SIZE:

				if coverField[arrayRow][arrayCol] == 0:
					#print("Clicked cell: (" + str(arrayCol + 1) + ", " + str(arrayRow + 1) + ")")
					coverField[arrayRow][arrayCol] = 1
					testSurrounding(arrayCol, arrayRow)

					if mineField[arrayRow][arrayCol] == 1:
						pygame.quit()
						quit()
						"""HERE: DRAWs over 1's and cannot undo flag"""

	if liftedMouse == True and mouseButton == "Right":

		if mouseX > blockX and mouseX < blockX + TILE_SIZE:

			if mouseY > blockY and mouseY < blockY + TILE_SIZE:

				if coverField[arrayRow][arrayCol] == 0:
					#print("Flaggeded cell: (" + str(arrayCol + 1) + ", " + str(arrayRow + 1) + ")")
					coverField[arrayRow][arrayCol] = 2

				elif coverField[arrayRow][arrayCol] == 2:
					#print("Flaggeded cell: (" + str(arrayCol + 1) + ", " + str(arrayRow + 1) + ")")
					coverField[arrayRow][arrayCol] = 0

	#if liftedMouse < 0:
		#testMouse()

	if coverField[arrayRow][arrayCol] == 0 and coverField[arrayRow][arrayCol] != 1:
		gameDisplay.blit(coverImg, (blockX, blockY))

	if coverField[arrayRow][arrayCol] == 2:
		gameDisplay.blit(flagImg, (blockX, blockY))

def bombSearch(blockX,blockY):

	touchingBombs = 0

	if mineField[blockY-1][blockX-1] == 1 and blockY > 0 and blockX > 0:
		touchingBombs+=1

	if mineField[blockY-1][blockX] == 1 and blockY > 0:
		touchingBombs+=1

	if blockX < COLUMNS-1 and mineField[blockY-1][blockX+1] == 1 and blockY > 0:
		touchingBombs+=1

	if mineField[blockY][blockX-1] == 1 and blockX > 0:
		touchingBombs+=1
		
	if blockX < COLUMNS-1 and mineField[blockY][blockX+1] == 1:
		touchingBombs+=1
		
	if blockY < ROWS-1 and mineField[blockY+1][blockX-1] == 1 and blockX > 1:
		touchingBombs+=1
		
	if blockY < ROWS-1 and mineField[blockY+1][blockX] == 1 :
		touchingBombs+=1
		
	if blockY < ROWS-1 and blockX < COLUMNS-1 and mineField[blockY+1][blockX+1] == 1:
		touchingBombs+=1

	return touchingBombs
	
def searchSurroinding(blockX,blockY):

	if mineField[blockY-1][blockX-1] == 1 and blockY > 0 and blockX > 0:
		touchingField[blockY][blockX] += 1
	if mineField[blockY-1][blockX] == 1 and blockY > 0:
		touchingField[blockY][blockX] += 1
	if blockX < COLUMNS-1 and mineField[blockY-1][blockX+1] == 1 and blockY > 0:
		touchingField[blockY][blockX] += 1
	if mineField[blockY][blockX-1] == 1 and blockX > 0:
		touchingField[blockY][blockX] += 1		
	if blockX < COLUMNS-1 and mineField[blockY][blockX+1] == 1:
		touchingField[blockY][blockX] += 1		
	if blockY < ROWS-1 and mineField[blockY+1][blockX-1] == 1 and blockX > 1:
		touchingField[blockY][blockX] += 1		
	if blockY < ROWS-1 and mineField[blockY+1][blockX] == 1 :
		touchingField[blockY][blockX] += 1		
	if blockY < ROWS-1 and blockX < COLUMNS-1 and mineField[blockY+1][blockX+1] == 1:
		touchingField[blockY][blockX] += 1

for blockY in range(ROWS):

		for blockX in range(COLUMNS):

			searchSurroinding(blockX, blockY)

print(touchingField)

def processAllCells(mouseStatus, whichMouseButton):

	for blockY in range(ROWS):

		for blockX in range(COLUMNS):

			coverBlock(blockX, blockY, mouseStatus, whichMouseButton, bombSearch(blockX, blockY))
			bombBlock(blockX, blockY, bombSearch(blockX, blockY))
			

def gameLoop():

	while not gameOver: 

		liftedMouse = False
		mouseButton = "Left"

		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				#gameOver = True
				pygame.quit()
				quit()

			"""if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
			    #None
			    liftedMouse = False
			    mouseButton = "Left"

			 """

			if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
			    #None
			    liftedMouse = True
			    mouseButton = "Left"

			elif event.type == pygame.MOUSEBUTTONUP and event.button == 3:
			    #None
			    liftedMouse = True
			    mouseButton = "Right"

			processAllCells(liftedMouse, mouseButton)
			    

		#gameDisplay.blit(backgroundImg, (WIN_WIDTH-WIN_WIDTH, WIN_HEIGHT-WIN_HEIGHT))
		#blockCover = True

		pygame.display.update()

		#pygame.event.wait()

		clock.tick(60)

gameLoop()

pygame.display.quit()
pygame.quit()
quit()