import tkinter as tk
from tkinter import messagebox, ttk
import mysql.connector as mc
from mysql.connector import errorcode


class User:
    def __init__(self, id, name: str = "", age: int = 0, grade: int = 0):
        self.id = id
        self.name = name
        self.age = age
        self.grade = grade
        self.data = [self.id, self.name, self.age, self.grade]


def __main__():
    user1 = User("NULL", name="masallo", age=21, grade=75)
    user_insert(user1)


def connection() -> mc.MySQLConnection:
    try:
        conn = mc.connect(host="localhost", database="db_py", user="root")
        print("Database Connected")
        return conn
    except mc.Error as err:  # Error Handling
        print("Database failed: ", err)


def user_insert(user: User):
    try:
        con = connection()
        cursor = con.cursor()
        query = "INSERT INTO tbl_user VALUES (%s, %s, %s, %s)"

        cursor.execute(query, user.data)

        con.commit()
        con.close()

        messagebox.showinfo("Insert", "Insert success")
    except mc.Error as err:
        messagebox.showerror("Error", err)
        print("Database failed: ", err)


# Startup
if __name__ == "__main__":
    __main__()
