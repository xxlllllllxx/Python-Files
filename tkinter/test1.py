import tkinter as tk


def __main__():
    root = tk.Tk()

    root.geometry("500x200")
    font = {'Arial', 16}
    root.title("PYTHON")
    label = tk.Label(root, text="Hello", font=font)
    label.pack(pady=20)

    textbox = tk.Text(root, height=1, font=font)
    textbox.pack(padx=30)

    buttonFrame = tk.Frame(root)
    create_calc_button(buttonFrame, 0, 0, "1")
    create_calc_button(buttonFrame, 1, 0, "2")
    create_calc_button(buttonFrame, 2, 0, "3")
    create_calc_button(buttonFrame, 0, 1, "4")
    create_calc_button(buttonFrame, 1, 1, "5")
    create_calc_button(buttonFrame, 2, 1, "6")
    create_calc_button(buttonFrame, 0, 2, "7")
    create_calc_button(buttonFrame, 1, 2, "8")
    create_calc_button(buttonFrame, 2, 2, "9")
    buttonFrame.pack(fill='x', padx=30)
    root.mainloop()


def create_calc_button(root, col, row, digit):
    root.columnconfigure(col, weight=1)
    button = tk.Button(root, text=digit, font={"Arial", 20})
    button.grid(row=row, column=col, sticky=tk.W+tk.E, padx=5)


__main__()
