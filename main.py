from data import Data
from output_wndw import OutputWindow, OutputGraph
# import tkinter.messagebox
import customtkinter


class App(customtkinter.CTk):
    def __init__(self, title: str) -> None:
        super().__init__()

        dft_font = customtkinter.CTkFont(family='consolas', size=14)

        self.geometry(f"{1100}x{720}")
        self.title(title)

        self.sidebar_frame = customtkinter.CTkFrame(self,
                                                    width=140,
                                                    corner_radius=0
                                                    )
        self.sidebar_frame.grid(row=0, column=0, rowspan=100, sticky="nsew")

        self.tab_wdw = customtkinter.CTkTabview(self, width=570)
        self.tab_wdw.grid(row=0,
                          column=2,
                          sticky="nsew"
                          )
        # self.tab_wdw.add("Dist Tab")
        # self.tab_wdw.add("Val Tab")
        # # self.tabview.add("Tab 3")
        # self.tab_wdw.tab("Dist Tab").grid_columnconfigure(0, weight=1)
        # self.tab_wdw.tab("Val Tab").grid_columnconfigure(0, weight=1)

        self.input1 = customtkinter.CTkTextbox(self,
                                               width=700,
                                               height=160,
                                               font=dft_font
                                               )
        self.input1.grid(
            column=1, row=2,
            columnspan=3,
        )

        self.clr_btn = customtkinter.CTkButton(self,
                                               text='LIMPAR',
                                               command=lambda:
                                               self.clr_input(),
                                               font=dft_font
                                               )
        self.clr_btn.grid(padx=20, pady=20, column=1, row=3, sticky="ew")

        self.format_btn = customtkinter.CTkButton(self,
                                                  text="DISTRIBUIR",
                                                  command=lambda:
                                                  self.create_freq(
                                                      self.
                                                      input1.
                                                      get(
                                                          1.0,
                                                          'end'
                                                      )
                                                  ),
                                                  font=dft_font
                                                  )
        self.format_btn.grid(padx=20, pady=20, column=2, row=3, sticky="ew")

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)

        self.ext_btn = customtkinter.CTkButton(self,
                                               text='SAIR',
                                               command=lambda: self.quit(),
                                               font=dft_font
                                               )
        self.ext_btn.grid(padx=20, pady=20, column=3, row=3, sticky="ew")

    def create_freq(self, data: str) -> None:
        try:
            user_input = data.strip().split(' ')
            number_input = [
                float(number)
                for number in [*user_input]
            ]
            d = Data(*number_input)
            OutputWindow("Tabela", d.tabulated_data)
            OutputGraph(d.freq_dist.classes_range, d.freq_dist.get_fi)

        except (TypeError, ValueError) as e:
            print("Erro de entrada!", e)

    def clr_input(self):
        self.input1.delete(1.0, "end")


if __name__ == '__main__':
    root = App("Distribuidor de Frequência")
    root.mainloop()
