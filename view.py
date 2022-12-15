import tkinter as tk

class View(tk.Tk):

    PAD = 10
    MAX_BUTTONS_PER_ROW = 4
    button_captions = [
        'C', '+/-', '%', '/',
        7, 8, 9, '*',
        4, 5, 6, '-',
        1, 2, 3, '+',
        0, '.', '='
    ]

    def __init__(self):
        super().__init__()
        self.title("Calculadora")
        self.resizable(False, False)
        self.value_var = tk.StringVar()
        self._make_main_frame()
        self._make_entry()
        self._make_buttons()
        self._center_window()
    
    def set_controller(self, controller):
        self.controller = controller
    
    def run(self):
        self.mainloop()
    

    def _make_main_frame(self): # Cria barra para inserção de valores
        self.main_frame = tk.Frame(self)
        self.main_frame.pack(padx=self.PAD, pady=self.PAD)

    def _make_entry(self): # Permite a inserção de valores
        entry = tk.Entry(self.main_frame, justify='right', textvariable=self.value_var, state='readonly', font=('Arial', 16))
        entry.pack(fill='x')
    
    def _make_buttons(self): # Cria os botões da calculadora
        outer_frame = tk.Frame(self.main_frame)
        outer_frame.pack()

        inner_frame = tk.Frame(outer_frame)
        inner_frame.pack()

        buttons_in_row = 0

        for caption in self.button_captions:
            if caption == 0:
                fill = 'x'
                expand = 1
            else:
                fill = 'none'
                expand = 0
            if buttons_in_row == self.MAX_BUTTONS_PER_ROW:
                inner_frame = tk.Frame(outer_frame)
                inner_frame.pack(fill='x')
                buttons_in_row = 0
            button = tk.Button(inner_frame, text=caption, padx=10, command=(lambda clicked_button=caption: self.controller.on_button_click(clicked_button)), width=5)
            button.pack(fill=fill, expand=expand, side='left')
            buttons_in_row += 1
    
    def _center_window(self): # Faz a calculadora iniciar no meio da tela
        self.update()

        width = self.winfo_width()
        height = self.winfo_height()

        x_offset = (self.winfo_screenwidth() - width) // 2
        y_offset = (self.winfo_screenheight() - height) // 2

        self.geometry(f'{width}x{height}+{x_offset}+{y_offset}')