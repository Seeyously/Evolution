#%%
import tkinter as tk

class Visualized2dArray(tk.Frame):
    def __init__(self, parent, rows=10, columns=2, width = 2, height = 1):
        tk.Frame.__init__(self, parent, background="black")
        self._widgets = []
        for row in range(rows):
            current_row = []
            for column in range(columns):
                label = tk.Label(self, borderwidth = 0, width = width, height = height)
                label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                current_row.append(label)
            self._widgets.append(current_row)

        for column in range(columns):
            self.grid_columnconfigure(column, weight=1)


    def set(self, row, column, value):
        widget = self._widgets[row][column]
        widget.configure(text=value)

if __name__ == "__main__":
    frame = tk.Tk()
    board = Visualized2dArray(frame, 10,10)
    board.pack(side = "top", fill="x")
    board.set(1,1,5)
    board.mainloop()