import serial
import time

port = serial.serial_for_url('loop://', timeout=1, baudrate=9600)


def read_data():
    data = port.readline()
    return data.decode('utf-8').strip()


# Example usage
counter = 0
while counter < 50:
    received_data = read_data()
    print(f"Received data: {received_data}")
    time.sleep(1)
    counter += 1
