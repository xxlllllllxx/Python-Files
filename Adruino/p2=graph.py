import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random
import serial
import time
from collections import deque


class MockSerial:
    def __init__(self):
        self.counter = 0

    def readline(self):
        # Generate a random number between 1 and 100
        value = random.randint(0, 100)
        value = value / 100
        # Increment a counter for x-axis values
        self.counter += 1
        return f"{value}\n".encode('utf-8')


# ser = MockSerial()
ser = serial.Serial('/dev/ttyACM0', 57600)

fig, (ax1, ax2) = plt.subplots(2, 1)

max_data_points = 100
x_data = list(range(max_data_points))
y_data_line = deque(maxlen=max_data_points)
y_data_bar = deque(maxlen=max_data_points)

bar_container = ax2.bar(range(max_data_points), [0] * max_data_points)

line_plot, = ax1.plot(x_data, [0] * max_data_points, lw=2)

largest = 0


def update(frame):
    global largest
    try:
        data = ser.readline().decode('utf-8').strip()

        value = float(data)

        y_data_line.append(value)
        y_data_bar.append(value)

        if largest < value:
            largest = value
            ax1.set_ylim(0, largest)
            ax2.set_ylim(0, largest)
            ax1.relim()

        line_plot.set_data(x_data[-len(y_data_line):], y_data_line)

        for i, bar in enumerate(bar_container):
            if i < len(y_data_bar):
                bar.set_height(y_data_bar[i])

    except Exception as e:
        print(f"Error reading data: {e}")

    return line_plot, bar_container


ani = FuncAnimation(fig, update, frames=range(100), interval=200)

plt.show()
