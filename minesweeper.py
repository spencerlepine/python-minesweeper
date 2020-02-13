import pygame
import sys
import time
import random
import math
#started on ‎Tuesday, ‎July ‎16, ‎2019, ‏‎3:28:13 PM"

#https://www.reddit.com/r/SublimeText/comments/2mwb8u/quick_tip_sublime_text_clipboard_copy_paste/
#TO-DO ------------------------------------------------------------
#clean up code and label/explain stuff
#add clicks and dissiapearing covers
#automatically change touching block if clicked
#maybe add second paremeter for touching blanks
#make sure the middle four are always blank (ROWS/2)

#draw seperate cover on top with flag and breakbable boolean
#alwasy draw the bombs under
#SEARCH FOR "HERES" and print + MAKe banner with epic epxlosions
#change X-PADDING to just padding in code
#remove dash in readme title
#-------------------------------------------------------------------

#initiate program
pygame.init()

#variables
ROWS = 9
COLUMNS = 9
bombCount = 10
flagsPlaced = 0
TILE_SIZE = 16
MARGIN = TILE_SIZE
PADDING = 10
X_PADDING = 10
WIN_WIDTH = PADDING + (COLUMNS) * TILE_SIZE + PADDING
WIN_HEIGHT = MARGIN + MARGIN + ((ROWS) * TILE_SIZE) + MARGIN + PADDING
backgroud_colour = (255,255,255)

#set up the game window
gameDisplay = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

#window title
pygame.display.set_caption('Minesweeper')

#set up important clock
timeElapsed = 0
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

smileState = "Game"

#load images
coverImg = pygame.image.load("Media/block16.jpg")
bombImg = pygame.image.load("Media/bomb16.jpg")
blankImg = pygame.image.load("Media/blank16.jpg")
flagImg = pygame.image.load("Media/flag16.jpg")
smileUpImg = pygame.image.load("Media/smile-up.jpg")
smileDownImg = pygame.image.load("Media/smile-down.jpg")
smileOhNoImg = pygame.image.load("Media/smile-ohno.jpg")
smileDeadImg = pygame.image.load("Media/smile-dead.jpg")
smileCoolImg = pygame.image.load("Media/smile-cool.jpg")
#bombsImg = pygame.image.load("Media/bomb16s.jpg")
timesImg = pygame.image.load("Media/time.jpg")

oneImg = pygame.image.load("Media/one.jpg")
twoImg = pygame.image.load("Media/two.jpg")
threeImg = pygame.image.load("Media/three.jpg")
fourImg = pygame.image.load("Media/four.jpg")
fiveImg = pygame.image.load("Media/five.jpg")
sixImg = pygame.image.load("Media/six.jpg")
sevenImg = pygame.image.load("Media/seven.jpg")
eightImg = pygame.image.load("Media/eight.jpg")
nineImg = pygame.image.load("Media/nine.jpg")
zeroImg = pygame.image.load("Media/zero.jpg")
zipImg = pygame.image.load("Media/zip.jpg")

backgroundImg = pygame.image.load("Media/screenoutline.png")

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

def initializeGame():
	global ROWS
	global COLUMNS
	global bombCount
	global TILE_SIZE
	global MARGIN
	global WIN_WIDTH
	global WIN_HEIGHT
	global backgroud_colour
	global gameDisplay
	global clock
	global cursorEvent
	global gameOver
	global coverImg
	global bombImg
	global blankImg
	global flagImg
	global mineField
	global touchingField
	global coverField
	global smileState
	global flagsPlaced
	global timeElapsed

	#variables
	ROWS = 9
	COLUMNS = 9
	bombCount = 10

	flagsPlaced = 0
	#TILE_SIZE = 16
	#MARGIN = TILE_SIZE
	#WIN_WIDTH = MARGIN + COLUMNS * TILE_SIZE + MARGIN
	#WIN_HEIGHT = MARGIN + MARGIN + ROWS * TILE_SIZE + MARGIN
	#backgroud_colour = (255,255,255)

	#set up mouse events
	cursorEvent = pygame.event.poll()

	#set up window icon
	#logo = pygame.image.load("Media/icon.png")
	#pygame.display.set_icon(logo)

	timeElapsed = 0

	#game starts
	gameOver = False
	smileState = "Game"

	"""#load images DO I NEED THESE?
	coverImg = pygame.image.load("Media/block16.jpg")
	bombImg = pygame.image.load("Media/bomb16.jpg")
	blankImg = pygame.image.load("Media/blank16.jpg")
	flagImg = pygame.image.load("Media/flag16.jpg")"""

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

	print("Restated variables")

	placeBombs()

	for blockY in range(ROWS):

			for blockX in range(COLUMNS):

				searchSurrounding(blockX, blockY)

	gameLoop()

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
				#print("placed a bomb")

	#restart function until there are enough bombs
	if tempBombCount < bombCount:
		placeBombs()

