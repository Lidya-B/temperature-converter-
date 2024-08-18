# ****************************************************************************************************
#
# File name:   FtoC.py
# Description:
#       This program coverts Celsius to Fahrenheit and vice vera.
#
# ****************************************************************************************************

import tkinter
import messagebox


# ****************************************************************************************************

class Converter:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.frame1 = tkinter.Frame(self.main_window)
        self.label1 = tkinter.Label(self.frame1, text='Celsius:')
        self.degree_entry1 = tkinter.Entry(self.frame1, width=20)
        self.calculate_CtoF = tkinter.Button(
            self.frame1,
            text='Calculate Celsius to Fahrenheit',
            command=self.CtoF_calculation
        )

        self.label1.pack(side='left')
        self.degree_entry1.pack(side='left')
        self.calculate_CtoF.pack(side='left')

        self.frame1.pack()

        self.frame2 = tkinter.Frame(self.main_window)
        self.label2 = tkinter.Label(self.frame2, text='Fahrenheit:')
        self.degree_entry2 = tkinter.Entry(self.frame2, width=20)
        self.calculate_FtoC = tkinter.Button(
            self.frame2,
            text='Calculate Fahrenheit to Celsius',
            command=self.FtoC_calculation
        )

        self.label2.pack(side='left')
        self.degree_entry2.pack(side='left')
        self.calculate_FtoC.pack(side='left')

        self.frame2.pack()

        self.frame3 = tkinter.Frame(self.main_window)
        self.quit_button = tkinter.Button(
            self.frame3,
            text='Quit',
            command=self.main_window.destroy
        )

        self.quit_button.pack()

        self.frame3.pack(side='bottom')

        tkinter.mainloop()

# ****************************************************************************************************

    def CtoF_calculation(self):
        try:
            celsius = float(self.degree_entry1.get())
            fahrenheit = (celsius * 9 / 5) + 32
            self.degree_entry2.insert(0, f'{fahrenheit:.10f}')
        except ValueError:
            messagebox.showerror('Error', 'Invalid input. Please enter a valid number.')

 # ****************************************************************************************************

    def FtoC_calculation(self):
        try:
            fahrenheit = float(self.degree_entry2.get())
            celsius = (fahrenheit - 32) * 5 / 9
            self.degree_entry1.insert(0, f'{celsius:.10f}')
        except ValueError:
            messagebox.showerror('Error', 'Invalid input. Please enter a valid number.')


# ****************************************************************************************************


if __name__ == "__main__":
    converter = Converter()

# ****************************************************************************************************
