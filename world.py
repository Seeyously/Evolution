#%%
import tkinter as tk

class ExampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        t = SimpleTable(self, 10,10)
        t.pack(side="top", fill="x")
        t.set(1,1,5)
        #t.lift()

class SimpleTable(tk.Frame):
    def __init__(self, parent, rows=10, columns=2):
        tk.Frame.__init__(self, parent, background="black")
        self._widgets = []
        for row in range(rows):
            current_row = []
            for column in range(columns):
                label = tk.Label(self, borderwidth = 0, width = 2, height = 1)
                label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                current_row.append(label)
            self._widgets.append(current_row)

        for column in range(columns):
            self.grid_columnconfigure(column, weight=1)


    def set(self, row, column, value):
        widget = self._widgets[row][column]
        widget.configure(text=value)

if __name__ == "__main__":
    app = ExampleApp()
    app.attributes('-topmost', True)
    app.mainloop()
