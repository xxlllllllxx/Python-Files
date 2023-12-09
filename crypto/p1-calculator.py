import customtkinter as tk

tx_coin_1 = "USDT"
tx_coin_2 = "BTC"
tx_coin_3 = "BNB"

# root
root = tk.CTk()

# 3 coins value
coin_1 = tk.StringVar(value="0.00")
coin_2 = tk.StringVar(value="0.00")
coin_3 = tk.StringVar(value="0.00")

# amount
amount_1 = tk.StringVar(value="0.00")
amount_2 = tk.StringVar(value="0.00")
amount_3 = tk.StringVar(value="0.00")

# pairs
pair_1_2 = tk.StringVar(value="0.0")
pair_1_3 = tk.StringVar(value="0.0")

pair_2_1 = tk.StringVar(value="0.0")
pair_2_3 = tk.StringVar(value="0.0")

pair_3_1 = tk.StringVar(value="0.0")
pair_3_2 = tk.StringVar(value="0.0")

pair_labels = [tx_coin_1, tx_coin_2, tx_coin_3]
total_value_vars = [tk.StringVar(value="0.00") for _ in range(3)]
exchange_earnings_vars = [tk.StringVar(value="0.00") for _ in range(3)]
amount_labels = [tx_coin_1, tx_coin_2, tx_coin_3]
amount_vars = [tk.StringVar(value="0.00") for _ in range(3)]


def calculate():
    coin_1_val = float(coin_1.get())
    coin_2_val = float(coin_2.get())
    coin_3_val = float(coin_3.get())

    amount_1_val = float(amount_1.get())
    amount_2_val = float(amount_2.get())
    amount_3_val = float(amount_3.get())

    # Calculate the trading pairs
    pair_1_2_val = coin_1_val / coin_2_val
    pair_1_3_val = coin_1_val / coin_3_val
    pair_2_1_val = coin_2_val / coin_1_val
    pair_2_3_val = coin_2_val / coin_3_val
    pair_3_1_val = coin_3_val / coin_1_val
    pair_3_2_val = coin_3_val / coin_2_val

    # Update the pair values in the UI
    pair_1_2.set(f"{pair_1_2_val:.4f}")
    pair_1_3.set(f"{pair_1_3_val:.4f}")
    pair_2_1.set(f"{pair_2_1_val:.4f}")
    pair_2_3.set(f"{pair_2_3_val:.4f}")
    pair_3_1.set(f"{pair_3_1_val:.4f}")
    pair_3_2.set(f"{pair_3_2_val:.4f}")

    # Example calculation - you should replace this with your actual logic
    for i in range(3):
        total_value = coin_1_val * pair_1_2_val + coin_1_val * pair_1_3_val
        total_value_vars[i].set(f"{total_value:.2f}")

        exchange_earnings = amount_1_val * pair_1_2_val + amount_1_val * pair_1_3_val
        exchange_earnings_vars[i].set(f"{exchange_earnings:.2f}")

        # Update the amount calculation if needed
        amount = amount_1_val * pair_1_2_val + amount_1_val * pair_1_3_val
        amount_vars[i].set(f"{amount:.2f}")


tk.CTkLabel(root, text="NAME").grid(row=0, column=0, padx=10)
tk.CTkLabel(root, text="EXCHANGE").grid(row=0, column=1, padx=10)
tk.CTkLabel(root, text="AMOUNT").grid(row=0, column=2, padx=10)

# exchange earnings here
tk.CTkLabel(root, text=f"{tx_coin_1}").grid(row=0, column=3, padx=10)
tk.CTkLabel(root, text=f"{tx_coin_2}").grid(row=0, column=4, padx=10)
tk.CTkLabel(root, text=f"{tx_coin_3}").grid(row=0, column=5, padx=10)

tk.CTkLabel(root, text=tx_coin_1).grid(row=1, column=0, padx=10)
tk.CTkLabel(root, text=tx_coin_2).grid(row=2, column=0, padx=10)
tk.CTkLabel(root, text=tx_coin_3).grid(row=3, column=0, padx=10)

tk.CTkEntry(root, textvariable=coin_1).grid(row=1, column=1, padx=5)
tk.CTkEntry(root, textvariable=coin_2).grid(row=2, column=1, padx=5)
tk.CTkEntry(root, textvariable=coin_3).grid(row=3, column=1, padx=5)

tk.CTkEntry(root, textvariable=amount_1).grid(row=1, column=2, padx=5)
tk.CTkEntry(root, textvariable=amount_2).grid(row=2, column=2, padx=5)
tk.CTkEntry(root, textvariable=amount_3).grid(row=3, column=2, padx=5)

tk.CTkLabel(root, text=tx_coin_1).grid(row=1, column=3, padx=10)
tk.CTkLabel(root, textvariable=pair_1_2).grid(row=1, column=4, padx=10)
tk.CTkLabel(root, textvariable=pair_1_3).grid(row=1, column=5, padx=10)

tk.CTkLabel(root, textvariable=pair_1_2).grid(row=2, column=3, padx=10)
tk.CTkLabel(root, text=tx_coin_2).grid(row=2, column=4, padx=10)
tk.CTkLabel(root, textvariable=pair_2_3).grid(row=2, column=5, padx=10)

tk.CTkLabel(root, textvariable=pair_1_3).grid(row=3, column=3, padx=10)
tk.CTkLabel(root, textvariable=pair_2_3).grid(row=3, column=4, padx=10)
tk.CTkLabel(root, text=tx_coin_3).grid(row=3, column=5, padx=10)

tk.CTkLabel(root, text="Trade Summary", font=("Helvetica", 16)).grid(row=5, column=0, columnspan=6, pady=10)

tk.CTkLabel(root, text="Pair").grid(row=6, column=0, padx=10)
tk.CTkLabel(root, text="Total Value").grid(row=6, column=1, padx=10)
tk.CTkLabel(root, text="Exchange Earnings").grid(row=6, column=2, padx=10)


for i in range(3):
    tk.CTkLabel(root, text=pair_labels[i]).grid(row=i + 7, column=0, padx=10)
    tk.CTkLabel(root, textvariable=total_value_vars[i]).grid(row=i + 7, column=1, padx=10)
    tk.CTkLabel(root, textvariable=exchange_earnings_vars[i]).grid(row=i + 7, column=2, padx=10)


tk.CTkButton(root, text="CALCULATE", command=calculate).grid(row=4, column=0, columnspan=4)

root.mainloop()
