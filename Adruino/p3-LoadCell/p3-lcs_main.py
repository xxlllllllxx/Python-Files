# TODO: change tp [ src.lcs_serial_mock as serial ] for realtime data

from matplotlib.lines import Line2D
from matplotlib.patches import Arc
from matplotlib.animation import FuncAnimation
import random
import serial
from collections import deque
import customtkinter as ctk
from matplotlib.typing import ColorType
import src.lcs_graph as monitor
import src.lcs_calibration as calibrate
import src.lcs_serial_mock as serial
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib
import matplotlib.pyplot as plt


matplotlib.use("TkAgg")
ctk.set_appearance_mode("dark")
plt.style.use("dark_background")
title = "Arduino Project"


class App:
    def __init__(self, arduino: serial.Arduino):
        self._arduino = arduino

        self.root = ctk.CTk()

        # STATE
        self.calibrated: bool = False
        self._is_calibrating: bool = False
        self.run_monitor: bool = False
        self._is_running = False
        self.exit: bool = False
        self._is_exiting: bool = False

        # GRAPHS
        self.largest = 1
        self.lowest = 0
        self.max_x_data: int = 100
        self.x_data = list(range(self.max_x_data))
        self.y_data = deque(maxlen=self.max_x_data)

        self.cal_fig = Figure(figsize=(12, 5), dpi=50, constrained_layout=False)
        self.bar_grp = self.cal_fig.add_subplot(111)
        self.bar_grp.set_ylim(self.lowest - 1, self.largest)
        self.plt_bar = self.bar_grp.bar(self.x_data, [0] * self.max_x_data)

        self.mon_fig = Figure(figsize=(14, 5), dpi=50, constrained_layout=False)
        self.line_grp = self.mon_fig.add_subplot(111)
        self.plt_line = self.line_grp.plot(self.x_data, [0] * self.max_x_data, lw=2)

        self.gauge_fig = Figure(figsize=(4, 4), dpi=50)
        self.gauge_ax = self.gauge_fig.add_subplot(111)
        self.plt_gauge = Arc((0.5, 0.5), 1, 1, theta1=180, theta2=180, color='skyblue', linewidth=2, edgecolor='black')
        self.gauge_ax.add_patch(self.plt_gauge)
        self.gauge_ax.axis('off')
        self.tx_gaud = ctk.StringVar(value="GAUGE")

        # CALIBRATION
        self.selected_calibration: int = 1
        self.unit: str = "kg"
        self.tx_cal = ctk.StringVar(value="[ 0000.00 ] kg")

        # UI
        self.root.title(title)
        self.root.resizable(False, False)
        self.font_title = ('Arial', 16)
        self.font_text = ('Arial', 12)
        self.font_button = ('Arial', 14)
        self.pad = 8

    def _calibrationUI(self) -> bool:
        result = calibrate.UI().test(self.selected_calibration)
        if (result == True):
            return True
        return self._calibrationUI()

    def _monitorUI(self) -> bool:
        result = monitor.UI()

    def start(self):
        cal_fm = ctk.CTkFrame(self.root)
        cal_fm.grid(padx=self.pad, pady=self.pad, sticky="new")
        ctk.CTkLabel(cal_fm, text="CALIBRATION", font=self.font_title).grid(padx=self.pad, pady=self.pad, sticky="nw")
        cal_fm_graph = ctk.CTkFrame(cal_fm, width=500)
        cal_fm_graph.grid(padx=self.pad, pady=self.pad, sticky="nsew", row=1, column=0, columnspan=3, rowspan=2)
        cal_fm_sel_unit = ctk.CTkFrame(cal_fm)
        cal_fm_sel_unit.grid(padx=self.pad, pady=self.pad, sticky="nsew", row=1, column=3, rowspan=2)
        ctk.CTkLabel(cal_fm, text=self.tx_cal.get(), font=self.font_text).grid(padx=self.pad, pady=self.pad, sticky="sew", row=1, column=4)
        ctk.CTkButton(cal_fm, text="CALIBRATE", font=self.font_button, command=self._calibrationUI).grid(
            padx=self.pad, pady=self.pad, sticky="sew", row=2, column=4)

        self.cal_cvs = FigureCanvasTkAgg(self.cal_fig, cal_fm_graph)
        self.cal_cvs.get_tk_widget().grid(sticky=ctk.NSEW)
        self.cal_cvs._tkcanvas.grid(padx=self.pad, pady=self.pad, sticky=ctk.NSEW)
        self.anim = FuncAnimation(self.cal_fig, lambda frame: self.updateCal(frame), frames=range(100), interval=self._arduino.interval)

        mon_fm = ctk.CTkFrame(self.root)
        mon_fm.grid(padx=self.pad, pady=self.pad, sticky="new")
        ctk.CTkLabel(mon_fm, text="MONITOR", font=self.font_title).grid(padx=self.pad, pady=self.pad, sticky="nw")

        mon_fm_graph = ctk.CTkFrame(mon_fm, width=700)
        mon_fm_graph.grid(padx=self.pad, pady=self.pad, sticky="nsew", column=0, row=1)

        self.mon_cvs = FigureCanvasTkAgg(self.mon_fig, mon_fm_graph)
        self.mon_cvs.get_tk_widget().grid(sticky=ctk.NSEW)
        self.mon_cvs._tkcanvas.grid(padx=self.pad, pady=self.pad, sticky=ctk.NSEW)

        self.anim2 = FuncAnimation(self.mon_fig, lambda frame: self.updateMon(frame), frames=range(100), interval=self._arduino.interval)

        mon_fm_gaud = ctk.CTkFrame(mon_fm)
        mon_fm_gaud.grid(padx=self.pad, pady=self.pad, sticky="nsew", column=1, row=1)
        self.gauge_cvs = FigureCanvasTkAgg(self.gauge_fig, mon_fm_gaud)
        self.gauge_cvs.get_tk_widget().grid(sticky=ctk.NSEW)
        self.gauge_cvs._tkcanvas.grid(padx=self.pad, pady=self.pad, sticky=ctk.NSEW)

        ctk.CTkLabel(mon_fm_gaud, textvariable=self.tx_gaud, font=self.font_button).grid(sticky="NEW")

        self.anim3 = FuncAnimation(self.gauge_fig, lambda frame: self.updateGauge(frame), frames=range(100), interval=self._arduino.interval)

        plt.show()

        self.root.mainloop()

    def updateCal(self, frame):
        data = float(self._arduino.readline().decode('utf-8').strip())
        self.y_data.append(data)

        self.check(data)

        for rect, h in zip(self.plt_bar, self.y_data):
            rect.set_height(h)

        return self.plt_bar

    def updateMon(self, frame):
        self.x_data = list(range(len(self.y_data)))

        self.plt_line[0].set_data(self.x_data[-self.max_x_data - 1:], list(self.y_data)[-self.max_x_data:])

        return self.plt_line

    def updateGauge(self, frame):
        data = float(self._arduino.readline().decode('utf-8').strip())
        self.plt_gauge.theta1 = (180 - (data / self.largest * 180))
        self.tx_gaud.set(value=f'{data} / {self.largest}')
        return self.plt_gauge

    def check(self, data):
        if self.largest < data:
            self.largest = data
            self.bar_grp.set_ylim(self.lowest, self.largest + 1)
            self.line_grp.set_ylim(self.lowest, self.largest + 1)
            self.line_grp.relim()
        if self.lowest > data:
            self.lowest = data
            self.bar_grp.set_ylim(self.lowest - 1, self.largest)
            self.line_grp.set_ylim(self.lowest - 1, self.largest)
            self.line_grp.relim()


if __name__ == "__main__":
    # NOTE: Configure this port and baudrate
    arduino = serial.Arduino('/dev/ttyACM0', 57600, interval=500)
    app = App(arduino)

    app.start()
