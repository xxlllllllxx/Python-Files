import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random
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


# Initialize the mock serial port
ser = MockSerial()

# Initialize the figure and axes
fig, (ax1, ax2) = plt.subplots(2, 1)

# Initialize rolling arrays for data
max_data_points = 100
x_data = list(range(max_data_points))  # Use a list for x_data
y_data_line = deque(maxlen=max_data_points)
y_data_bar = deque(maxlen=max_data_points)

# Initialize bar plot with zeros
bar_container = ax2.bar(range(max_data_points), [0] * max_data_points)

# Initialize plots
line_plot, = ax1.plot(x_data, [0] * max_data_points, lw=2)

largest = 0

# Function to update the plots


def update(frame):
    global largest
    try:
        # Read data from the mock serial port
        data = ser.readline().decode('utf-8').strip()

        # Process the data (assuming it's a floating-point value)
        value = float(data)

        # Update the rolling arrays
        y_data_line.append(value)
        y_data_bar.append(value)

        if largest < value:
            largest = value
            ax1.set_ylim(0, largest)
            ax2.set_ylim(0, largest)
            ax1.relim()  # Recalculate data limits
            # ax1.autoscale_view()  # Autoscale the view

        # Update the line plot
        line_plot.set_data(x_data[-len(y_data_line):], y_data_line)

        # Update the bar plot
        for i, bar in enumerate(bar_container):
            if i < len(y_data_bar):  # Check deque length
                bar.set_height(y_data_bar[i])

    except Exception as e:
        print(f"Error reading data: {e}")

    return line_plot, bar_container


# Set the animation interval in milliseconds
ani = FuncAnimation(fig, update, frames=range(100), interval=200)

# Show the plot
plt.show()
