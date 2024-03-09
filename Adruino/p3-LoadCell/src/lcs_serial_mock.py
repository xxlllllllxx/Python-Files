import random


class Arduino:
    def __init__(self, port, baudrate, interval=100):
        self.counter = 0
        self.interval = interval

    def readline(self):
        value = random.randint(0, 20)
        self.counter += 1
        return f"{value}\n".encode('utf-8')
