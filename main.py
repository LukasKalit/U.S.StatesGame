import turtle
import os.path
import pandas
from writing_on_screen import pen

# screen init
screen = turtle.Screen()
screen.setup(width=725, height=491)
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

pen = pen()

# downloading states names
country_data = pandas.read_csv("50_states.csv")
df = pandas.DataFrame(country_data)
print(df)

# creating or reading a list quested states and saving a progress.
missing_states_list = []
if os.path.isfile("progress.csv"):
    missing_states = pandas.read_csv("progress.csv")
    missing_states_list = missing_states.States.to_list()
    print(missing_states_list)
    for item_in_list in missing_states_list:
        print(missing_states_list)
        for state in df["state"]:
            if state == item_in_list:
                print(state)
                print(item_in_list)
                selected_row = (df[df["state"] == state])
                selected_cell_x = selected_row["x"]
                selected_cell_y = selected_row["y"]
                pen.write_country(state, int(selected_cell_x), int(selected_cell_y))

states_answered = len(missing_states_list)

# main loop
while True:
    answer_state = screen.textinput(title=f"{states_answered}/{len(df)} Guess the State",
                                    prompt="What's another state's name?")
    if answer_state == "exit":
        save_file = pandas.Series(missing_states_list, name="States")
        print(save_file)
        save_file.to_csv("progress.csv", index=False)
        break
    elif answer_state in missing_states_list:
        pass
    else:
        for state in df["state"]:

            if state == answer_state:
                selected_row = (df[df["state"] == state])
                selected_cell_x = selected_row["x"]
                selected_cell_y = selected_row["y"]
                missing_states_list.append(state)

                pen.write_country(state, int(selected_cell_x), int(selected_cell_y))
                print("i do it")
                states_answered += 1

screen.exitonclick()
