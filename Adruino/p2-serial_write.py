import serial
import time

port = serial.serial_for_url('COM3', timeout=1, baudrate=9600)


def write_data(data):
    port.write(data.encode('utf-8'))


counter = 0
while counter < 50:
    data = f"{counter-1},{counter},{counter+1}"
    write_data(data)
    print(f"Data: {data}")
    time.sleep(1)
    counter += 1
