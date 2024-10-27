import tkinter as tk
class ClickerGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Clicker Game")
        self.root.geometry("400x300")

        self.score = 0

        self.score_label = tk.Label(root, text="Score: 0", font=("Arial", 36), fg="blue")
        self.score_label.pack(pady=20)

        self.click_button = tk.Button(root, text="Click Me!", font=("Arial", 24), command=self.increment_score)
        self.click_button.pack(pady=20)

        self.reset_button = tk.Button(root, text="Reset", font=("Arial", 24), command=self.reset_score)
        self.reset_button.pack(pady=20)

    def increment_score(self):
        self.score += 1
        self.score_label.config(text=f"Score: {self.score}")

    def reset_score(self):
        self.score = 0
        self.score_label.config(text="Score: 0")

if __name__ == "__main__":
    root = tk.Tk()
    game = ClickerGame(root)
    root.mainloop()