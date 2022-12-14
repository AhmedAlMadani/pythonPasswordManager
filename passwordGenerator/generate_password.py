from tkinter import *
import string
from secrets import choice


uppercase = list(string.ascii_uppercase)
lowercase = list(string.ascii_lowercase)
number = list(string.digits)
special_character = list(string.punctuation)


class PasswordGenerator:

    def __init__(self):
        self.window = Tk()
        self.window.title("Password Generator")
        self.window.geometry("450x300")

        # Label Frame
        self.label_frame = LabelFrame(
            self.window, text="Enter the number of characters")
        self.label_frame.pack(pady=20)

        # Entry box
        self.length_entry_box = Entry(self.label_frame, width=20)
        self.length_entry_box.pack(padx=20, pady=20)

        # message
        self.feedback = Label(self.window)

        # Entry box
        self.password_entry_box = Entry(
            self.window, width=50)
        self.password_entry_box.pack(pady=20)

        # Frame for buttons
        self.button_frame = Frame(self.window)
        self.button_frame.pack(pady=20)

        # Generate Password Button
        generate_btn = Button(
            self.button_frame, text="Generate Password", command=self.generate_password)
        generate_btn.grid(row=0, column=0, padx=10)

        # Copy Password Button
        copy_btn = Button(self.button_frame,
                          text="Copy Password", command=self.copy_password)
        copy_btn.grid(row=0, column=1, padx=10)

    def generate_password(self):
        self.password_entry_box.delete(0, END)
        try:
            password_length = int(self.length_entry_box.get())
            self.feedback.destroy()  # Destroy feedback if length is there
            data = uppercase + lowercase + number + special_character
            password = ''.join(choice(data) for _ in range(password_length))
            self.password_entry_box.insert(0, password)
        except ValueError:
            self.feedback = Label(self.window, fg="red",
                                  text="Please enter number of characters")
            self.feedback.place(x=130, y=100)

    def copy_password(self):
        self.window.clipboard_clear()
        self.window.clipboard_append(self.password_entry_box.get())


if __name__ == "__main__":
    PasswordGenerator().window.mainloop()
