from tkinter import *
import tkinter.font as tkFonts
import tkinter.messagebox as tkmessagebox
import itertools as it
import sys

mark = 0  # Counter for the X/O changing term
buttons_list_text = []  # stores name of the button
buttons_info = []  # stored information of the buttons clicked
button_names = []  # Stores the Id of the buttons
pressed_button_names = []  # stores the clicked button name
click_counter = 0  # Stores the Number of clicks Performed
custom_button_name = []  # Stores the Cutomized name for the button  ie. 0-8
winner_name = " "  # Stores Winner's name
display_data = " X"  # Display option x/o on hover
player_1 = None  # Textbox for the name retrival of the player 1
player_2 = None  # Textbox for the name retrival of the player 2
empty_field = " "

class Controls:  # Controls class is the backhand of the program it controls the activities.
    def __init__(self, root):  # Class Initialization
        """Control Section of the Game"""
        self.widget = None
        self.master = root
        self.__game_mode = "Contol section"

    def condition_check(
            self):  # Generates pattern of the button clicked in the screen and send data for conformation of the winner_pos
        global winner_data, player_1, player_2
        button_permutation = it.permutations(buttons_info,
                                             3)  # Generates the random permutation in range 3 for given buttons

        for check_val in button_permutation:  # Condition varification for Winner verification
            init_str = " "
            check_button_name = " "
            specific_seq = []
            for individual_buttons in check_val:  # Nested loop for value addition and pressed buttton list generation
                init_str += individual_buttons["text"]
                check_button_name += individual_buttons.winfo_name()
                specific_seq.append(individual_buttons.winfo_id())
                init_str = init_str.lower()

            x_3 = init_str.find("xxx")  # Checks if the input has "xxx" Character on it
            o_3 = init_str.find("ooo")  # Checks if the input has "ooo" character o nit.

            if x_3 == 1 or o_3 == 1:  # Checking random generated button text consists "xxx" or "ooo" as the combination of 3 buttons or not
                winner_data = player_1.get() if x_3 == 1 else player_2.get()
                Controls.verify_win(self, specific_seq)

            if len(
                    pressed_button_names) == 9:  # This checks whether if buttons pressed are 9 and no one has won the game.
                Graphical.drawdialogbox(self)  # Calls drawdailogbox function located in Graphical class
                sys.exit()

    def verify_win(self, pair_3_buttn):  # Pattern matching section and
        get_data_list = []
        winner_choice = [[0, 1, 2], [1, 4, 7], [2, 5, 8], [0, 4, 8], [6, 4, 2], [0, 3, 6], [3, 4, 5], [6, 7, 8]]

        for buttn in pair_3_buttn:  # Creates the random list of length 3 so the to check if the pattern matechs the choice defined
            get_data_list.append(button_names.index(buttn))

        for dat in winner_choice:  # Final winner condition matching
            if get_data_list == dat:
                Graphical.winnerdialog_box(self)
                sys.exit()

    # Button and Mouse Configuration
    def disable_widget(
            self):  # Disabled the button widget if clicked once and sets text on the button as well. Called by blind method when left mouse button is clicked
        global mark, click_counter, empty_field  # makes variable global

        if player_1.get() == "" and player_2.get() == "":  # These checks if the name field are left black or not
            empty_field = "Player 1 and Player 2 Name"
            Graphical.showwarning_dialog(self)  # Calls showwarning method of Graphical class if condition satiesfied


        elif player_1.get() == "":
            empty_field = "Player 1 Name"
            Graphical.showwarning_dialog(self)

        elif player_2.get() == "":
            empty_field = " Player 2 Name "
            Graphical.showwarning_dialog(self)
        else:  # if names are fulfilled properly then this block is executed
            widg = self.widget

            if widg[
                "state"] == "normal":  # Checks state of the button so that it could be disabled and embeds the text on buttonsa after being disabled as well
                widg.config(state="disable", bg="#f2f2f2", fg="black")

                if mark == 0:
                    widg.config(text="X")
                    mark = 1

                else:
                    widg.config(text="O")
                    mark = 0

                buttons_list_text.append(widg["text"])
                buttons_info.append(widg)
                pressed_button_names.append(widg.winfo_name())
                click_counter += 1

            if click_counter >= 5:
                Controls.condition_check(self)

    def mouse_enter(self):  # CAlled by blind when mouse enters the button
        widg = self.widget
        if widg["state"] == "normal":  # On hover of the mouse the text is displayed
            if mark == 0:
                display_data = "X"
            else:
                display_data = "O"
            widg.config(bg="black", fg="white", text=display_data)

    def mouse_exit(self):  # CAlled by bindfunction when mouse leaves the button
        widg = self.widget
        if widg["state"] == "normal":
            widg.config(bg="white", fg="black", text="X/O")

    def name_exchange(self):  # Provides the alternative names for the button
        global custom_button_name
        global button_names
        name = 1
        for but_name in button_names:
            custom_button_name.append(name)
            name += 1
        print(custom_button_name)


