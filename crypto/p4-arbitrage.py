import customtkinter as ctk
from p3_arbitrage import calculate_profit, get_binance_coins

root = ctk.CTk()

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

stable_coins, alt_coins = get_binance_coins()


def calculate(status: ctk.CTkLabel, coin1: ctk.StringVar, val1: ctk.StringVar, coin2: ctk.StringVar, val2: ctk.StringVar, coin3: ctk.StringVar, val3: ctk.StringVar, earn: ctk.StringVar):
    status.configure(require_redraw=True, text="FETCHING DATA...", text_color="red")
    root.update_idletasks()

    coin1.set(coin1.get().upper())
    coin2.set(coin2.get().upper())
    coin3.set(coin3.get().upper())

    result = calculate_profit(float(val1.get()), coin1.get(), coin2.get(), coin3.get())
    val2.set(f"{result[0]:.20}")
    val3.set(f"{result[1]:.20}")
    earn.set(f"{result[2] - float(val1.get()):.20f}")

    status.configure(require_redraw=True, text="OK", text_color="lightgreen")
    root.update_idletasks()


if __name__ == "__main__":
    root.columnconfigure(0, weight=1)

    tx_coin_1 = ctk.StringVar(value=str(stable_coins[0]))
    tx_coin_2 = ctk.StringVar(value=str(stable_coins[1]))
    tx_coin_3 = ctk.StringVar(value=str(stable_coins[0]))

    tx_coin_1_value = ctk.StringVar()
    tx_coin_2_value = ctk.StringVar()
    tx_coin_3_value = ctk.StringVar()
    tx_earnings = ctk.StringVar()

    ctk.CTkLabel(root, font=("Arial", 20), text="Crypto Arbitrage Calculator", text_color="orange").grid(row=0, column=0, sticky="NEW")

    frame = ctk.CTkFrame(root, height=400, fg_color="gray")
    frame.grid(row=1, column=0, padx=10, pady=10, sticky=ctk.NW)

    combo_box_1 = ctk.CTkComboBox(frame, values=stable_coins, variable=tx_coin_1, width=180)
    combo_box_1.grid(row=0, column=0, padx=10, pady=10, sticky=ctk.NW)

    combo_box_1 = ctk.CTkComboBox(frame, values=stable_coins, variable=tx_coin_2, width=180)
    combo_box_1.grid(row=0, column=1, padx=10, pady=10, sticky=ctk.NW)

    combo_box_1 = ctk.CTkComboBox(frame, values=alt_coins, variable=tx_coin_3, width=180)
    combo_box_1.grid(row=0, column=2, padx=10, pady=10, sticky=ctk.NW)

    entry_1 = ctk.CTkEntry(frame, textvariable=tx_coin_1_value, width=180)
    entry_1.grid(row=1, column=0, padx=10, pady=10, sticky=ctk.NW)

    entry_2 = ctk.CTkEntry(frame, textvariable=tx_coin_2_value, state="readonly", width=180)
    entry_2.grid(row=1, column=1, padx=10, pady=10, sticky=ctk.NW)

    entry_3 = ctk.CTkEntry(frame, textvariable=tx_coin_3_value, state="readonly", width=180)
    entry_3.grid(row=1, column=2, padx=10, pady=10, sticky=ctk.NW)

    entry_4 = ctk.CTkEntry(frame, textvariable=tx_earnings, state="readonly", width=180)
    entry_4.grid(row=1, column=3, padx=10, pady=10, sticky=ctk.NW)

    status = ctk.CTkLabel(frame, text="OK", text_color="lightgreen", font=("Arial", 16, "bold"))
    status.grid(row=0, column=3, padx=10, pady=10, sticky=ctk.NW)

    ctk.CTkButton(frame, text="CALCULATE", command=lambda: calculate(status, tx_coin_1,
                                                                     tx_coin_1_value, tx_coin_2, tx_coin_2_value,
                                                                     tx_coin_3, tx_coin_3_value, tx_earnings)
                  ).grid(row=2, column=0, columnspan=4, padx=10, pady=10,)

    root.mainloop()
