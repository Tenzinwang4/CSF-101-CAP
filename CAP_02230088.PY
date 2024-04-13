################################
# Tenzin Wangyel
# Bachelors of Engineering in Electrical Engineering (EE)
# 02230088
################################
# REFERENCES
# @CHAT_GPT
# https://www.mastersportal.com/search/master/information-technology/united-kingdom
################################
# SOLUTION
# The Solution Score:49843
# input_8_cap1.txt()
###############################
# A for Rock, B for Paper, and C for Scissors.
# X means lose, Y means draw, and Z means win
#Total SCore: 49843
###############################

# For reading the input function file of read_input
def read_input(file_name): 
    A = [] #A Datas to be store as a list
    with open(file_name, 'r') as C:
        for B in C:#USing A for loop to  allign the data
            opponent_choice, outcome = B.split()
            A.append((opponent_choice, outcome))#appending an item in the list
    return A #Returning a stored list A

# Scores are calculated one by one in each round
def calculate_score(Number_of_rounds):
    Points = 0
    for opponent, outcome in Number_of_rounds:
        if outcome == 'X':  # By any means we must be Defeated
            if opponent == 'A':
                Points += 3  #  if oppent choose A we must choose scissors to be defeated
            elif opponent == 'B':
                Points += 1  # if oppent choose B we must choose rock to be defeated
            else:
                Points += 2  #  if oppent choose C we must choose paper to be defeated
        elif outcome == 'Y':  # Draw
            if opponent == 'A':
                Points += 4  # if oppent choose A we must choose rock to get draw
            elif opponent == 'B':
                Points += 5  # if oppent choose B we must choose paper to get draw
            else:
                Points += 6  # if oppent choose C we must choose scissors to get draw
        elif outcome == 'Z':  # oh!victory
            if opponent== 'A':
                Points += 8  # if oppent choose A we must choose Paper to get victory
            elif opponent == 'B':
                Points += 9  # if oppent choose B we must choose scisspr to get victory
            else:
                Points += 7  # if oppent choose C we must choose rock to get victory
    print(f"The total score is:{Points}") #outcome will print your total score is _____

# Function that was called earlier is being executed to find the solution
file_name = "CSF-101-CAP/input_8_cap1.txt"
calculate_score(read_input(file_name))



