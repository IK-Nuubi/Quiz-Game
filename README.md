# Quiz-Game
A Console based quiz game built using Python
I was tasked with designing, implementing, and testing a small console-based quiz game in python. The quiz should ask the user(s) 10 questions. I was also tasked to include the below in the game:
1.	Asks the user their name
2.	Runs through all questions of the quiz and keep a running score of the number of correctly questions answered.
3.	Once the users have answered all the questions, the system should print out their score out of 10 as well as a percentage score on the screen.
4.	The program should then prompt to ask if anybody else wants to take the quiz. It should then perform steps 1-4 again for the next user.
5.	Once all the users have finished the quiz, the program displays the following:
a.	The name of the user with the highest score (as well as the scores for other users).
b.	The average score of all users.
6.	You should make use of conditional statements, iterative statements, functions, data structures etc. in your program.
7.	Your program should suitably handle user errors (e.g., incorrect input type, such as empty answer or name etc.).
Also, to implements the following additional features:
1.	You can produce a quiz which can ask any number of questions (i.e., not always 10 questions, where users can specify the number of questions they want to answer).
2.	You can ask the questions in a random order.
3.	The user is shown which questions they got correct and which they got incorrect (as well as showing the correct answer for any questions they answered incorrectly).
 
METHODOLOGY
To achieve the design and implementation of this project, one must first understand how object oriented programming works since python is an object oriented programming language. We need to understand the various characteristics of object programming concepts which includes:
1.	Encapsulation
2.	Abstraction
3.	Inheritance
4.	Polymorphism
With the above in mind, we set out to design the project using the tools available to us which include:
1.	Import
2.	Modules
3.	Functions
4.	Lists
5.	Dictionaries
6.	Variables
7.	Loops
8.	Classes (Range) 
The following steps were taken to implement the design:
1.	Import random: This was done to bring in the random module into our code as I planned on using functions in the module which would not be possible if I do not import random into the code.
2.	Created 2 dictionaries, One to store our questions and the second to store the name and score of all the users and present it as a leader board at the end of the game.
3.	Created multiple lists to store the values from the game like the username and score of each user
4.	Created multiple functions to do implement different purposes throughout the code.
5.	Used for loops, while loops and if statements to execute a set of statements. 
6.	Used multiple inbuilt functions such as print.
7.	Used multiple inbuilt methods such as extend, lower, append, clear.
TESTING:
Testing the code:
A simple testing method was carried out where I broke the whole code into bits and checked them for errors to make sure of their functionality. After which I then brought the whole codes together, looking for errors in them and regularizing where necessary. I started this by checking:
1.	The q_and_a dictionary: This is where I stored the questions and answers of my quiz. I initially wanted to make two lists of questions and answers because when I first made the dictionary I struggled with making my questions appear randomly. I instead was able to put my values into a list in a dictionary thereby making it easy to create unique traceable keys for the dictionary.
2.	Created the lists; question_list to store my questions that’ll pick from the list, users to save the name of each player of the game and user_score to store the score of each player. I tested out these lists and variables using the print function to print out the contents of the lists after each player had played the game.
3.	Created a leader_board dictionary where I stored the name of each player as key and then stored the score as value. This was also tested using the print function.
4.	Select_questions function: This made a function that selects the number of questions the user wanted to ask. Creates a list of unique numbers from that range of numbers using random.shuffle and saving it in the earlier created questions_list list.
5.	Game function: This is where the questions are then picked out from the q_and_a dictionary. This is done by looping through each value in the questions_list and matching it with a key in the q_and_a dictionary. When matched it then returns the first value of the list of values and asks that as a question.
The answer is then checked against the second value of the list of values of that same key.
If correct, 1 is added to the correct answer variable already created to keep score.
6.	Play_again function: This function checks to see if the user or another user wants to play again and calls the main_game function if the answer is yes.
Testing this code I realised that if a new user decided to play again and selected another set of questions, it will ask him a total number of the questions already selected by the old user and the ones the new user selected. This was mitigated by using a .clear method to clear the list once a new game was to be played.
7.	Main_game function: This function welcomes the player to the game and calls the other functions for the game to start running only after a player has entered a name. The input was tested as I noticed that an empty space could be saved in the variable. To avoid that I used a while loop to keep asking the user to only enter a name until the user does.
I also noticed while testing that any number would bring out a question as I did not want any user answering any less than 8 questions. I was able to resolve that using another while loop.
Another error came up if a letter was inputted when input asked for a number instead. I checked that by using the .isnumeric method to check if the value inputted is numeric else the user inputs till he inputs a numeric value.

CHALLENGES FACED:
Most of the challenges I faced were in figuring out the while loops. Also made sure the inputs accepted only what was necessary and converted to the correct values the code needed to function with and not throw up a value error.
