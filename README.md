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


# [Table of contents](#table-of-contents)
- [User Experience](#user-experience)
    - Project goals
    - User stories
    - Flowchart
- [Features](#features)
- [Technologies used](#technologies-used)
    - Languages
    - Programs, frameworks
- [Testing](#testing)
    - Testing user stories
    - Code validation
    - Manual testing
- [The finished Game](#the-finished-game)
- [Bugs](#bugs)
- [Deployment](#deployment)
- [Credits](#credits)
    - Content
    - Acknowledgements

# User Experience


## Project Goals

Create a graphical interface for the game that includes a playing rid. Generate a random arrangement of ships on the playing grid. Provide feedback to the user about whether their guess was a hit or miss. Keep track of the number of turns it takes the user to find all the ships. Allow the user to play again with a new random arrangement of ships.


## User Stories

- As a user, I want to be able to start the game.
- As a user, I want to be informed about the game rules.
- As a user, I want to be able to mark my shots on the table. 
- As a user, I want to know how many ships are on the table.
- As a user, I want to know how many shots I have.
- As a user, I want to know how many shots are left.
- As a user, I want to be informed if my shots  hits or misses a ship.
- As a user, I want to know how many ships have shunk.
- As a user, I want to know where the missed ships are located on the board.
- As a user, I want to be able to restart the game.

[Back to top ⇧](#table-of-contents)
   

## Flowchart

To create the program flowchart [Miro](https://miro.com/) has been used.
|              |                                                            |
| ----------------- | ------------------------------------------------------------------ |
| Flowchart   | ![Flowchart](https://res.cloudinary.com/duxsycizt/image/upload/v1681083582/battleships-game/My_First_Board_uapqvs.jpg)  |
|              |                                                            |

# Features

- Create the grid and placed the ships on the grid.
- Target input
    - Collect the target information (x, y coordinate) from the user.
- Target input check
    - Check if the input is valid or not. Valid if the numbers between 0 and 9 and space used between the values. 
- Target output. 
    - Print the shot on the board.
    - Print X if hit.
    - Print O if miss.
- Counting the shots
    - Number of shots 10, the game is over if the player used all the shots.
- Display the final results
    - After the last shot the final results display, with the missed ships
    - The player win if hit all the ships.
- Restart
    - The player able to restert the game, the final massege assist.

[Back to top ⇧](#table-of-contents)

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
 - [Pythonchecker](https://www.pythonchecker.com/)
 
[Back to top ⇧](#table-of-contents)

# Testing

## Testing user stories

- As a user I want to be able to start the game.
    - To start the game, simply execute the Python script.
- As a user I want to be informed about the game rules.
    - At the beginning of the game, the user is provided with information about the game and rules.
- As a user I want to be able to mark my shots on the table. 
    - The process of marking shots is easy and the user is provided with text instructions. The player has to enter the x and y coordinates of their shot (separated by a space).
- As a user, I want to know how many ships are on the table.
    - At the beginning of the game, the user is informed about the number of ships on the board (5).
- As a user, I want to know how many shots I have.
    - At the beginning of the game, the user is informed about the numbers of shots available during the game (10).
- As a user, I want to know how many shots are left.
    - The user is informed during the game and check how many shots are left at the bottom of the board.
- As a user I want to be informed if my shots  hits or misses a ship.
    - There are two ways to check whether the shot hit or missed. On the board, the player can see "X" if it's a hit, and "O" if it's a missed shot. These instructions are also provided at the beginning of the game. The user is also informed after each shot with a message: "Hit!" if the shot hits, or "Miss!" if it misses.
- As a user I want to know how many ships have shunk.
    - At the end of the game, the user can check how many ships have sunk.
- As a user I want to know where the missed ships are located on the board.
    - At the end of the game the user can check the last board to see the locations of the enemy ships. The missed ships are marked as "S" and the sunk ships are marked as "X".
- As a user, I want to be able to restart the game.
    - The process to restart the game is easy:  the user can simply click "Run program" whenever they want to restart the game.



## Code validation

The [CI Python Linter](https://pep8ci.herokuapp.com/) (from Code Institute) was used continuosly during the development proces to validate the Python code for PEP8 requirements. For this reason no before and after snapshots are available. 

![Python Code](https://res.cloudinary.com/duxsycizt/image/upload/v1681137605/battleships-game/Screenshot_2023-04-10_153929_usoty3.png)



## Manual testing

<table>
    <tr>
        <th>FEATURE</th>
        <th>OUTCOME</th>
        <th>EXAMPLE</th>
        <th>PASS/FAIL</th>
    </tr>
    <tr>
        <td>Start game</td>
        <td>Checked when clicked 'Run Program' button, the program started or not</td>
        <td><img src=https://res.cloudinary.com/duxsycizt/image/upload/v1681150418/battleships-game/Bship-start_lhidb0.png alt="Start game"></td>
        <td>Pass</td>
    </tr>
    <tr>
        <td rowspan=7>Target selection</td>
        <td>Validate if value is empty</td>
        <td><img src=https://res.cloudinary.com/duxsycizt/image/upload/v1681408362/battleships-game/Scr-invalid_mroiqi.png alt="Value is empty"></td>
        <td>Pass</td>
    </tr>
    <tr>
        <td> Validate if value is letter</td>
        <td><img src=https://res.cloudinary.com/duxsycizt/image/upload/v1681408640/battleships-game/Scr-letter_rohkv3.png alt="Value is letter"></td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>Validate if value is invalid number</td>
        <td><img src=https://res.cloudinary.com/duxsycizt/image/upload/v1681409373/battleships-game/Scr-invalid3_kkcxmx.png alt="Value is invalid"></td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>Validate if value isn't contain space</td>
        <td><img src=https://res.cloudinary.com/duxsycizt/image/upload/v1681408975/battleships-game/Scr-notspace_eqgwzg.png alt="Value is not contain space"></td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>Validate if value is not a number</td>
        <td><img src=https://res.cloudinary.com/duxsycizt/image/upload/v1681409138/battleships-game/Scr-notnumber_sv50yn.png alt="Value is not number"></td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>Validate if value is too high</td>
        <td><img src=https://res.cloudinary.com/duxsycizt/image/upload/v1681409223/battleships-game/Scr-toohigh_gbuiwt.png alt="Value is too high"></td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>Validate if value is too low</td>
        <td><img src=https://res.cloudinary.com/duxsycizt/image/upload/v1681408876/battleships-game/Scr-invalid2_trwqhe.png alt="Value is too low"></td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>Finished game</td>
        <td>Checked when game over the results are adequate</td>
        <td><img src=https://res.cloudinary.com/duxsycizt/image/upload/v1681410681/battleships-game/Scr-end_onba2b.png alt="Game over results"></td>
        <td>Pass</td>
    </tr>
</table>

[Back to top ⇧](#table-of-contents)

# The Finished Game

|             |                                                            |
| ----------------- | ------------------------------------------------------------------ |
| Start   | ![Start](https://res.cloudinary.com/duxsycizt/image/upload/v1681150418/battleships-game/Bship-start_lhidb0.png)  |
| Invalid input    | ![Invalid input](https://res.cloudinary.com/duxsycizt/image/upload/v1681150478/battleships-game/Bship-invalid_dpcepz.png)  |
| Invalid input    | ![Invalid input4](https://res.cloudinary.com/duxsycizt/image/upload/v1681412642/battleships-game/final4_rywm9z.png)  |
| Empty input | ![Invalid input1](https://res.cloudinary.com/duxsycizt/image/upload/v1681412250/battleships-game/final1_wy0ucf.png)  |
| Invalid numbers | ![Invalid input2](https://res.cloudinary.com/duxsycizt/image/upload/v1681412431/battleships-game/final2_n7ffnj.png)  |
| Invalid numbers | ![Invalid input3](https://res.cloudinary.com/duxsycizt/image/upload/v1681412527/battleships-game/final3_so9ubw.png)  |
| Missed shot   | ![Missed shot](https://res.cloudinary.com/duxsycizt/image/upload/v1681150506/battleships-game/Bship-miss_cjxgit.png)  |
| Hit   | ![Hit](https://res.cloudinary.com/duxsycizt/image/upload/v1681150528/battleships-game/Bship-hit_k5vhie.png)  |
| Final results   | ![Final result](https://res.cloudinary.com/duxsycizt/image/upload/v1681410950/battleships-game/Scr-final_i15hev.png)  |



You can visit the deployeded website [here](https://battleships-game11.herokuapp.com/).

[Back to top ⇧](#table-of-contents)

# Bugs

## Solved bugs
- At the beginning of the work the ships (S) were visible instead of invisible, but I fixed it later.
- I received several warning messages but most of them coming from the template, so I changed the variable names, and the warnings disappeared.
- At the beginning of the work I used [Pythonchecker](https://www.pythonchecker.com/) and followed the instructions from the website. However, some instructions did not work well, like the whitespaces, so I ignored them; othervise, the table woukd look bad. 
- I tried to use bare 'except' code but I encountered some problems. Later, I found out how to use it without any error messages.
- I missed a few whitespaces and tabs, but I resolved them during the work.
- At the end of the game, the final result was incorrect. However, I found the problem and fixed it. 
- I noticed that the last shot was missing from the table. I added it to the last table that displayed all the shots that were missed. 

## Unsolved bugs
No bugs remaining

[Back to top ⇧](#table-of-contents)

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

[Back to top ⇧](#table-of-contents)

# Credits

## Content

- How to code battleship in Python [Youtube](https://www.youtube.com/watch?v=tF1WRCrd_HQ)
- [Slack Community](https://slack.com/intl/en-ie/) used and consulted for inspiration.
- All content was written by the developer.


## Acknowledgements

 - Marcel Mulders mentor
 - [Code Institute](https://codeinstitute.net/ie/)
 - [YouTube - tutorials ](https://www.youtube.com/)
 - [Slack Community](https://slack.com/intl/en-ie/) 

 [Back to top ⇧](#table-of-contents)