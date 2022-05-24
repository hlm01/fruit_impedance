from json import tool
import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import get_data
import algorithm
from time import sleep


class App(tk.Tk):
    # impedance constant thresholds
    MAX = 640000
    HIGH = 400000
    LOW = 280000
    MIN = 40000

    def __init__(self):
        super().__init__()

        # root window
        self.title('Fruit Ripeness:')
        self.geometry('700x700+1000+0')
        self.resizable(False, False)
        self.style = ttk.Style(self)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)

        # make a button to measure
        self.button = ttk.Button(self, text="Measure")
        self.button["command"] = self.button_clicked
        self.button.grid(row=3, columnspan=2, pady=20)

        self.setup_plot()

        self.canvas.draw()
        self.canvas.get_tk_widget().grid(column=1, padx=30, sticky="N")
        self.bar = ttk.Progressbar(self, orient='horizontal',
                                   mode='determinate', length=400)
        self.bar.grid(columnspan=2, row=0, sticky="n", pady=30)
        # current value label
        current_value_label = ttk.Label(
            self,
            text='Current Value:'
        )
        left_label = ttk.Label(self, text='ripeness')


        left_label.grid(row=0, sticky = "E")
        current_value_label.grid(
            row=1,
            columnspan=2,
            sticky='n',
            ipadx=10,
            ipady=10
        )

    # plot the data with matplotlib
    def setup_plot(self):
        # draw figure
        fig = Figure(figsize=(10, 7), dpi=50)
        self.canvas = FigureCanvasTkAgg(fig, master=self)
        self.plot1 = fig.add_subplot()

    def plot_data(self):
        self.plot1.cla()
        freq = list(self.measurement.keys())
        values = list(self.measurement.values())

        vmax, vmin = max(values), min(values)
        self.plot1.plot(freq, values)  # plot values
        self.plot1.set_xlabel("frequency hz")
        self.plot1.set_ylabel("impedance ohms")
        self.plot1.set_ylim(vmin*0.9, vmax*1.1)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(column=1, padx=30, sticky="N")

    # runs script to collect data
    def button_clicked(self):
        get_data.get_data()
        sleep(2)
        self.measurement = algorithm.make_dictionary()
        self.plot_data()
        raw = self.measurement[10000]
        if raw > self.HIGH:
            value = 20
        elif raw < self.LOW:
            value = 50
        else:
            value = 80
        self.bar['value'] = value
        
if __name__ == "__main__":
    app = App()
    app.mainloop()
