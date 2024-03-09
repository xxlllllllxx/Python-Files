import serial


class Arduino:
    def __init__(self, port, baudrate, interval=100):
        self.interval = interval
        self._serial = serial.Serial(port=port, baudrate=baudrate, interval=self.interval)

    def readline(self):
        self._serial.readline()
