import matplotlib.pyplot as plt
from matplotlib.patches import Arc
from matplotlib.animation import FuncAnimation
import random
from collections import deque


class MockSerial:
    def __init__(self):
        self.counter = 0

    def readline(self):
        value = random.randint(0, 100)
        value = value / 100
        self.counter += 1
        return f"{value}\n".encode('utf-8')


ser = MockSerial()

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)

max_data_points = 100
x_data = list(range(max_data_points))
y_data_line = deque(maxlen=max_data_points)
y_data_bar = deque(maxlen=max_data_points)

bar_plot = ax2.bar(x_data, [0] * max_data_points)
line_plot, = ax1.plot(x_data, [0] * max_data_points, lw=1)
scatter_plot = ax3.scatter(x_data, [0]*max_data_points, s=1)

largest = 0

# Create an Arc for the gauge chart
gauge_arc: Arc = Arc((0.5, 0.5), 0.7, 0.7, theta1=180, theta2=180, color='skyblue', linewidth=4)

ax4.add_patch(gauge_arc)
text_element = ax4.text(0.5, 0.5, 'GAUGE', ha='center', va='center', fontsize=8)
ax4.axis('off')


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
            ax3.set_ylim(0, largest)
            # ax4.set_ylim(0, largest)
            ax1.relim()

        # BAR
        for i, bar in enumerate(bar_plot):
            if i < len(y_data_bar):
                bar.set_height(y_data_bar[i])

        # LINE
        line_plot.set_data(x_data[-len(y_data_line):], y_data_line)

        # SCATTER
        scatter_plot.set_offsets([(x, y) for x, y in zip(x_data[-len(y_data_line):], y_data_line)])

        # GAUGE
        gauge_arc.theta1 = (180 - (value / largest * 180))
        text_element.set_text(f'{value} / {largest}')

    except Exception as e:
        print(f"Error reading data: {e}")

    return line_plot, bar_plot, scatter_plot, gauge_arc


ani = FuncAnimation(fig, update, frames=range(100), interval=200)

plt.show()
