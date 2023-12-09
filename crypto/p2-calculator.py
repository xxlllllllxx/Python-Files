import tkinter as tk


class CryptoConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Crypto Converter")

        # Crypto exchange rates
        self.bnb_to_usdt = 230
        self.btc_to_usdt = 43530
        self.bnb_to_btc = 0.005298

        # Widgets
        self.amount_label = tk.Label(root, text="Enter Amount (USDT):")
        self.amount_entry = tk.Entry(root)
        self.convert_button = tk.Button(root, text="Convert", command=self.convert)
        self.result_label = tk.Label(root, text="Result:")

        # Layout
        self.amount_label.grid(row=0, column=0, padx=10, pady=10)
        self.amount_entry.grid(row=0, column=1, padx=10, pady=10)
        self.convert_button.grid(row=1, column=0, columnspan=2, pady=10)
        self.result_label.grid(row=2, column=0, columnspan=2, pady=10)

    def convert(self):
        try:
            usdt_amount = float(self.amount_entry.get())
            bnb_value = usdt_amount / self.bnb_to_usdt
            btc_value = usdt_amount / self.btc_to_usdt
            bnb_to_btc_value = bnb_value * self.bnb_to_btc
            btc_to_bnb_value = btc_value / self.bnb_to_btc
            btc_to_usd_value = btc_value * self.btc_to_usdt

            result_text = (
                f"BNB Value: {bnb_value:.4f}\n"
                f"BTC Value: {btc_value:.8f}\n"
                f"BNB to BTC Value: {bnb_to_btc_value:.8f}\n"
                f"BTC to BNB Value: {btc_to_bnb_value:.4f}\n"
                f"BTC to USD Value: {btc_to_usd_value:.2f}"
            )
            self.result_label.config(text=result_text)

        except ValueError:
            self.result_label.config(text="Please enter a valid number.")


if __name__ == "__main__":
    root = tk.Tk()
    app = CryptoConverterApp(root)
    root.mainloop()
