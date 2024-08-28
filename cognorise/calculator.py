import tkinter as tk
from tkinter import ttk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.geometry("250x400")
        self.configure(bg="black")
        
        self.expression = ""
        self.history = []

       
        self.display_frame = self.create_display_frame()

       
        self.buttons_frame = self.create_buttons_frame()

      
        self.history_frame = self.create_history_frame()
        
        self.create_display_labels()
        self.create_buttons()
        self.create_history_listbox()
    
    def create_display_frame(self):
        frame = tk.Frame(self, height=70, bg="black")
        frame.pack(expand=False, fill="both")
        return frame
    
    def create_buttons_frame(self):
        frame = tk.Frame(self, height=150, bg="black")
        frame.pack(expand=True, fill="both")
        return frame

    def create_history_frame(self):
        frame = tk.Frame(self, height=130, bg="black")
        frame.pack(expand=False, fill="both")
        return frame
    
    def create_display_labels(self):
        self.total_label = tk.Label(self.display_frame, text="", anchor=tk.E, bg="black", fg="white", padx=10, font=("Arial", 16))
        self.total_label.pack(expand=True, fill="both")

        self.label = tk.Label(self.display_frame, text="", anchor=tk.E, bg="black", fg="white", padx=10, font=("Arial", 28))
        self.label.pack(expand=True, fill="both")

    def create_history_listbox(self):
        self.history_label = tk.Label(self.history_frame, text="History", anchor=tk.W, bg="black", fg="white", padx=10, font=("Arial", 14))
        self.history_label.grid(row=0, column=0, columnspan=4, sticky="nsew")

        self.clear_history_button = tk.Button(self.history_frame, text="Clear History", command=self.clear_history, bg="black", fg="orange", font=("Arial", 12))
        self.clear_history_button.grid(row=0, column=4, sticky="nsew")

        self.history_listbox = tk.Listbox(self.history_frame, bg="black", fg="white", font=("Arial", 12))
        self.history_listbox.grid(row=1, column=0, columnspan=5, sticky="nsew")

        self.history_frame.rowconfigure(1, weight=1)
        self.history_frame.columnconfigure([0, 1, 2, 3, 4], weight=1)
    
    def add_to_expression(self, value):
        self.expression += str(value)
        self.update_label()
    
    def update_label(self):
        self.label.config(text=self.expression[:21])
    
    def evaluate(self):
        try:
            self.total_label.config(text=self.expression)
            result = str(eval(self.expression))
            self.history.append(self.total_label.cget("text") + " = " + result)
            self.expression = result
            self.update_history_listbox()
            self.update_label()
        except Exception as e:
            self.expression = "Error"
            self.update_label()
    
    def update_history_listbox(self):
        self.history_listbox.delete(0, tk.END)
        for item in self.history:
            self.history_listbox.insert(tk.END, item)

    def clear_history(self):
        self.history = []
        self.update_history_listbox()
    
    def clear(self):
        self.expression = ""
        self.total_label.config(text="")
        self.update_label()
    
    def create_buttons(self):
        button_texts = [
            ["AC", "C", "%", "/"],
            [7, 8, 9, "*"],
            [4, 5, 6, "-"],
            [1, 2, 3, "+"],
            ["", 0, ".", "="]
        ]

        for row, texts in enumerate(button_texts):
            for col, text in enumerate(texts):
                button = tk.Button(self.buttons_frame, text=str(text), bg="#333", fg="orange" if text in ["AC", "C", "%", "/", "*", "-", "+", "="] else "white", font=("Arial", 16), borderwidth=0)
                button.grid(row=row, column=col, sticky=tk.NSEW)
                button.config(command=lambda t=text: self.on_button_click(t))
        
        for i in range(5):
            self.buttons_frame.rowconfigure(i, weight=1)
            self.buttons_frame.columnconfigure(i, weight=1)
    
    def on_button_click(self, char):
        if char in ["AC", "C"]:
            self.clear()
        elif char == "=":
            self.evaluate()
        else:
            self.add_to_expression(char)

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
