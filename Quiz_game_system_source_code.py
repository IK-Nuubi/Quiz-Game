import random #importing the random module


#creating a dictionary for the questions and answers
#the question and answers are in a list as value and numbers was used as unique keys
q_and_a = {1:["What is the capital of Qatar? ", "doha"],
           2:["Which continent in the world would you find Nigeria? ", "africa"],
           3:["Which country currently has the largest population in the world? ", "china"],
           4:["Which continent is France in? ", "europe"],
           5:["What is the name of the planet closest to the sun? ", "mercury"],
           6:["Name the longest river in the world? ", "nile"],
           7:["What is the name of the 4th planet from the sun? ", "mars"],
           8:["Which continent is the coldest in the world? ", "antarctica"],
           9:["In which city would you find the London Bridge? ", "london"],
           10:["What is the name of the 3rd planet from the sun? ", "earth"],
           11:["In which country is the leaning tower of Pisa located? ", "italy"],
           12:["What is the name of the 6th planet from the sun? ", "saturn"],
           13:["In which country is the Acropolis situated? ", "greece"],
           14:["In which country would you find the famous pyramids of Giza? ", "egypt"]
           }


question_list = [] #this creates a list to store the questions each user will answer
users = [] #a list to store the name of each user
users_score = [] #a list to store the score of each user
leader_board = {} #a dictionary to store both the name and score of all users.


#function for the player to select the number of questions they want to answer
def select_questions(no_of_questions):
    n = list(random.sample(range(1, 14), no_of_questions)) #random.sample creates a list of unique numbers from the given range
    question_list.extend(n) #the created list is then added to the question list initially created using the extend function 
    return question_list


#function that runs the game and asks the user questions.
def game(user_name, no_of_questions):
    correct_answer = 0 #to save the number of correct answers
    question_count = 0 #to keep count of the number of questions asked.
    while question_count < len(question_list):
        for each_question in question_list: #for each unique number in the questions list
            answer = input(q_and_a[each_question][0]).lower() #this will pick the unique number from the question_list and match with the identical key from the q_and_a dictionary and return the first value as question
            if answer == q_and_a[each_question][1]: #if the answer provided matches the second value in the list in the dictionary 
                correct_answer += 1 #keeps count of the correct questions answered by the user
                print("CORRECT!")
            else:
                print("Incorrect")
                print("The correct answer is", q_and_a[each_question][1])
            question_count += 1
    users_score.append(correct_answer) #appends the final correct score of the user to the user_score list.
    leader_board[user_name] = correct_answer #inputs the key which is the user's name and value which is the users score to the leader_board dictionary
    percentage_score = (correct_answer / no_of_questions) * 100 #calculates a percentage for the user's score
    print("That will be all for today", user_name)
    print(user_name, "Your Final Score is", correct_answer, "/", no_of_questions, percentage_score,"%")


#function to calculate the max score
def max_score():  
     leader_board_values = list(leader_board.values())
     leader_board_keys = list(leader_board.keys())
     highest_score_player = leader_board_keys[leader_board_values.index(max(leader_board_values))]
     print("Player with the highest score is", highest_score_player)


#function to check if the user or another user wants to play again
def play_again(user_name):
    play_again = input("Would you like to play again?\ninput yes or no ").lower()
    if play_again == "yes":
        question_list.clear() #Clears the question list already selected by the previous user.
        main_game() #function for the main game is called if the user decides to play again.
    else:
        print("Leader Board:", leader_board)
        average_score = sum(users_score) / len(users_score) #calculates the average score
        print("the average score is", average_score)
        max_score()
        print("Thank you for your time, Goodbye")

#function that houses the other functions and runs the main game.
def main_game():
    print("WELCOME PLAYER")
    while True:
        user_name = input("Kindly enter your name: ")
        if user_name != " ": #Stops an empty space being saved to the variable and used as user_name
            users.append(user_name) #adds player's name to the user_name list
            print("Kindly enter the number of questions you want to answer")
            while True:
                no_of_questions = input("enter a number between 8 and 14 ")
                if no_of_questions.isnumeric() == True: #checks if the input is a numeric value
                    no_of_questions = int(no_of_questions) #converts input to integer if numeric
                    if no_of_questions >= 8 and no_of_questions <= 14: #makes certain that only a value between the provided numbers is entered
                        select_questions(no_of_questions)
                        game(user_name, no_of_questions)
                        play_again(user_name)
                        break
            break

#calls the function.
main_game()