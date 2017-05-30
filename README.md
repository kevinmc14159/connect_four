# Connect Four
*Connect Four* is a Python implementation of the Connect Four game played via the console.

## How to Use
To play, execute the script via the command line. To set a custom board size, pass in the board dimensions as arguments when creating an instance of the *Game* object.

## How to Play
Players take turns entering a number for the column they want to drop their piece in. The piece will always land at the lowest unoccupied row for the column. If the column is full, no more pieces can be placed in that column. Once placed, pieces cannot be removed. The game goes on until a player manages to connect four of his/her pieces in a line either vertically, horizontally, or diagonally. At this point, the game ends and that player wins. If the whole board is full and nobody has won yet, the game ends in a draw.

## Key Concepts Applied
* Data Types
* Operators
* Decision Making
* Looping
* Functions
* Files & I/O
* Classes & Objects

## What I Learned
* Application of the object-oriented programming paradigm for this game is possible because the game can be represented as a class with fields (board dimensions, current state of the board, etc.) and methods (adding a move, checking for a win, etc.).
* Testing individual methods while they are written reduces the likelihood of complex bugs later in development.
* Writing code should only happen after you have solid understanding of the implementation of the fundamental principles being used for a project.
* Methods require a calling object while functions do not.
* The *print()* function automatically prints a newline character after printing the arguments passed in. If the *print()* function is called without any arguments, it simply prints a newline character.