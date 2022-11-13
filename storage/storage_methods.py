from tkinter import simpledialog
from databaseGenerator.generate_database import init_database


class StorageMethods:

    def __init__(self):
        self.db, self.cursor = init_database()

    def popup_entry(self, heading):
        answer = simpledialog.askstring("Enter details", heading)
        return answer

    def add_password(self, popup_screen):
        platform = self.popup_entry("Platform")
        userid = self.popup_entry("Username/Email")
        password = self.popup_entry("Password")

        insert_cmd = """INSERT INTO vault(platform, userid, password) VALUES (?, ?, ?)"""
        self.cursor.execute(insert_cmd, (platform, userid, password))
        self.db.commit()
        popup_screen()

    def update_password(self, id, popup_screen):
        password = self.popup_entry("Enter New Password")
        self.cursor.execute(
            "UPDATE vault SET password = ? WHERE id = ?", (password, id))
        self.db.commit()
        popup_screen()

    def remove_password(self, id, popup_screen):
        self.cursor.execute("DELETE FROM vault WHERE id = ?", (id,))
        self.db.commit()
        popup_screen()
