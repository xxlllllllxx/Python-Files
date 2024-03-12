import threading
import time
import customtkinter as ctk


class UI:
    def __init__(self, title, arduino, callback_function):
        self.root = ctk.CTk()
        self.root.title(title)
        self.root.geometry("300x150")
        self.callback_function = callback_function
        self.arduino = arduino

        self.message = ctk.StringVar(value="Please wait ....")

        self.message_label = ctk.CTkLabel(self.root, textvariable=self.message, font=('Arial', 14))
        self.message_label.pack(pady=20)

        self.cancel_button = ctk.CTkButton(self.root, text="Cancel", command=self.cancel_callback)
        self.cancel_button.pack(side="left", padx=10)

        self.ok_button = ctk.CTkButton(self.root, text="START", command=self.start)
        self.ok_button.pack(side="right", padx=10)

        self.is_stable = False
        self.is_cancelled = False
        self.list_of_res = []

    def close_window(self):

        self.is_cancelled = True
        self.is_stable = True
        self.root.destroy()

    def start(self):
        threading.Thread(target=self.read_data, args=(self.arduino,)).start()

    def cancel_callback(self):
        self.is_cancelled = True
        self.is_stable = True
        try:
            if self.root.winfo_exists():
                self.root.after(0, self.callback_function, 0)
                self.root.after(0, self.close_window)
        except Exception as e:
            print(f"Error in cancel_callback: {e}")

    def read_data(self, arduino):
        while not self.is_stable:
            value = arduino.readline()
            self.list_of_res.append(value)
            self.message.set(f"[ {value} ] kg")  # Use set method instead of value
            time.sleep(1)

            if len(self.list_of_res) >= 5:
                self.is_stable = all(x == self.list_of_res[-1] for x in self.list_of_res[-5:])

        if self.is_cancelled:
            return 0

        result = self.list_of_res[-1]
        self.callback_function(result)
        self.close_window()

    def test(self, cal: str) -> bool:
        print(cal)
        return True

# CALIBRATIONS value
# negative calibration -> value = value - neg_cal      tare()
# float adjustment -> value = value / adj_cal

# ADD weight
# 1kg value -> v1 = value (with 1kg)
# 2kg value -> v2 = value (with 2kg)
# calibration -> linear = (v2 == v1*2)  ----> end
# calibration -> with_eq =  (v2 == v1 + newval)
# 3kg value -> v3 = value (with 3kg)
# calibration -> with_eq = (v1 = val) (v2 == v1 + val/2) (v3 == v2 + val/3)


class UIUX:
    def __init__(self, arduino, neg_cal: float, adj_cal: float):
        self._arduino = arduino
        self.root = ctk.CTk()

        self.txin_neg_cal = ctk.DoubleVar(value=neg_cal)
        self.txin_adj_cal = ctk.DoubleVar(value=adj_cal)

    def start(self):

        self.root.mainloop()
