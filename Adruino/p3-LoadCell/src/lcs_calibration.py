import customtkinter as ctk

class UI:

    def __init__(self):
        pass

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
    def __init__(self, arduino, neg_cal:float, adj_cal: float):
        self._arduino = arduino
        self.root = ctk.CTk()
        
        self.txin_neg_cal = ctk.DoubleVar(value=neg_cal)
        self.txin_adj_cal = ctk.DoubleVar(value=adj_cal)
    
    def start(self):
        

        self.root.mainloop()