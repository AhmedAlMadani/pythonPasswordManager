from tkinter import simpledialog
from databaseGenerator.generate_database import init_database


def popup_entry(heading):
    answer = simpledialog.askstring("Enter details", heading)
    return answer


class StorageMethods:

    def __init__(self):
        self.db, self.cursor = init_database()

    def add_password(self, add_password):
        userid = popup_entry("Username/Email")
        password = popup_entry("Password")

        insert_cmd = """INSERT INTO storage(userid, password) VALUES (?, ?)"""
        self.cursor.execute(insert_cmd, (userid, password))
        self.db.commit()
        add_password()

    def update_password(self, id, update_password):
        password = popup_entry("Enter New Password")
        self.cursor.execute(
            "UPDATE storage SET password = ? WHERE id = ?", (password, id))
        self.db.commit()
        update_password()

    def remove_password(self, id, remove_password):
        self.cursor.execute("DELETE FROM storage WHERE id = ?", (id,))
        self.db.commit()
        remove_password()
