from data import Data
# import customtkinter

if __name__ == '__main__':
    while True:
        try:
            user_input = input('Insira números: ')
            format_input = user_input.split(' ')
            number_input = [
                float(number)
                for number in [*format_input]
            ]
            d = Data(*number_input)
            print()
            print(d.freq_dist)

        except (TypeError, ValueError) as e:
            print("Erro de entrada!", e)


# root = customtkinter.CTk()
# root.geometry("500x500")
# root.title("Distribuidor de Frequências")


# root.mainloop()
