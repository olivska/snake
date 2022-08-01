# Snake
A game in which the user controls a snake on the bordered plane.
The main purpose is to gather the objects displayed on a screen.

## Table of contents
* [Description](#description)
* [Dependencies](#dependencies)
* [Setup and Execution](#setup-and-execution)

## Description
Once the game runs the screen pops up. It contains the starting snake object, which is built of three square segments, 
and randomly placed food object (single square) within the borders of the screen. User is in charge of the snake that 
is in constant movement, player controls its head and therefore the direction of which the snake is heading. The aim is 
to eat the most possible amount of food by making contact with it, once snake touches the food it changes its location 
and the point is added to the player's score. The snake is growing bigger each time he eats the food, one new segment is 
added to the body. The user must keep the whole snake inside the borders and watch out to not eat its own tail. The game 
is over when snake's head touches the edge of the screen or its own body.

This project was created for learning purposes.
	
## Dependencies
Project is created with:
* Windows 10
* Python 3.10
* PyCharm 2022.1
## Setup and Execution
Clone this repo to your PyCharm and run main.py to start the program.