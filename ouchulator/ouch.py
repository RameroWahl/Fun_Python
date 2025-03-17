import tkinter as tk
import random

# List of "ouch" variations
OUCH_PHRASES = [
    "Oof!", "Yeowch!", "That smarts!", "Ow!", "Not again!", "Why must you hurt me?", 
    "Oh no, not the 7 key!", "I trusted you...", "Zounds!", "My digits!", "AHHHHHHHH!", 
    "I didn't sign up for this!", "Ouchie!", "Stop the violence!", "Have mercy!"
]

class Ouchulator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ouchulator")
        self.geometry("300x400")
        self.configure(bg="lightgray")

        self.display = tk.Entry(self, font=("Arial", 24), justify="right", bd=10, relief=tk.RIDGE)
        self.display.pack(pady=10, padx=10, fill=tk.BOTH)

        self.ouch_label = tk.Label(self, text="", font=("Arial", 14, "bold"), fg="red", bg="lightgray")
        self.ouch_label.pack()

        self.create_buttons()

    def create_buttons(self):
        button_frame = tk.Frame(self, bg="lightgray")
        button_frame.pack(pady=10)
        
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2),
            ('0', 4, 1)
        ]
        
        for (text, row, col) in buttons:
            btn = tk.Button(button_frame, text=text, font=("Arial", 20), width=5, height=2,
                            command=lambda t=text: self.button_pressed(t))
            btn.grid(row=row, column=col, padx=5, pady=5)

    def button_pressed(self, key):
        self.display.insert(tk.END, key)
        self.show_ouch()
    
    def show_ouch(self):
        self.ouch_label.config(text=random.choice(OUCH_PHRASES))
        self.after(1000, lambda: self.ouch_label.config(text=""))  # Reset after 1 sec

if __name__ == "__main__":
    app = Ouchulator()
    app.mainloop()
