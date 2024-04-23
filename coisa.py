import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt


def plot_bar_chart():
    data = {'A': 10, 'B': 15, 'C': 7, 'D': 10}  # Dadospara o gráfico de barras
    labels = list(data.keys())
    values = list(data.values())

    fig, ax = plt.subplots()
    ax.bar(labels, values)

    ax.set_xlabel('Categoria')
    ax.set_ylabel('Valores')
    ax.set_title('Gráfico de Barras')

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack()


root = tk.Tk()
root.title("Gráfico de Barras com Tkinter e Matplotlib")

plot_button = tk.Button(root, text="Plotar Gráfico de Barras",
                        command=plot_bar_chart)
plot_button.pack()

root.mainloop()
