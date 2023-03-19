#For the TV series “Game of Thrones,” an extensive cast of actors was put to work.
#Not only is this series one of the most watched of all time but a lot of merchandize
#has also found its way into the market. Moreover, several games have been launched
#allowing the player to assume the role of one of the lead characters and experience adventures.
#Write a script that displays one of the main characters of the series and asks the user
#which actor played the role. The programmer can choose to either display the actors’
#names and let the player chose one or to not display any options at all.
#The actors and characters are listed in the following table:

#Actor                       Character
#Sean Bean                  Ned Stark
#Mark Addy                  Robert Baratheon
#Nikolaj Coster-Waldau      Jaime Lannister
#Michelle Fairley           Catelyn Stark
#Lena Headey                Cersei Lannister

#After each question, the player is informed if their answer was correct. The game is
#finished when the user has linked five actors to five characters correctly. At the end of the
#game, the number of correct guesses is displayed on the screen.

def Game_OF_Thrones_Game():
    Game_Of_Thrones = {"Sean bean" : "Ned Stark" , "Mark Addy" : "Robert Baratheon",
                       "Nikolaj Coster-Waldau" : "Jaime Lannister", "Chelle Fairlady" : "Catelyn Stark" ,
                       "Lena Headey" : "Cersei Lannister"}
    print("The aim is to guess which actors played which characters")
    User_Input = input("Who played Ned Stark? ")
    while User_Input != "Sean Bean":
        User_Input = input("Who played Ned Stark? ")
    User_Input_1 = input("Who Played Robert Baratheon? ")
    while User_Input_1 != "Mark Addy":
        User_Input_1 = input("Who Played Robert Baratheon? ")
    User_Input_2 = input("Who Played Jaime Lannister? ")
    while User_Input_2 != "Nikolaj Coster-Waldau":
        User_Input_2 = input("Who Played Jaime Lannister? ")
    User_Input_3 = input("Who played Catelyn Stark? ")
    while User_Input_3 != "Michelle Fairley":
        User_Input_3 = input("Who played Catelyn Stark? ")
    User_Input_4 = input("Who played Cersei Lannister")
    while User_Input_4 != "Lena Headey":
        User_Input_4 = input("Who played Cersei Lannister")


Game_OF_Thrones_Game()