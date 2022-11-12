from tkinter import *

import string
import random
from tkinter.constants import END

list_of_characters = []

uppercase = random.randint(0, 25)
list_of_characters.append(string.ascii_uppercase[uppercase])

lowercase = random.randint(0, 25)
list_of_characters.append(string.ascii_lowercase[lowercase])

numbers = random.randint(0, 9)
list_of_characters.append(string.digits[numbers])

special_character = random.randint(0, 35)
list_of_characters.append(string.punctuation[special_character])


class PasswordGenerator:
    def __init__(self):
        self.window = Tk()
        self.window.title("Password Generator")
        self.window.geometry("450x300")
        self.window.configure(background="#856ff8")

        # Label Frame
        self.label_frame = LabelFrame(
            self.window, text="Enter the number of characters")
        self.label_frame.pack(pady=20)

        # Entry box for number of characters
        self.length_entry_box = Entry(self.label_frame, width=20)
        self.length_entry_box.pack(padx=20, pady=20)

        # Declaring feedback if no length is found
        self.feedback = Label(self.window)

        # Entry box for password
        self.password_entry_box = Entry(
            self.window, text="", width=50)
        self.password_entry_box.pack(pady=20)

        # Frame for buttons
        self.button_frame = Frame(self.window)
        self.button_frame.pack(pady=20)

        # Generate Password Button
        generate_btn = Button(
            self.button_frame, text=" Generate Password", command=self.generate_random_password
        )
        generate_btn.grid(row=0, column=0, padx=10)

        # copy Password Button
        copy_btn = Button(self.button_frame, text=" Copy Password")
        copy_btn.grid(row=0, column=1, padx=10)

    def generate_random_password(self):
        self.password_entry_box.delete(0, END)
        try:
            password_lenght = int(self.length_entry_box.get())
            self.feedback.destroy()

            for i in range(password_lenght - 4):
                rest_characters = random.randint(0, 95)
                list_of_characters.append(string.printable[rest_characters])

            random.shuffle(list_of_characters)
            password = ''.join(list_of_characters)
            self.password_entry_box.insert(0, password)
        except ValueError:
            self.feedback = Label(self.window, fg="red",
                                  text="Please Enter number of Character")
            self.feedback.place(x=130, y=100)


if __name__ == '__main__':
    PasswordGenerator().window.mainloop()
