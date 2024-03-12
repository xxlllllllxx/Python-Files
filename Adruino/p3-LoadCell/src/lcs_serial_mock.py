import random


class Arduino:
    def __init__(self, port, baudrate, interval=100):
        self.interval = interval
        self.no_weight = 1.0
        self.selected_unit = 1
        self.weighted = {1: 1, 10: 10, 15: 15, 20: 20}

    def readline(self):
        value = random.randint(0, 20)
        raw_value = f"{value}\n".encode('utf-8').decode('utf-8').strip()
        calibrated_value = self.calibrate(raw_value)
        return calibrated_value

    def calibrate(self, raw_value: str) -> float:
        raw_float = float(raw_value)

        # Use the selected_unit to determine the calibration value
        if self.selected_unit in self.weighted:
            calibration_value = self.weighted[self.selected_unit]
        else:
            calibration_value = self.no_weight

        calibrated_value = raw_float / calibration_value

        return raw_float
