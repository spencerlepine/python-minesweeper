import pygame
import sys
import time
import random
import math

#Initialize all imported pygame modules.
pygame.init()

#Define variables.
ROWS = 9
COLUMNS = 9
TILE_SIZE = 16
MARGIN = TILE_SIZE
PADDING = 10
WIN_WIDTH = PADDING + (COLUMNS) * TILE_SIZE + PADDING
WIN_HEIGHT = MARGIN + MARGIN + ((ROWS) * TILE_SIZE) + MARGIN + PADDING
backgroud_colour = (255,255,255)

#Set up the game clock.
timeElapsed = 0
clock = pygame.time.Clock()

#Define mouse event variable.
cursorEvent = pygame.event.poll()

#Define game variables.
gameOver = False
bombCount = 10
flagsPlaced = 0
smileState = "Game"

#Load images into pygame to display.
coverImg = pygame.image.load("Media/cover16.jpg")
bombImg = pygame.image.load("Media/bomb16.jpg")
endBombImg = pygame.image.load("Media/endbomb.jpg")
noBombImg = pygame.image.load("Media/nobomb.jpg")
blankImg = pygame.image.load("Media/blank16.jpg")
flagImg = pygame.image.load("Media/flag16.jpg")
smileUpImg = pygame.image.load("Media/smile-up.jpg")
smileDownImg = pygame.image.load("Media/smile-down.jpg")
smileOhNoImg = pygame.image.load("Media/smile-ohno.jpg")
smileDeadImg = pygame.image.load("Media/smile-dead.jpg")
smileCoolImg = pygame.image.load("Media/smile-cool.jpg")

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

#Set up the Pygame window.
gameDisplay = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption('Minesweeper')

logo = pygame.image.load("Media/icon.jpg")
pygame.display.set_icon(logo)

gameDisplay.fill(backgroud_colour)

#Template array.
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

#Define the defualt array for mineField, touchingField, and coverField.
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

#Function to reset all of the game values.
def initializeGame():
	global ROWS
	global COLUMNS
	global gameOver
	global mineField
	global touchingField
	global coverField
	global smileState
	global flagsPlaced
	global timeElapsed

	#Return initial values.
	timeElapsed = 0
	gameOver = False
	smileState = "Game"
	flagsPlaced = 0

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

	#Generate a new minefield.
	placeBombs()

	#Set up touchingFeild to display numbers.
	for blockY in range(ROWS):
			for blockX in range(COLUMNS):
				searchSurrounding(blockX, blockY)

	#Run the game loop to use these new values.
	gameLoop()


#Randomly place bombs in mineField.
def placeBombs():
	tempBombCount = 0

	#Randomly generate mine coordinates withing the array.
	for i in range(bombCount):
		tempX = random.randrange(0, COLUMNS)
		tempY = random.randrange(0, ROWS)

		#Verify that a mine is not already in this spot.
		if mineField[tempY][tempX] == 0:
			mineField[tempY][tempX] = 1

	#Check array for the amount of bombs placed.
	for checkY in range(ROWS):
		for checkX in range(COLUMNS):
			if mineField[checkY][checkX] == 1:
				tempBombCount += 1

	#Place more bombs until there are enough bombs.
	if tempBombCount < bombCount:
		placeBombs()


#Returns displayable textSurface.get_rect().
def textObjects(text, font, color):
	textSurface = font.render(text, True, color)
	return textSurface, textSurface.get_rect()


#Display text object in gameDispay.
def textDisplay(text, x, y, color, type):
	if type == "Block":
		numberText = pygame.font.Font("Media/minesweeper.ttf", round(TILE_SIZE*(2/3)-1))
		textSurf, textRect = textObjects(text, numberText, color)
		textRect.center = (x + TILE_SIZE/2, y + TILE_SIZE/2)
		gameDisplay.blit(textSurf, textRect)


#Recursively uncover the blocks that are not a bomb, in layers outwards.
def testSurrounding(cellColumn, cellRow):
	if mineField[cellRow][cellColumn] == 0 and touchingField[cellRow][cellColumn] == 0:
		#Test if edges are uncoverable.
		if cellRow > 0 and coverField[cellRow-1][cellColumn] == 0:
			coverField[cellRow-1][cellColumn] = 1
			testSurrounding(cellColumn, cellRow-1)

		if cellColumn > 0 and coverField[cellRow][cellColumn-1] == 0:
		 	coverField[cellRow][cellColumn-1] = 1
		 	testSurrounding(cellColumn-1, cellRow)

		if cellColumn < COLUMNS-1 and coverField[cellRow][cellColumn+1] == 0:
		 	coverField[cellRow][cellColumn+1] = 1
		 	testSurrounding(cellColumn+1, cellRow)

		if cellRow < ROWS-1 and coverField[cellRow+1][cellColumn] == 0:
		 	coverField[cellRow+1][cellColumn] = 1
		 	testSurrounding(cellColumn, cellRow+1)

		#Test if corners are uncoverable.
		if cellRow > 0 and cellColumn > 0 and coverField[cellRow-1][cellColumn-1] == 0:
			coverField[cellRow-1][cellColumn-1] = 1
			testSurrounding(cellColumn-1, cellRow-1)

		if cellColumn < COLUMNS-1 and cellRow > 0 and coverField[cellRow-1][cellColumn+1] == 0:
			coverField[cellRow-1][cellColumn+1] = 1
			testSurrounding(cellColumn+1, cellRow-1)			

		if cellRow < ROWS-1 and cellColumn > 0 and coverField[cellRow+1][cellColumn-1] == 0:
			coverField[cellRow+1][cellColumn-1] = 1
			testSurrounding(cellColumn-1, cellRow+1)

		if cellRow < ROWS-1 and cellColumn < COLUMNS-1 and coverField[cellRow+1][cellColumn+1] == 0:
			coverField[cellRow+1][cellColumn+1] = 1
			testSurrounding(cellColumn+1, cellRow+1)


