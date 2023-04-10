# BATTLESHIPS GAME

![Battleships Game](https://res.cloudinary.com/duxsycizt/image/upload/v1681071164/battleships-game/Screenshot01_zctbai.png) 

## Introduction

This is a simple implementation of the Battleships game in Python. In this game, the payer has to sink all the ships in the grid within a limited number of turns.
- The grid size is defined as 10.
- The number of ships is defined as 5.
- The ship symbol is defined as "S".
- The hit symbol is defined as "X".
- The miss symbol is defined as "O".
- The ships are randomly placed on the grid.
- The player has 10 turns to sink all the ships.
- The player has to enter the x and y coordinates of their shot (separated by a space).
- The game displays whether the shot was a hit or a miss.
- The game ends when all the ships are sunk or when the player has used all their turns.
- At the end of the game, the player is informed of the number of ships they sunk.

To run the game, simply execute the Python script. The game will prompt the player to enter their shots below the table.


# Table of contents
- User Experience
    - Project goals
    - User stories
    - Flowchart
- Technologies used
    - Languages
    - Programs, frameworks
- Testing
    - Testing user stories
    - Code validation
    - Manual testing
- The finished Game
- Bugs
- Deployment
- Credits
    - Content
    - Acknowledgements

# User Experience


## Project Goals

Create a graphical interface for the game that includes a playing rid. Generate a random arrangement of ships on the playing grid. Provide feedback to the user about whether their guess was a hit or miss. Keep track of the number of turns it takes the user to find all the ships. Allow the user to play again with a new random arrangement of ships.


## User Stories

- As a user I want to be able to start the game.
- As a user I want to be able to informed about the game and rules.
- As a user I want to be able mark my shots on the table. 
- As a user I want to be able to know how many ships are on the table.
- As a user I want to be able to know how many shot I have.
- As a user I want to be able to know how many shots left
- As a user I want to be able to informed if my shot is hit or missedd a ship.
- As a user I want to be able to check how many ships shunk.
- As a user I want to be able to restart the game.
   

## Flowchart

To create the program flowchart [Miro](https://miro.com/) has been used.
|              |                                                            |
| ----------------- | ------------------------------------------------------------------ |
| Flowchart   | ![Flowchart](https://res.cloudinary.com/duxsycizt/image/upload/v1681083582/battleships-game/My_First_Board_uapqvs.jpg)  |
|              |                                                            |



# Technologies Used

## Languages

- [Python3](https://en.wikipedia.org/wiki/Python_(programming_language))

## Programs, Frameworks
 
 - [Cloudinary](https://cloudinary.com/?&utm_campaign=1329&utm_content=instapagelogocta-selfservetest)
 - [GitPod](https://gitpod.io/)
 - [GitHub](https://github.com/)
 - [Heroku](https://id.heroku.com/) was used to deploy the application.
 - [Miro](https://miro.com/) was used to create the program flowchart.
 - [CI Python Linter](https://pep8ci.herokuapp.com/) was used to validate the Python code for PEP8 requirements.
 
 
# Testing

- As a user I want to be able to start the game.
- As a user I want to be able to informed about the game and rules.
- As a user I want to be able mark my shots on the table. 
- As a user I want to be able to know how many ships are on the table.
- As a user I want to be able to know how many shot I have.
- As a user I want to be able to know how many shots left
- As a user I want to be able to informed if my shot is hit or missedd a ship.
- As a user I want to be able to check how many ships shunk.
- As a user I want to be able to restart the game.



## Code validation

The [CI Python Linter](https://pep8ci.herokuapp.com/) (from Code Institute) was used continuosly during the development proces to validate the Python code for PEP8 requirements. For this reason no before and after snapshots are available. 

![Python Code](https://res.cloudinary.com/duxsycizt/image/upload/v1681137605/battleships-game/Screenshot_2023-04-10_153929_usoty3.png)


## Manual Testing

Common Elements Testing

TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Zodiac button | Checked when clicked Zodiac button, quiz startred or not | PASS
Planet button| Checked when clicked Planet button, quiz startred or not | PASS


# The Finished Game

|             |                                                            |
| ----------------- | ------------------------------------------------------------------ |
| Start   | ![Start](https://res.cloudinary.com/duxsycizt/image/upload/v1681078176/battleships-game/Battleship-0_h68nhw.png)  |
| Invalid input    | ![Invalid input](https://res.cloudinary.com/duxsycizt/image/upload/v1681077803/battleships-game/Battleship-5_noyb5h.png)  |
| Missed shot   | ![Missed shot](https://res.cloudinary.com/duxsycizt/image/upload/v1681078041/battleships-game/Battleship-6_ayuxtc.png)  |
| Hit   | ![Hit](https://res.cloudinary.com/duxsycizt/image/upload/v1681138102/battleships-game/Screenshot_2023-04-10_154803_v9r3uf.png)  |
| Final results   | ![Final result](https://res.cloudinary.com/duxsycizt/image/upload/v1681137974/battleships-game/Screenshot_2023-04-10_154541_kdjaly.png)  |





You can visit the deployeded website [here](https://battleships-game11.herokuapp.com/).

# Bugs

## Solved bugs
- At the beginning of the work the ships (S) were not invisible, but solved.
- I had many warning messages but most of them coming from the template so I changed the variable names, after that the warnings are gone.
- During the work I used [CI Python Linter](https://pep8ci.herokuapp.com/) and followed the instructions from the website but couple of instructions are doesn't worked well -like the whitespaces- so I ignored it otherwise the table looks bad. 
- I tried to use bare 'except' code but I had problem with that, after it I found how can I use it without error message.
- I missed a couple of whitespaces and tabs but solved during the work.
- At the end of the game the final result was incorrect, when I found the problem I solved.
- The last shot was missed from the table than I realized, the last table with all shots (10) missing but solved.

## Unsolved bugs
No bugs remaining

# Deployment

The project has been deployed using [Heroku](https://id.heroku.com/) using the following steps:
1. Sign up to Heroku's website.
2. On Heroku dashboard click "Create new app".
3. Enter the "App name" and "Choose a region" than coose "Create app".
4. Go to the settings and add "Config Var" (Key: PORT, Value: 8000)
5. At the settings "Add buildpacks" select "python" and "node.js" than "Save changes".
6. Go to the "Deployment method" under the "Deploy" tab select "GitHub" than "Connect to GitHub".
7. Go to the "Connect to GitHub" section and "Search" the repostory to be deployed than "Connect".
8. Choose "Automatic deploys" or "Manual deploys" to deploy your application.

# Credits

## Content

- How to code battleship in Python [Youtube](https://www.youtube.com/watch?v=tF1WRCrd_HQ)
- [Slack Community](https://slack.com/intl/en-ie/) used and consulted for inspiration.
- All content was written by the developer.


## Acknowledgements

 - [Code Institute](https://codeinstitute.net/ie/)
 - [YouTube - tutorials ](https://www.youtube.com/)
 - [Slack Community](https://slack.com/intl/en-ie/) 