class Graphical:  # Graphical or Fronthand view of the Game

    def __init__(self, main_window):  # Initialization of Graphical class
        """Graphical Section of the Game"""
        self.master = main_window
        self.__game_mode = "Graphical section"
        main_window.title("Tic-Tac-Toe")
        main_window.geometry("500x550+200+150")
        self.frame_1 = None
        self.times_new = tkFonts.Font(family="Times New Roman", size=15)

    def player_name(self):  # Gets the name of the player from the user
        global player_1, player_2
        self.Common_label = Frame(self.master)  # Declaration of master frame for the textboxes
        self.Common_label.pack()

        Label_box_1 = LabelFrame(self.Common_label,
                                 text="Player 1 (X)")  # Label box for the player 1 name field or textbox
        Label_box_1.pack(padx=10, pady=10, side=LEFT)
        player_1 = Entry(Label_box_1)  # player 1 textbox
        player_1.pack(ipadx=10, ipady=10)

        Label_box_2 = LabelFrame(self.Common_label, text="Player 2 (O) ")
        Label_box_2.pack(padx=10, pady=10, side=RIGHT)
        player_2 = Entry(Label_box_2)
        player_2.pack(ipadx=10, ipady=10)

    def frame_init(self):  # Initialization of the master frame for buttons arranged.
        self.main_frame = Frame(self.master, width=350, height=350, highlightbackground="black", highlightthickness=1,
                                bg="red")
        self.main_frame.pack(padx=20, pady=20)

    def sub_frame_init(self):  # It is desplays under main_frame and displays 3 buttons at time
        self.sub_frame = Frame(self.main_frame)
        self.sub_frame.pack(fill=Y, side=LEFT)
        for x in range(3):
            button = Button(self.sub_frame, text="X/O", width=7, height=5, bg="White", font=self.times_new,
                            relief="sunken", state="normal")
            button.pack()
            button_names.append(button.winfo_id())
            button.bind("<Enter>",
                        Controls.mouse_enter)  # Calls mouse_enter method  of class COntrols when Mouse enters in the Button
            button.bind("<1>",
                        Controls.disable_widget)  # Calls disable_widget method of class Controls when Mouse left clicks  in the Button
            button.bind("<Leave>",
                        Controls.mouse_exit)  # Calls mouse_exit method  of class COntrols when Mouse exits the Button

    def winnerdialog_box(self):  # Shows winners name in the dialog box
        text_var = f"{winner_data} wins The Game"
        tkmessagebox.showinfo(title="Winner", message=text_var)

    def drawdialogbox(self):  # Shows tie message if no one wins
        text_var = "No-one Won the game"
        tkmessagebox.showinfo(title="Tie", message=text_var)

    def showwarning_dialog(self):  # Shows errors if name field is left blank
        text_var = f"{empty_field} Hasn't been fulfilled yet. Please Fulfill to Continue.."
        tkmessagebox.showerror(title="Name Error", message=text_var)
        sys.exit()
        


# Calling methods and declaring the objects for the class
root = Tk()  # Dedicates the parent window for the program execution
Control = Controls(root)  # Object decleration of Controls class
GUI = Graphical(root)  # Object decleration for Graphics class
GUI.player_name()  # Gui method call
GUI.frame_init()  # Gui method call
GUI.sub_frame_init()  # Gui method call
GUI.sub_frame_init()  # Gui method call
GUI.sub_frame_init()  # Gui method call

root.mainloop()  # Infinite loop for the window
