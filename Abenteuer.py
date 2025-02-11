import tkinter as tk
import random

class AbenteuerGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Zufälliges Abenteuer")
        self.root.geometry("600x400")
        self.root.resizable(False, False)

        self.main_frame = tk.Frame(self.root, bg="#333333")
        self.main_frame.pack(fill="both", expand=True)

        self.text_label = tk.Label(
            self.main_frame, 
            text="", 
            fg="white", 
            bg="#333333", 
            font=("Helvetica", 14), 
            wraplength=580, 
            justify="left"
        )
        self.text_label.pack(pady=20)

        self.button_frame = tk.Frame(self.main_frame, bg="#333333")
        self.button_frame.pack(pady=10)

        # Level-Struktur und zufällige Pfade
        self.levels = [
            ("Ein seltsamer Nebel taucht auf. Gehst du mutig vorwärts?", ["Vorwärts", "Zurück"]),
            ("Ein Baum spricht zu dir: 'Wohin des Wegs?'", ["Links", "Rechts"]),
            ("Ein mysteriöser Händler bietet dir einen Keks an.", ["Nehmen", "Ablehnen"]),
            ("Du stehst vor einer finsteren Höhle.", ["Betreten", "Weggehen"])
        ]
        
        self.start_game()

    def clear_buttons(self):
        """Entfernt alle Buttons im Button-Frame."""
        for widget in self.button_frame.winfo_children():
            widget.destroy()

    def start_game(self):
        """Startet das Spiel neu."""
        self.current_level = 0
        self.show_level()

    def show_level(self):
        """Zeigt den aktuellen Level-Text und die Optionen."""
        if self.current_level < len(self.levels):
            level_text, options = self.levels[self.current_level]
            self.text_label.config(text=level_text)
            self.clear_buttons()
            
            for option in options:
                button = tk.Button(
                    self.button_frame,
                    text=option,
                    command=lambda opt=option: self.handle_choice(opt),
                    font=("Helvetica", 12),
                    width=15
                )
                button.pack(side="left", padx=10)
        else:
            self.show_victory()

    def handle_choice(self, choice):
        """Behandelt die Wahl des Spielers und geht zufällig zum nächsten Level."""
        self.text_label.config(text=f"Du hast dich für '{choice}' entschieden.")
        
        # Zufälliger Level-Sprung
        self.current_level = random.randint(0, len(self.levels) - 1)
        
        # Warte eine Sekunde für den Effekt, bevor der nächste Level kommt
        self.root.after(1000, self.show_level)

    def show_victory(self):
        """Zeigt den Siegbildschirm."""
        self.text_label.config(text=(
            "Herzlichen Glückwunsch!\n\n"
            "Du hast das Abenteuer überlebt – oder zumindest irgendwie beendet.\n"
            "Danke fürs Spielen!"
        ))
        self.clear_buttons()
        restart_button = tk.Button(
            self.button_frame, 
            text="Neustarten", 
            command=self.start_game, 
            font=("Helvetica", 12),
            width=15
        )
        restart_button.pack(pady=5)
        exit_button = tk.Button(
            self.button_frame, 
            text="Beenden", 
            command=self.root.quit, 
            font=("Helvetica", 12),
            width=15
        )
        exit_button.pack(pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    game = AbenteuerGame(root)
    root.mainloop()
