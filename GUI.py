from tkinter import StringVar, IntVar
from customtkinter import CTk, CTkLabel, CTkEntry, CTkRadioButton, CTkButton
import re
from tkinter import messagebox


class BombPartyGUI(CTk):

    def __init__(self, *args, **kwargs):
        CTk.__init__(self, *args, **kwargs)
        self.geometry("290x500")
        self.bot_name = StringVar()
        self.room_link = StringVar()
        self.language = StringVar()
        self.difficulty = IntVar()

        self.diff_var = IntVar()
        self.diff_var.set(1)
        self.language_var = StringVar()
        self.language_var.set("en")

        # Title Label
        self.title_label = CTkLabel(text="Bomb Party Bot", text_font=("Roboto Medium", 16))
        self.title_label.grid(row=1, column=0, columnspan=4, pady=10, padx=0)

        # Bot Name
        self.bot_name_label = CTkLabel(self, text="Bot's name: ", text_font=("Roboto Medium", -16))
        self.bot_name_label.grid(row=2, column=0, columnspan=2, pady=0, padx=0)
        self.bot_name_entry = CTkEntry(self, width=140, placeholder_text="BombParty_bot")
        self.bot_name_entry.grid(row=2, column=2, columnspan=2, pady=10, padx=(0, 0))

        # Room link
        self.room_link_label = CTkLabel(text="Room's link: ", text_font=("Roboto Medium", -16))
        self.room_link_label.grid(row=3, column=0, columnspan=2, pady=0, padx=0)
        self.room_link_entry = CTkEntry(width=140, placeholder_text="https://jklm.fun/XXXX")
        self.room_link_entry.grid(row=3, column=2, columnspan=2, pady=10, padx=(0, 0))

        # Chose difficulty
        self.chose_diff_label = CTkLabel(text="Chose difficulty: ", text_font=("Roboto Medium", 14))
        self.chose_diff_label.grid(row=4, column=0, columnspan=4, pady=10, padx=0)

        # Easy
        self.diff_easy_label = CTkLabel(self, text="Easy", text_font=("Roboto Medium", 12), width=10)
        self.diff_easy_label.grid(row=5, column=0, pady=(10, 0), padx=0)
        self.diff_easy_button = CTkRadioButton(variable=self.diff_var, value=0, text="")
        self.diff_easy_button.grid(row=6, column=0, pady=10, padx=(10, 0))

        # Normal
        self.diff_normal_label = CTkLabel(self, text="Normal", text_font=("Roboto Medium", 12), width=10)
        self.diff_normal_label.grid(row=5, column=1, pady=(10, 0), padx=0)
        self.diff_normal_button = CTkRadioButton(variable=self.diff_var, value=1, text="")
        self.diff_normal_button.grid(row=6, column=1, pady=10, padx=(10, 0))
        # Hard
        self.diff_hard_label = CTkLabel(text="Hard", text_font=("Roboto Medium", 12), width=10)
        self.diff_hard_label.grid(row=5, column=2, pady=(10, 0), padx=0)
        self.diff_hard_button = CTkRadioButton(variable=self.diff_var, value=2, text="")
        self.diff_hard_button.grid(row=6, column=2, pady=10, padx=(10, 0))

        # Impossible
        self.diff_impossible_label = CTkLabel(text="Impossible", text_font=("Roboto Medium", 12), width=10)
        self.diff_impossible_label.grid(row=5, column=3, pady=(10, 0), padx=0)
        self.diff_impossible_button = CTkRadioButton(variable=self.diff_var, value=3, text="")
        self.diff_impossible_button.grid(row=6, column=3, pady=10, padx=(10, 0))

        # Chose language
        self.chose_diff_label = CTkLabel(text="Chose Language: ", text_font=("Roboto Medium", 14))
        self.chose_diff_label.grid(row=7, column=0, columnspan=4, pady=10, padx=0)

        # English
        self.english_label = CTkLabel(self, text="English", text_font=("Roboto Medium", 12), width=10)
        self.english_label.grid(row=8, column=0, columnspan=2, pady=(10, 0), padx=0)
        self.english_button = CTkRadioButton(variable=self.language_var, value="en", text="")
        self.english_button.grid(row=9, column=0, columnspan=2, pady=10, padx=(10, 0))

        # French
        self.french_label = CTkLabel(self, text="French", text_font=("Roboto Medium", 12), width=10)
        self.french_label.grid(row=8, column=2, columnspan=2, pady=(10, 0), padx=0)
        self.french_button = CTkRadioButton(variable=self.language_var, value="fr", text="")
        self.french_button.grid(row=9, column=2, columnspan=2, pady=10, padx=(10, 0))

        # Start Button
        self.start_button = CTkButton(text="Start", command=self.start)
        self.start_button.grid(row=10, column=0, columnspan=4, pady=10, padx=10)
        self.grid()
        self.mainloop()

    def start(self):

        self.room_link = CTkEntry.get(self.room_link_entry)
        self.bot_name = CTkEntry.get(self.bot_name_entry)
        if len(self.bot_name) < 1:
            self.bot_name = "BombParty_bot"
        self.difficulty = self.diff_var.get()
        self.language = self.language_var.get()
        link_pattern = re.compile("https://jklm.fun/[A-Z]{4}$")

        if link_pattern.match(self.room_link):
            self.destroy()
        else:
            messagebox.showerror(title='Error', message=f"Please enter a valid Room Link")

# test = BombPartyGUI()
# test.mainloop()
# print(link_room, bot_name, difficulty, language)
