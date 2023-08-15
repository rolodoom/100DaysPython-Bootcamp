#######################################
# CLASS PROJECT
# U.S. States Game
#######################################

# Day 25 - 🇺🇲 U.S. States Game 🇺🇲 #100DaysOfCode #100DaysOfCodePython #Python #Bootcamp

import turtle
import pandas

# Load States data
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

# Screen setup
screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(width=725, height=491, startx=100, starty=100)
map_image = "blank_states_img.gif"
screen.addshape(map_image)
turtle.shape(map_image)

# Write correct guesses onto the map
correct_guesses = []

# Keep track of the score
# len(correct_guesses)

# Use a loop to allow the user to keep guessing
while len(correct_guesses) < len(all_states):
    # while len(correct_guesses) < 3:
    # Ask the user to guess a state name and convert the guess to Title case
    answer_state = screen.textinput(
        title=f"[{len(correct_guesses)}/50] States Correct",
        prompt=f"[{len(correct_guesses)}/50] Enter state:",
    ).title()

    # Exit Game
    if answer_state == "Exit":
        missing_states = [
            s for s in all_states if not any(xs in s for xs in correct_guesses)
        ]
        # States to learn
        data_dict = {
            "Learn State": missing_states,
        }
        df = pandas.DataFrame(data_dict)
        df.to_csv("states_to_learn.csv")

        break

    # Check if the guess is among 50 states
    if answer_state in all_states:
        # Only add new answers
        if answer_state not in correct_guesses:
            # Record the correct guesses in a list
            correct_guesses.append(answer_state)

            # Write correct guesses onto the map
            txt = turtle.Turtle()
            txt.hideturtle()
            txt.penup()
            state_data = data[data.state == answer_state]
            txt.goto(int(state_data.x.item()), int(state_data.y.item()))
            txt.write(state_data.state.item())
