import customtkinter
import CTkTable
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np


class OutputWindow(customtkinter.CTk):
    def __init__(self, title: str, table_data: list[str]) -> None:
        super().__init__()

        self.title(title)
        tree = CTkTable.CTkTable(self)

        indexes = ["i", "classes", "fi", "fri", "Fi", "xi", "pi%"]

        for i, column in enumerate(indexes):
            tree.add_column('')
            tree.insert(column=i, row=0,  value=column)

        for i, data in enumerate(table_data):
            tree.add_row(data)

        tree.delete_row(1)
        tree.delete_columns([7, 8])
        tree.grid()

        self.mainloop()


class OutputGraph(customtkinter.CTk):
    def __init__(self, range_data, fi_values):
        super().__init__()

        self.x_axis = range_data
        self.y_axis = fi_values

        # Gerando cores para as barras
        num_bars = len(self.x_axis)
        colors = plt.cm.viridis(np.linspace(0, 1, num_bars))

        fig, ax = plt.subplots()
        ax.bar(self.x_axis, self.y_axis, width=10, color=colors)
        ax.set_xlabel('Classes')
        ax.set_ylabel('Valores')
        ax.set_title('Histograma')

        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.draw()
        canvas.get_tk_widget().pack()

        self.mainloop()


if __name__ == '__main__':
    out = OutputWindow("Tabela", ['1', '2', '3'])