placeBombs()

#set up text function
def textObjects(text, font, color):
	textSurface = font.render(text, True, color)
	return textSurface, textSurface.get_rect()

#display a message function
def textDisplay(text, x, y, color, type):

	if type == "Block":

		#numberText = pygame.font.Font("freesansbold.ttf", round(TILE_SIZE/2))
		#numberText = pygame.font.Font("Media/digit-7-mono.ttf", round((TILE_SIZE/8)*7))
		numberText = pygame.font.Font("Media/minesweeper.ttf", round(TILE_SIZE*(2/3)))
		textSurf, textRect = textObjects(text, numberText, color)
		#center the text
		textRect.center = (x + TILE_SIZE/2, y + TILE_SIZE/2)
		gameDisplay.blit(textSurf, textRect)

	"""elif type == "Digital": 

		fontSize = 28
		#numberText = pygame.font.Font("freesansbold.ttf", round(TILE_SIZE/2))
		#numberText = pygame.font.Font("Media/digit-7-mono.ttf", round((TILE_SIZE/8)*7))
		numberText = pygame.font.Font("Media/digit-7-mono.ttf", fontSize)
		textSurf, textRect = textObjects(text, numberText, color)
		#center the text
		#textRect.center = (x + TILE_SIZE/2, y + TILE_SIZE/2)
		textRect.center = (x, y + 10)
		gameDisplay.blit(textSurf, textRect)"""

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
	blockX+=X_PADDING
	blockY+=MARGIN*2 + PADDING*2

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
			textDisplay(touchingBombsLabel, blockX, blockY, labelColor, "Block")

	elif blockType == "bomb" and coverField[arrayRow][arrayCol] == 1:
		gameDisplay.blit(bombImg, (blockX, blockY))
		
def coverBlock(arrayCol, arrayRow, liftedMouse, mouseButton):

	global gameOver
	global smileState
	global flagsPlaced

	blockX = arrayCol * TILE_SIZE
	blockY = arrayRow * TILE_SIZE

	#center game grid
	blockX+=X_PADDING
	blockY+= PADDING*2 + MARGIN*2

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
						#pygame.quit()
						#quit()
						gameOver = "True"
						"""HERE: DRAWs over 1's and cannot undo flag"""

	if liftedMouse == True and mouseButton == "Right":

		if mouseX > blockX and mouseX < blockX + TILE_SIZE:

			if mouseY > blockY and mouseY < blockY + TILE_SIZE:

				if coverField[arrayRow][arrayCol] == 0:
					#print("Flaggeded cell: (" + str(arrayCol + 1) + ", " + str(arrayRow + 1) + ")")
					coverField[arrayRow][arrayCol] = 2
					flagsPlaced+=1

				elif coverField[arrayRow][arrayCol] == 2:
					#print("Flaggeded cell: (" + str(arrayCol + 1) + ", " + str(arrayRow + 1) + ")")
					coverField[arrayRow][arrayCol] = 0
					flagsPlaced-=1

	#if liftedMouse < 0:
		#testMouse()

	if coverField[arrayRow][arrayCol] == 0 and coverField[arrayRow][arrayCol] != 1:
		gameDisplay.blit(coverImg, (blockX, blockY))

	if coverField[arrayRow][arrayCol] == 2:
		gameDisplay.blit(flagImg, (blockX, blockY))

