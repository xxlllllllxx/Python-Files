import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Data Entry")


def __main__():
    fr_main = tk.Frame(root)
    fr_main.grid(column=0, row=0, padx=20)

    ui = frt_create(fr_main, "User Information", 0, 0)
    mid = frt_create(fr_main, "", 1, 0)
    dps = frt_create(fr_main, "Data Privacy Statement", 2, 0)

    consolidate(3, lblxent_create(ui, "firstname: "), lblxent_create(
        ui, "Middlename: "), lblxent_create(ui, "Lastname: "),)
    consolidate(3, lblxent_create(mid, "firstname: "))

    consolidate(3, lblxent_create(dps, "firstname: "), lblxent_create(
        dps, "Middlename: "), lblxent_create(dps, "Lastname: "))


def frt_create(main: tk.Frame, title: str, row: int, col: int) -> tk.LabelFrame:
    frt_container = tk.LabelFrame(main, text=title)
    frt_container.grid(column=col, row=row, pady=10)
    return frt_container


def lblxent_create(main: tk.Frame, label: str) -> tk.Frame:
    frt_container = tk.Frame(main)
    lbl_text = tk.Label(frt_container, text=label)
    lbl_text.grid(column=0, row=0, sticky=tk.W)
    ent_box = tk.Entry(frt_container)
    ent_box.grid(column=0, row=1, sticky=tk.W)
    return frt_container


def lblxcbx_create(main: tk.Frame, label: str) -> tk.Frame:
    frt_container = tk.Frame(main)
    lbl_text = tk.Label(frt_container, text=label)
    lbl_text.grid(column=0, row=0, sticky=tk.W)
    cbx_box = ttk.Combobox(frt_container)
    cbx_box.grid(column=0, row=1, sticky=tk.W)
    return frt_container


def consolidate(maxCol: int, *args: tk.Frame):
    col: int = 0
    row: int = 0

    for frm in args:
        frm.grid(column=col, row=row, padx=[5, 50], pady=5)
        col += 1
        if (col >= maxCol):
            col = 0
            row += 1


__main__()
root.mainloop()
