import tkinter as tk
from tkinter import messagebox


class GUI:
    def __init__(self):
        self.font = {"Arial", 12}
        self.root = tk.Tk()
        self.menu = tk.Menu(self.root)
        self.create_menu(self.menu)
        self.static_design(self.root)
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def create_menu(self, menu):
        self.filemenu = tk.Menu(menu, tearoff=0)
        self.filemenu.add_command(label="Run", command=self.btn_test_click)
        self.filemenu.add_command(label="Execute", command=self.run_clear)
        self.filemenu.add_command(label="Close", command=self.on_closing)
        self.editmenu = tk.Menu(menu, tearoff=0)
        self.editmenu.add_command(label="Undo")
        self.editmenu.add_command(label="Redo")
        self.viewmenu = tk.Menu(menu, tearoff=0)
        self.viewmenu.add_command(label="Run", command=self.btn_test_click)

        menu.add_cascade(menu=self.filemenu, label="File")
        menu.add_cascade(menu=self.editmenu, label="Edit")
        menu.add_cascade(menu=self.viewmenu, label="View")

        self.root.config(menu=menu)

    def static_design(self, root):
        root.title("Calculator")
        root.geometry("320x500")
        self.textbox = tk.Entry(root, font=self.font)
        self.textbox.bind("<KeyPress>", self.shortcut)
        self.textbox.pack(padx=10, pady=10)
        self.cb_ckecker_state = tk.IntVar()
        self.cb_checker = tk.Checkbutton(
            root, text="Try", font=self.font, variable=self.cb_ckecker_state)
        self.cb_checker.pack()
        self.btn_test = tk.Button(
            self.root, text="TEST CLICK", font=self.font, command=self.btn_test_click)
        self.btn_test.pack()

    def btn_test_click(self):
        # print(self.textbox.get('1.0', tk.END), self.cb_ckecker_state.get())
        if self.cb_ckecker_state.get() == 1:
            messagebox.showinfo(
                title="Checked", message=self.textbox.get())

    def run_clear(self):
        self.cb_ckecker_state.set(1)
        self.btn_test_click()
        self.textbox.delete()

    def shortcut(self, event):
        if event.keysym == "Return":
            self.run_clear

    def on_closing(self):
        if messagebox.askyesno("QUIT?", "Are you sure you want to exit?"):
            self.root.destroy()

    def start(self):
        self.root.mainloop()


gui = GUI()
gui.start()