#Draw the image as a number from touchingField or as a bomb from mineField.
def bombBlock(arrayCol, arrayRow):
	blockX = arrayCol * TILE_SIZE
	blockY = arrayRow * TILE_SIZE

	touchingBombs = str(touchingField[arrayRow][arrayCol])
	touchingBombsLabel = str(touchingBombs)

	#Change the block coordinates to center the sprites in gameDisplay.
	blockX += PADDING
	blockY += MARGIN*2 + PADDING*2

	blockType = "Blank"

	one = (0,0,255)
	two = (0,123,0)
	three = (255,0,0)
	four = (0,0,123)
	five = (123,0,0)
	six = (0,123,123)
	seven = (0,255,0)
	eight = (123,123,123)

	#If the position in mineField is 1, this block is a bomb instead of a label.
	if mineField[arrayRow][arrayCol] == 1:
		blockType = "Bomb"

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

	if blockType == "Blank" and coverField[arrayRow][arrayCol] == 1:
		gameDisplay.blit(blankImg, (blockX, blockY))
		if touchingBombsLabel != "0" and coverField[arrayRow][arrayCol] == 1:
			textDisplay(touchingBombsLabel, blockX, blockY, labelColor, "Block")
	elif blockType == "Bomb" and coverField[arrayRow][arrayCol] == 1:
		gameDisplay.blit(bombImg, (blockX, blockY))


#Draw the cover, flag, or no image based on the given mineField	index.
def coverBlock(arrayCol, arrayRow, liftedMouse, mouseButton):
	global gameOver
	global smileState
	global flagsPlaced
	global ROWS
	global COLUMNS

	blockX = arrayCol * TILE_SIZE
	blockY = arrayRow * TILE_SIZE

	#Change the block coordinates to center the sprites in gameDisplay.
	blockX += PADDING
	blockY += PADDING*2 + MARGIN*2

	mouseX, mouseY = pygame.mouse.get_pos()

	#Test if the mouse is clicked within cell coordinates.
	if liftedMouse == True and mouseButton == "Left":
		if mouseX > blockX and mouseX < blockX + TILE_SIZE:
			if mouseY > blockY and mouseY < blockY + TILE_SIZE:
				if coverField[arrayRow][arrayCol] == 0:
					coverField[arrayRow][arrayCol] = 1
					testSurrounding(arrayCol, arrayRow)
					if mineField[arrayRow][arrayCol] == 1:
						coverField[arrayRow][arrayCol] = 3
						for bY in range(ROWS):
							for bX in range(COLUMNS):
								if coverField[bY][bX] == 2 and mineField[bY][bX] == 0:
									coverField[bY][bX] = 4
									coverBlock(bX, bY, liftedMouse, mouseButton)
						gameOver = "True"

	if liftedMouse == True and mouseButton == "Right":
		if mouseX > blockX and mouseX < blockX + TILE_SIZE:
			if mouseY > blockY and mouseY < blockY + TILE_SIZE:
				if coverField[arrayRow][arrayCol] == 0:
					coverField[arrayRow][arrayCol] = 2
					flagsPlaced += 1
				elif coverField[arrayRow][arrayCol] == 2:
					coverField[arrayRow][arrayCol] = 0
					flagsPlaced -= 1

	if coverField[arrayRow][arrayCol] == 0 and coverField[arrayRow][arrayCol] != 1:
		gameDisplay.blit(coverImg, (blockX, blockY))

	if coverField[arrayRow][arrayCol] == 2:
		gameDisplay.blit(flagImg, (blockX, blockY))
	elif coverField[arrayRow][arrayCol] == 3:
		gameDisplay.blit(endBombImg, (blockX, blockY))
	elif coverField[arrayRow][arrayCol] == 4:
		gameDisplay.blit(noBombImg, (blockX, blockY))


#Draw the proper smiley face image depending on the current smileState.
def processSmiley(mouseDown, liftedMouse, smileState):
	smileImgX = ((WIN_WIDTH / 2) - (26/2))
	smileImgY = ((MARGIN) - (26/2)) + PADDING

	mouseX, mouseY = pygame.mouse.get_pos()

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
	elif smileState == "Cool":
		gameDisplay.blit(smileCoolImg, ((smileImgX), (smileImgY)))


