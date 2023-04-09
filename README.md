# BATTLESHIPS GAME

![Battleships Game](https://res.cloudinary.com/duxsycizt/image/upload/v1681071164/battleships-game/Screenshot01_zctbai.png) 

## Introduction
This is a simple implementation of the Battleships game in Python. The game is played on grids on which each player's fleet of battleships are marked. The locations of the fleets are concealed from the other player. Players call shots at the other player's ships, and the objective of the game is to destroy the opposing player's fleet.


# Table of contents
- User Experience
    - Project goals
    - User stories
    - Wireframes
- Features
    - Categories
- Technologies used
    - Languages
    - Programs, frameworks
- Testing
    - Testing user stories
    - Code validation
    - Manual testing
- The finished Website
- Bugs
- Deployment
- Credits
    - Content
    - Media
    - Acknowledgements

# User Experience


## Project Goals

- The game is


## User Stories

- As a user I want to be able to start the game.
- As a user I want to be able to enter a grid size at the beginning of the game.
- As a user I want to be able to enter a number of ships at the beginning of the game.
- As a user I want to be able to informed if my shot is a miss or a hit.
- As a user I want to be able to check the correct/incorrect answers.
- As a user I want to be able to check the computer shots are miss or hits.
- As a user I want to be able to check who is the winner.
- As a user I want to be able to restart the game.
   

## Wireframes

To design the website structure [Adobe Photoshop](https://www.adobe.com/ie/products/photoshop/free-trial-download.html) has been used.

### Desktop appearance 
|              |                                                            |
| ----------------- | ------------------------------------------------------------------ |
| Index   | ![Index](https://res.cloudinary.com/)  |
| Quiz   | ![Quiz](https://res.cloudinary.com/)  |



# Features

- Simple, clear color scheme and responsive design.



### Results
- The results show the numbers of the correct and incorrect answers at the end of the quiz.

    ![Scores](https://res.cloudinary.com/)

### Next
- The next button helps to move for the next question. The button pops up when the user choose an answer.

    ![Next](https://res.cloudinary.com/duxsycizt/image/upload/v1678315065/zodiac-quiz/Next_xziz5m.png)



# Technologies Used

## Languages

- [Python3](https://en.wikipedia.org/wiki/Python_(programming_language))

## Programs, Frameworks
 
 - [Cloudinary](https://cloudinary.com/?&utm_campaign=1329&utm_content=instapagelogocta-selfservetest)
 - [GitPod](https://gitpod.io/)
 - [GitHub](https://github.com/)
 - [Heroku](https://id.heroku.com/) was used to deploy the application.
 - [Miro](https://miro.com/) was used to create the program flowchart.
 
 
# Testing

- As a user I want to be able to start the game.
- As a user I want ot be able mark my shots on the table. 
- As a user I want to be able to informed if my shot is a miss or a hit.
- As a user I want to be able to check how many ships shunk.
- As a user I want to be able to restart the game.



## Code validation

- The [PEP8 online check](http://pep8online.com/) was used continuosly during the development proces to validate the Python code for PEP8 requirements. For this reason no before and after snapshots are available. 

![Python Code](https://res.cloudinary.com/)


## Manual Testing

- The website has been tested on the following browsers and no appearance, responsiveness or functionality issues:
    - [Google Chrome](https://www.google.com/chrome/?brand=YTUH&gclid=Cj0KCQiAic6eBhCoARIsANlox86hgZbgr7LezxlhgcxIVG3unaCJ9euD76PGf5Ny3KPmZ6MhmI5FDYMaAn6oEALw_wcB&gclsrc=aw.ds)
    - [Mozilla Firefox](https://www.mozilla.org/hu/firefox/new/)
    - [Microsoft Edge](https://www.microsoft.com/en-us/edge?exp=e507&form=MA13FJ)
    - [Safari](https://www.apple.com/safari/)


- Common Elements Testing

TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Zodiac button | Checked when clicked Zodiac button, quiz startred or not | PASS
Planet button| Checked when clicked Planet button, quiz startred or not | PASS


# The Finished Website

## Desktop appearance
|             |                                                            |
| ----------------- | ------------------------------------------------------------------ |
| Index   | ![Index](https://res.cloudinary.com/duxsycizt/image/upload/v1678400856/zodiac-quiz/screen-pc1-1_vyhroc.png)  |
| Username required   | ![Username required](https://res.cloudinary.com/duxsycizt/image/upload/v1678400856/zodiac-quiz/screen-pc2-1_y3fl6a.png)  |



You can visit the deployeded website [here](https://battleships-game11.herokuapp.com/).

# Bugs

- I try to use bare except code but I had problem with that, after it I found how can I use it without error message.

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

- All content was written by the developer.

## Acknowledgements

 - [Code Institute](https://codeinstitute.net/ie/)
 - [YouTube - tutorials ](https://www.youtube.com/)
 - [Slack Community](https://slack.com/intl/en-ie/) 