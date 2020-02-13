# Python-Minesweeper
A recreation of the classic Minesweeper with Pygame, coded in python.
I used pygame 1.9.4 for this project.

I had some troubles when I was programming the game. I was only using local variables and midly confused, since I hadn't yet learned what a global variable was.
Another issue I had was uncovering multiplel blocks at once. When you click a blank spot to uncover it, all of the surrounding blank spots should automatically uncover as well. I approached this by testing every block surrounding, each time the player clicks. This was very slow, so I created a new system. When the game started a pool field would be generated, based on the spots with no bombs nearby. This would be faster with a predetermined amount of spots to uncover.