def processSmiley(mouseDown, liftedMouse, smileState):

	smileImgX = ((WIN_WIDTH / 2) - (26/2))
	smileImgY = ((MARGIN) - (26/2)) + PADDING

	mouseX, mouseY = pygame.mouse.get_pos()

	#if mouseState == True:
	#Down
	#OhNo
	#Game

	if liftedMouse:
		
		if mouseX > smileImgX and mouseX < smileImgX + 26:

			if mouseY > smileImgY and mouseY < smileImgY + 26:

				gameOver = True
				initializeGame()

	if mouseDown:

		if mouseX > smileImgX and mouseX < smileImgX + 26:

			if mouseY > smileImgY and mouseY < smileImgY + 26:

				gameDisplay.blit(smileDownImg, ((smileImgX), (smileImgY)))
	
	elif smileState == "Game":

		gameDisplay.blit(smileUpImg, ((smileImgX), (smileImgY)))


	elif smileState == "Down":

		gameDisplay.blit(smileDownImg, ((smileImgX), (smileImgY)))

	elif smileState == "OhNo":

		gameDisplay.blit(smileOhNoImg, ((smileImgX), (smileImgY)))

	elif smileState == "Dead":

		gameDisplay.blit(smileDeadImg, ((smileImgX), (smileImgY)))

	#else:
		#gameDisplay.blit(smileUpImg, ((WIN_WIDTH / 2) - (26/2), (MARGIN) - (26/2)))

def decideDig(place, score):

	global bombCount
	global flagsPlaced

	#print(score)

	number = 0

	if place == 1:

		if score < 0:
			
			score*=-1

			if score < -99:

				number = 9

		number = score - ((math.floor(score / 10 )) * 10)

	elif place == 2:

		number = math.floor((score - (math.floor(score / 100)) * 100 ) / 10)	

		if score < 0:

			number = math.floor(((score*-1) - (math.floor((score*-1) / 100)) * 100 ) / 10)

			#if score > -10:

				#number = -1

			if score < -99:

				number = 9

	elif place == 3:

		number = math.floor((score - (math.floor(score / 1000)) * 1000 ) / 100)

		if score < 0:

			number = math.floor(((score*-1) - (math.floor((score*-1) / 1000)) * 1000 ) / 100)

			#if score < 0:

			number = -1

	#number = str(round(number))
	if number == 0:

		return zeroImg

	elif number == 1:

		return oneImg

	elif number == 2:

		return twoImg

	elif number == 3:

		return threeImg

	elif number == 4:

		return fourImg

	elif number == 5:

		return fiveImg

	elif number == 6:

		return sixImg

	elif number == 7:

		return sevenImg

	elif number == 8:

		return eightImg

	elif number == 9:

		return nineImg
	
	elif number == -1:

		return zipImg

def processBombCount():

	global flagsPlaced
	global bombCount

	bombCountX = PADDING + 4
	bombCountY = PADDING + 6
	digitSpacing = 13
	uncovered = bombCount - flagsPlaced

	#digit 1
	gameDisplay.blit(decideDig(1, uncovered), (bombCountX + digitSpacing*2, bombCountY))
	#digit 2
	gameDisplay.blit(decideDig(2, uncovered), (bombCountX + digitSpacing, bombCountY))
	#digit 3
	gameDisplay.blit(decideDig(3, uncovered), (bombCountX, bombCountY))
	#print(decideDig(3, flagsPlaced))
	#textDisplay(str(bombCount - flagsPlaced), blockX, blockY, (0,0,0), "Digital")

