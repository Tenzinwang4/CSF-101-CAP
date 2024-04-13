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


# Read the input.txt file
def read_input(Input_your_file_name): #Define read_input func.
    x = [] #Empty list
    with open(Input_your_file_name, 'r') as files:#
        for y in files:
            opponent_choice, outcome = y.split()
            x.append((opponent_choice, outcome))
    return x #Return list x

# Calculating the score for each round
def calculate_score(Total_Number_of_rounds):
    Points = 0
    for opponent_choice, outcome in Total_Number_of_rounds:
        if outcome == 'X':  # Defeat
            if opponent_choice == 'A':
                Points += 3  #  Paper defeats Rock
            elif opponent_choice == 'B':
                Points += 1  # Scissors defeats Paper
            elif opponent_choice == 'C':
                Points += 2  # Rock defets sicssor
        elif outcome == 'Y':  # Draw
            if opponent_choice == 'A':
                Points += 4  # same shape so it's a draw
            elif opponent_choice == 'B':
                Points += 5  # same shape so it's a draw
            elif opponent_choice == 'C':
                Points += 6  # Same shape so it's a draw
        elif outcome == 'Z':  # winner
            if opponent_choice == 'A':
                Points += 8  # Paper defeats rock
            elif opponent_choice == 'B':
                Points += 9  # Scissor defeats paper
            elif opponent_choice == 'C':
                Points += 7  # Rock defeats scissor
    print(f"The total score is:{Points}") #outcome will print your total score is _____

# To run a program
Input_your_file_name = "CSF-101-CAP/input_8_cap1.txt"
calculate_score(read_input(Input_your_file_name))



