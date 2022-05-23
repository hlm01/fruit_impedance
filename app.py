from json import tool
import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import get_data
import algorithm
from time import sleep


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # root window
        self.title('Fruit Ripeness:')
        self.geometry('700x700')
        self.resizable(False,False)
        self.style = ttk.Style(self)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)

        # make a button to measure
        self.button = ttk.Button(self, text = "Measure")
        self.button["command"] = self.button_clicked
        self.button.grid(row = 3, columnspan = 2,pady=20)
        #slider current value
        #current_value = tk.DoubleVar()
        current_value = 5
        
        self.setup_plot()
        def get_current_value():
            #return '{: .2f}'.format(current_value.get())
            return current_value
        
        def slider_changed(event):
            value_label.configure(text=get_current_value())
        
        #label for slider
        slider_label = ttk.Label(
            self,
            text = 'Ripeness:'
        )

        slider_label.grid(
            column=0,
            row=0,
            sticky='w'
        )

        #slider
        slider = ttk.Scale(
            self,
            from_=0,
            to=100,
            orient='horizontal',
            #command=slider_changed,
            variable=current_value
        )

        slider.grid(
            column=1,
            row=0,
            sticky='we',
            pady = 25,
            padx = 10
        )

        # current value label
        current_value_label = ttk.Label(
            self,
            text = 'Current Value:'
        )

        current_value_label.grid(
            row = 1,
            columnspan=2,
            sticky='n',
            ipadx=10,
            ipady=10
        )

        #value label
        value_label = ttk.Label(
            self,
            text=get_current_value()
        )
        value_label.grid(
            row=2,
            columnspan=2,
            sticky='n'
        )

    # plot the data with matplotlib
    def setup_plot(self):
        # draw figure
        fig = Figure(figsize = (10,7), dpi=50)
        self.canvas = FigureCanvasTkAgg(fig, master = self)
        self.plot1 = fig.add_subplot()

       
    def plot_data(self):
        self.plot1.cla()
        freq = list(self.measurement.keys())
        values = list(self.measurement.values())

        vmax, vmin = max(values), min(values)
        self.plot1.plot(freq,values) # plot values
        self.plot1.set_xlabel("frequency hz")
        self.plot1.set_ylabel("impedance ohms")
        self.plot1.set_ylim(vmin*0.9,vmax*1.1)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(column = 1,padx = 30, sticky="N")
    # runs script to collect data
    def button_clicked(self):
        get_data.get_data()
        sleep(2)
        self.measurement = algorithm.make_dictionary()
        self.plot_data()


if __name__ == "__main__":
    app = App()
    app.mainloop()