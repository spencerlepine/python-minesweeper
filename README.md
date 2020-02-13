# Python Minesweeper
Recreation of the classic Minesweeper game using Pygame

*Required:* Set up PyGame to run the code: https://stackoverflow.com/questions/28453854/add-pygame-module-in-pycharm-id

Troubles: 1) Only using local variables, had not learned what a global variable was at beginning. 2) The most difficult issue; uncovering multiple blocks at once (smoothly). My initial approach was to test surrounding blocks in daimond layers (up, down, left, right) outwards recursively, stopping before uncovering a bomb. This worked, but it was processing much to slowly to be functional. I took a break from this project after struggling to solve this problem. Later, when I began to work on other game mechanics, I added a timer. The timer needs to update regardless of user input, so it needed to be run in the 'while not gameOver' loop. That was the solution for uncovering the blocks: constantly update the cover blocks in the game loop. The blocks were uncovering slowly becuase it only updated if the cursor was being moved during the 'for event in pygame.event.get()'.

