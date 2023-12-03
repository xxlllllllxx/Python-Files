import customtkinter as ctk
from PIL import Image, ImageTk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


root = ctk.CTk()

ctk_font_large = ctk.CTkFont("Arial Black", 20, "bold")
ctk_text_color = "#10f0f0"

f1 = ctk.CTkFrame(root)
f1.grid(padx=10, pady=10)

tx_username = ctk.StringVar()
tx_password = ctk.StringVar()

img_show_password = ImageTk.PhotoImage(Image.open("images/dark_hidden.png"))
img_hide_password = ImageTk.PhotoImage(Image.open("images/dark_visible.png"))

ctk.CTkLabel(f1, text="LOGIN", font=ctk_font_large, text_color=ctk_text_color).grid(pady=5)


ctk.CTkLabel(f1, text="Username: ").grid(padx=20, sticky=ctk.W)
ctk.CTkEntry(f1, textvariable=tx_username, width=200, text_color=ctk_text_color).grid(padx=20)

ctk.CTkLabel(f1, text="Password: ").grid(padx=20, sticky=ctk.W)


ent_password = ctk.CTkEntry(f1, textvariable=tx_password, width=158, show="*", text_color=ctk_text_color)
ent_password.grid(row=4, padx=20, sticky=ctk.W)

btn_sh = ctk.CTkButton(f1, fg_color="transparent", hover=False,
                       image=img_show_password, text="", width=12, height=12, command=lambda: toggle_password())
btn_sh.grid(row=4, padx=20, sticky=ctk.E)

ctk.CTkButton(f1, text="Log In", command=lambda: login(tx_username.get(), tx_password.get())).grid(pady=20)


def login(username: str, password: str):
    print(f"Username: {username}\nPassword: {password}")


def toggle_password():
    if ent_password.cget("show") == "":
        ent_password.configure(show="*")
        btn_sh.configure(image=img_show_password)
    else:
        ent_password.configure(show="")
        btn_sh.configure(image=img_hide_password)


root.mainloop()