def processTimer():

	global timeElapsed
	seconds = round(timeElapsed / 1000)

	#secondsElapsed = int(round(pygame.time.get_ticks()/1000))
	digitSpacing = 13
	timerX = WIN_WIDTH - PADDING - 4 - (digitSpacing*3)
	timerY = PADDING + 6

	#digit 1
	gameDisplay.blit(decideDig(1,seconds), (timerX + digitSpacing*2, timerY))
	#digit 2
	gameDisplay.blit(decideDig(2,seconds), (timerX + digitSpacing, timerY))
	#digit 3
	gameDisplay.blit(decideDig(3,seconds), (timerX, timerY))
	#print(decideDig(3, flagsPlaced))
	#textDisplay(str(timer - flagsPlaced), blockX, blockY, (0,0,0), "Digital")

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
	
def searchSurrounding(blockX,blockY):

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

			searchSurrounding(blockX, blockY)

#print(touchingField)

def processAllCells(mouseStatus, whichMouseButton):

	for blockY in range(ROWS):

		for blockX in range(COLUMNS):

			coverBlock(blockX, blockY, mouseStatus, whichMouseButton)
			bombBlock(blockX, blockY, bombSearch(blockX, blockY))

	processBombCount()
	processTimer()

def uncoverBombs():

	global COLUMNS
	global ROWS

	#processAllCells(False, False)
	"""for blockY in range(ROWS):
		for blockX in range(COLUMNS):
			if mineField[blockY][blockX] == 1:
				gameDisplay.blit(blankImg, (blockX, blockY))"""
	for blockY in range(ROWS):
		for blockX in range(COLUMNS):
			if mineField[blockY][blockX] == 1:
				coverField[blockY][blockX] = 1
				bombBlock(blockX, blockY, bombSearch(blockX, blockY))

def gameLoop():

	global gameOver
	global smileState
	mouseX, mouseY = pygame.mouse.get_pos()#MAKE GLOBAL

	global timeElapsed
	"""smileImgX = ((WIN_WIDTH / 2) - (26/2))
	smileImgY = ((MARGIN) - (26/2))

	mouseX, mouseY = pygame.mouse.get_pos()"""
	

	while not gameOver: 
		
		#timeElapsed+=0.1
		liftedMouse = False
		mouseButton = "Left"
		mouseDown = False

		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				#gameOver = True
				pygame.quit()
				quit()

			"""if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
			    
			    liftedMouse = False
			    mouseButton = "Left"

			 """
			if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

				mouseDown = True
				smileState = "OhNo"

			if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
			    
			    liftedMouse = True
			    mouseButton = "Left"
			    smileState = "Game"

			elif event.type == pygame.MOUSEBUTTONUP and event.button == 3:
			    
			    liftedMouse = True
			    mouseButton = "Right"

		processAllCells(liftedMouse, mouseButton)
		processSmiley(mouseDown, liftedMouse, smileState)    

		gameDisplay.blit(backgroundImg, (0, 0))
		#blockCover = True

		pygame.display.update()

		#pygame.event.wait()
		
		clock.tick(60)
		timeElapsed+=16.66676
		print(str(round(timeElapsed/1000)) + " --- " + str(int(round(pygame.time.get_ticks()/1000))))

	while gameOver: 
		
		liftedMouse = False
		smileState = "Dead"
		smileImgX = ((WIN_WIDTH / 2) - (26/2))
		smileImgY = ((MARGIN) - (26/2)) + PADDING

		for blockY in range(9):
			for blockX in range(9):
			    uncoverBombs()

		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				#gameOver = True
				pygame.quit()
				quit()

			

			if mouseX > smileImgX and mouseX < smileImgX + 26:

				if mouseY > smileImgY and mouseY < smileImgY + 26:
					
					if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
						mouseDown = True
						smileState = "Down"

			if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
			    
			    liftedMouse = True

			    """if mouseX > smileImgX and mouseX < smileImgX + 26:

			    	if mouseY > smileImgY and mouseY < smileImgY + 26:
			    		initializeGame()"""

			processSmiley(mouseDown, liftedMouse, smileState)
			    
			#if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
			    
			    #print("Restarting program")
			    #initializeGame()

		pygame.display.update()

		clock.tick(60)


gameLoop()

#pygame.display.quit()
#pygame.quit()
#quit()