import customtkinter as ctk
import tkinter
from tkinter import *
import json
from level2 import Level2

# Selecting GUI theme - dark, light, system (for system default)
ctk.set_appearance_mode("dark")

# Selecting color theme - blue, green, dark-blue
ctk.set_default_color_theme("dark-blue")

# Setting window size and title.
app = ctk.CTk()
app.geometry("1200x1000")
app.title("Cyber Security Awareness Game")

# Reading the data from the json file
with open('data.json') as f:
    data = json.load(f)

# Background image
bg = tkinter.PhotoImage(file="images/circle.png")


def main_window():

    # Create a label for background picture
    bg_label = Label(app, image=bg)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Create custom frame
    frame = ctk.CTkFrame(master=app, width=500, height=500, corner_radius=6)
    frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    header_label = ctk.CTkLabel(master=frame, text="Main Menu", font=('font.ttf', 30))
    header_label.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

    # Create custom buttons
    play_button = ctk.CTkButton(master=frame, width=220, height=40, text="Play", command=play_options, corner_radius=6)
    play_button.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

    scoreboard_button = ctk.CTkButton(master=frame, width=220, height=40, text="Scoreboard", command=scoreboard, corner_radius=6)
    scoreboard_button.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)

    options_button = ctk.CTkButton(master=frame, width=220, height=40, text="Options", command=options_window,
                                   corner_radius=6)
    options_button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    feedback_button = ctk.CTkButton(master=frame, width=220, height=40, text="Feedback", command=app.quit,
                                    corner_radius=6)
    feedback_button.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

    exit_button = ctk.CTkButton(master=frame, width=220, height=40, text="Exit", command=app.quit, corner_radius=6)
    exit_button.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)


def options_window():
    options_frame = ctk.CTkFrame(master=app, width=500, height=500, corner_radius=6)
    options_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    options_frame2 = ctk.CTkFrame(master=options_frame, width=500, height=500, corner_radius=6)
    options_frame2.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    light_button = ctk.CTkButton(options_frame2, text='Light mode', command=lambda: ctk.set_appearance_mode('light'))
    light_button.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

    dark_button = ctk.CTkButton(options_frame2, text='Dark mode', command=lambda: ctk.set_appearance_mode('dark'))
    dark_button.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)

    construction_label = ctk.CTkLabel(options_frame2, text="This page is under construction", font=("font.tff", 30, 'bold'))
    construction_label.place(anchor='nw')

    back_button(options_frame2)


# Setting the score counter variable
score = 0


def button_clicked(button_num, check_answer):
    global score
    if button_num == check_answer:
        score += 1
        play_window()
    else:
        score
        play_window()


counter = 0


def increment_counter():
    global counter
    counter += 1


def reset_counter():
    global counter
    counter = 0


def back_button(window):
    return_button = ctk.CTkButton(master=window, width=220, height=40, text="Main Menu", command=main_window, corner_radius=6)
    return_button.place(relx=0.25, rely=0.9, anchor=tkinter.CENTER)

    quit_button = ctk.CTkButton(master=window, width=220, height=40, text="Quit", hover_color='red', fg_color='darkred', command=app.quit, corner_radius=6)
    quit_button.place(relx=0.75, rely=0.9, anchor=tkinter.CENTER)


def play_options():

    play_options_frame = ctk.CTkFrame(master=app, width=500, height=500, corner_radius=6)
    play_options_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    options_label = ctk.CTkLabel(master=play_options_frame, text="Levels", font=('font.ttf', 30))
    options_label.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

    level1_button = ctk.CTkButton(master=play_options_frame, width=220, height=40, text="Level 1", command=play_window, corner_radius=6)
    level1_button.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

    level2_button = ctk.CTkButton(master=play_options_frame, width=220, height=40, text="Level 2", command=level2_window, corner_radius=6)
    level2_button.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

    back_button(play_options_frame)


def level2_window():

    new_frame = ctk.CTkFrame(master=app, width=750, height=750, corner_radius=6)
    new_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    level2_frame = ctk.CTkFrame(master=new_frame, width=750, height=750, corner_radius=6)
    level2_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    Level2(level2_frame)

    back_button(new_frame)


def play_window():

    questions = question()
    alternatives = options()
    correct = correct_answers()
    play_frame = ctk.CTkFrame(master=app, width=750, height=750, corner_radius=6)
    play_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    if counter < len(questions):

        questions_frame = ctk.CTkFrame(master=play_frame, width=750, height=150, corner_radius=6)
        questions_frame.place(relx=0.5, rely=0, anchor=tkinter.N)
        questions_label = Label(questions_frame, text=questions[counter], font=("font.tff", 25, 'bold'))
        questions_label.place(x=0, y=0, relwidth=1, relheight=1)

        back_button(play_frame)

        option_1 = ctk.CTkButton(master=play_frame, width=260, height=140, text=alternatives[counter][0], command=play_window, corner_radius=6)
        option_1.place(relx=0.3, rely=0.4, anchor=tkinter.CENTER)
        option_2 = ctk.CTkButton(master=play_frame, width=260, height=140, text=alternatives[counter][1], command=play_window, corner_radius=6)
        option_2.place(relx=0.7, rely=0.4, anchor=tkinter.CENTER)
        option_3 = ctk.CTkButton(master=play_frame, width=260, height=140, text=alternatives[counter][2], command=play_window, corner_radius=6)
        option_3.place(relx=0.3, rely=0.6, anchor=tkinter.CENTER)
        option_4 = ctk.CTkButton(master=play_frame, width=260, height=140, text=alternatives[counter][3], command=play_window, corner_radius=6)
        option_4.place(relx=0.7, rely=0.6, anchor=tkinter.CENTER)

        option_1.configure(command=lambda: button_clicked(1, correct[counter-1]))
        option_2.configure(command=lambda: button_clicked(2, correct[counter-1]))
        option_3.configure(command=lambda: button_clicked(3, correct[counter-1]))
        option_4.configure(command=lambda: button_clicked(4, correct[counter-1]))

        increment_counter()

    else:
        #result_frame = ctk.CTkFrame(master=play_frame, width=750, height=750, corner_radius=15)
        #result_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        result_label = ctk.CTkLabel(play_frame, text=f'Your final score is:\n{score}', font=("font.tff", 50, 'bold'))
        result_label.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        player_entry = ctk.CTkEntry(play_frame, width=260, height=50, placeholder_text="Enter your name:")
        player_entry.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)
        #player_entry.bind('<Return>', lambda event: self.get_user_input())
        back_button(play_frame)
        reset_counter()


def player():
    user_frame = ctk.CTkFrame(master=app, width=750, height=750, corner_radius=6)
    user_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    username = ctk.CTkEntry(master=user_frame, width=220, placeholder_text='Username')
    username.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)
    password = ctk.CTkEntry(master=user_frame, width=220, placeholder_text='Password')
    password.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)
    login = ctk.CTkButton(master=user_frame, width=220, text='Login', corner_radius=6)
    login.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)


def scoreboard():
    pass


def feedback():
    pass


def options():
    option = (data['options'])
    return option


def correct_answers():
    answers = (data['answers'])
    return answers


def question():
    questions = (data['questions'])
    return questions


main_window()

if __name__ == '__main__':
    app.mainloop()

