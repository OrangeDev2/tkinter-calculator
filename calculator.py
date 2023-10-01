import tkinter as tk
from tkinter import ttk

class Calculator():
    def __init__(self):
        self.root = tk.Tk()
        self.input = ""
        self.buttons = [ ["AC","()","%", "/"],
                        ["7", "8", "9", "X"],
                        ["4", "5", "6", "-"],
                        ["1", "2", "3", "+"],
                        ["0", ".", "Del","="]  
                       ]
        
        self.create_window()
        self.inject_buttons()

    def create_window(self):
        root = self.root

        root.title("Hi, Mom")
        root.iconbitmap('./BLE.ico')

        window_width = 400
        window_height = 700

        # get the screen dimension
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # find the center point
        center_x = int(screen_width/2 - window_width / 2)
        center_y = int(screen_height/2 - window_height / 2)

        # set the position of the window to the center of the screen
        root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y-20}')


    def button_clicked():
        print('Button clicked')

    def number_key_pressed(event):
        if (event.char): #ignores empty string such as CAP LOCK
            input += event.char

    def inject_buttons(self):
        root = self.root
        buttons = self.buttons

        for i in range(0, len(buttons)):
            for j in range(0, len(buttons[i])):
                button = ttk.Button(root, text=f"{buttons[i][j]}")
                button.pack()

if __name__ == "__main__":
    #root.bind(f'<KeyPress>', Calculator.number_key_pressed)
    calculator = Calculator()
    calculator.root.mainloop()
