# main.py

import tkinter as tk
from tkinter import messagebox
from controlador import RegexController

class RegexApp:
    def __init__(self, root):
        self.root = root
        self.controller = RegexController(self)
        self.setup_ui()
    
    def setup_ui(self):
        self.root.title("Validador de Expresiones Regulares")
        
        # Entrada de expresión regular
        tk.Label(self.root, text="Expresión Regular:").pack()
        self.entry_regex = tk.Entry(self.root, width=50)
        self.entry_regex.pack()
        
        # Entrada de cadenas
        tk.Label(self.root, text="Cadenas para Validar:").pack()
        self.entry_strings = tk.Text(self.root, width=50, height=10)
        self.entry_strings.pack()
        
        # Botón de validación
        validate_button = tk.Button(self.root, text="Validar", command=self.on_validate)
        validate_button.pack()
        
        # Área de resultados
        tk.Label(self.root, text="Resultados:").pack()
        self.output_result = tk.Text(self.root, width=50, height=10, state=tk.DISABLED)
        self.output_result.pack()
    
    def on_validate(self):
        regex = self.entry_regex.get()
        strings = self.entry_strings.get("1.0", tk.END).splitlines()
        self.controller.validate_strings(regex, strings)
    
    def show_results(self, results):
        self.output_result.config(state=tk.NORMAL)
        self.output_result.delete("1.0", tk.END)
        for string, accepted in results.items():
            self.output_result.insert(tk.END, f"{string}: {'Aceptado' if accepted else 'Rechazado'}\n")
        self.output_result.config(state=tk.DISABLED)
    
    def show_error(self, message):
        messagebox.showerror("Error", str(message))

# Iniciar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = RegexApp(root)
    root.mainloop()
