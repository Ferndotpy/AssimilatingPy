# CS50P's Final Project - Póquer Game
#### This repo represents all the knowledge gained and applied throughout the CS50P course by Harvard University.
### These are the final results of this project: [Video Demo](https://www.youtube.com/watch?v=wJSSXFlwmxA) & [CS50P certificate](https://certificates.cs50.io/6329b323-052f-4d3a-b1eb-59c9b8decb9b.pdf?size=letter).
### Source Materials: [Course Playlist](https://www.youtube.com/playlist?list=PLhQjrBD2T3817j24-GogXmWqO5Q5vYy0V) | [Course Website](https://cs50.harvard.edu/python/2022/) | [Help Guide 1](https://www.youtube.com/watch?v=rfscVS0vtbw&list=WL&index=23&t=2297s) | [Help Guide 2](https://www.youtube.com/playlist?list=PLOLrQ9Pn6cazZScthXI-gMQv-YrDUMnlY)
### What is this project and why?
#### This program was made to represent a game of poker, mainly focused on the variant Texas hold'em. It tries to replicate most of the rules but is way more simplified, not all actions were included: no BID action and no FOLD action. The purpose of picking this topic is the range of options that opens, I mean if I'd like to learn about statistics I'd start from this game and try to add it, this also applies to learn about GUIs and ML.
### What does this program actually do?
#### The terminal will show the symbol and suit for each card as their visual representation. The program expects from the user/the player/you to enter a name and a number of players (2-10), so you can all play against each other (you and 'n-1' CPU). This program simulates one round for each execution and does not have a counter.
#### The player can execute 2 actions once the round has begun: CHECK (end of the round, it's mandatory if the board has 5 cards) and RAISE (add 1 more card to the board from the deck). The player can only see his cards and the board until the CHECK; at the moment of the CHECK action, the player will see all the cards (used for the best hand and the rest) and the hand type of each CPU player to verify the legitimacy of the program.
### Summary
#### These are the actions/ideas implemented to code this program, you can find in the project.py some comments related to each of these points.
#### 1. Determinate n° of players, from 2 to 10.
#### 2. Set the deck and shuffle it, absolute randomness.
#### 3. Deal 2 cards for each player in 2 rows of 1 at the time.
#### 4. Set the board with the community cards, at the start w/ 3 cards and then give the option to add 1 more card, max 2.
#### 5. Group all the cards from the board and from each hand for each player.
#### 6. Set the best hand for each player according to the hierarchy.
#### 7. In order to determinate the winner, in case the hierarchy it's the same between players, compare the cards. A tie is plausible.
### Content
#### This project contains 4 files.
#### 1. cards.csv → in this file there are all 52 cards defined by their symbol and suit, there's also as first line the keys for each column.
#### 2. cards.py → in this file is defined the class Carta, therefore, all their instance variables and methods implemented to facilitate the crafting of the functions.
#### 3. project.py → in this file there are all the necessary functions to achieve the goal of the project. It's mainly focused in 3 parts; being the first part, the part that determines if a hand (list of objects/Carta, 5 to 7 Carta) is a certain poker hand according to the hierarchy of values, this function is best_hand but it contains all the poker hands functions (10 in total); the second part is the one that uses this result (best_hand) for each player to get what cards (sorted) were used and which were not and thus determine the overall winner, or tie if the situation occurs; and the last part is focused in the main function along with others to set the deck, the amount of players, the distribution of cards, the board and the input's and the print's for the terminal.
#### 4. test_project → in this file each poker hand function is tested by a default hand that meet all the conditions for the function.
####
#### If you're even more interested in some complications, observations, bugs or details that have occurred through this project, you can check the comments within the project.
#### Thanks for for your attention ;D.