#The corresponding image for the 0-9 digit for the given place value.
def decideDig(place, score):
	global bombCount
	global flagsPlaced

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
			if score < -99:
				number = 9
	elif place == 3:
		number = math.floor((score - (math.floor(score / 1000)) * 1000 ) / 100)
		if score < 0:
			number = math.floor(((score*-1) - (math.floor((score*-1) / 1000)) * 1000 ) / 100)
			number = -1

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


#Determine which image should be displayed for each place value of the count of undiscovered bombs.
def processBombCount():
	global flagsPlaced
	global bombCount

	bombCountX = PADDING + 4
	bombCountY = PADDING + 6
	digitSpacing = 13
	uncovered = bombCount - flagsPlaced

	gameDisplay.blit(decideDig(1, uncovered), (bombCountX + digitSpacing*2, bombCountY))
	gameDisplay.blit(decideDig(2, uncovered), (bombCountX + digitSpacing, bombCountY))
	gameDisplay.blit(decideDig(3, uncovered), (bombCountX, bombCountY))


#Determine which image should be displayed for each place value of the time.
def processTimer():
	global timeElapsed
	seconds = round(timeElapsed / 1000)

	digitSpacing = 13
	timerX = WIN_WIDTH - PADDING - 4 - (digitSpacing*3)
	timerY = PADDING + 6

	gameDisplay.blit(decideDig(1,seconds), (timerX + digitSpacing*2, timerY))
	gameDisplay.blit(decideDig(2,seconds), (timerX + digitSpacing, timerY))
	gameDisplay.blit(decideDig(3,seconds), (timerX, timerY))


#Determine the amount of surrounding bombs for the given index in touchingField.	
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

	if blockY < ROWS-1 and mineField[blockY+1][blockX-1] == 1 and blockX > 0:
		touchingField[blockY][blockX] += 1

	if blockY < ROWS-1 and mineField[blockY+1][blockX] == 1 :
		touchingField[blockY][blockX] += 1	

	if blockY < ROWS-1 and blockX < COLUMNS-1 and mineField[blockY+1][blockX+1] == 1:
		touchingField[blockY][blockX] += 1


#Draw the array of sprites, update the bomb counter, and update the timer.
def processAllCells(mouseStatus, whichMouseButton):
	global ROWS
	global COLUMNS
	
	for blockY in range(ROWS):
		for blockX in range(COLUMNS):
			checkFlags()
			coverBlock(blockX, blockY, mouseStatus, whichMouseButton)
			bombBlock(blockX, blockY)

	processBombCount()
	processTimer()


#Explode bombs after death	
def uncoverBombs():
	global COLUMNS
	global ROWS

	for blockY in range(ROWS):
		for blockX in range(COLUMNS):
			if mineField[blockY][blockX] == 1:
				if coverField[blockY][blockX] < 2:
					coverField[blockY][blockX] = 1
					bombBlock(blockX, blockY)


#Pause the game if user wins
def checkFlags():
	global bombCount
	global flagsPlaced
	global gameOver
	global smileState

	acceptableFlags = 0

	if bombCount - flagsPlaced == 0:
		for blockY in range(ROWS):
			for blockX in range(COLUMNS):
					if coverField[blockY][blockX] == 2 and mineField[blockY][blockX] == 1:
						acceptableFlags += 1
		if acceptableFlags == bombCount:
			smileState = "Cool"
			gameOver = True


#Set up mineFeild 
placeBombs()

#Determine the amount of surrounding bombs for each touchingField index for the start of the game.
for blockY in range(ROWS):
		for blockX in range(COLUMNS):
			searchSurrounding(blockX, blockY)

#Main loop to update and draw the game in gameDisplay.
def gameLoop():
	global gameOver
	global smileState
	global timeElapsed
	mouseX, mouseY = pygame.mouse.get_pos()

	while not gameOver: 
		liftedMouse = False
		mouseButton = "Left"
		mouseDown = False

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

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

		pygame.display.update()

		
		clock.tick(60)
		timeElapsed += 16.66676

	#Stop processing coverField, wait for user to restart the game.
	while gameOver: 
		liftedMouse = False

		if smileState != "Cool": 
			smileState = "Dead"

		smileImgX = ((WIN_WIDTH / 2) - (26/2))
		smileImgY = ((MARGIN) - (26/2)) + PADDING

		for blockY in range(9):
			for blockX in range(9):
			    uncoverBombs()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

			if mouseX > smileImgX and mouseX < smileImgX + 26:
				if mouseY > smileImgY and mouseY < smileImgY + 26:	
					if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
						mouseDown = True
						smileState = "Down"

			if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
			    liftedMouse = True

			processSmiley(mouseDown, liftedMouse, smileState)

		pygame.display.update()

		clock.tick(60)


gameLoop()