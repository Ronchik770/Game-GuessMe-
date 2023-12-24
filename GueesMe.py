import tkinter as tk
from tkinter import messagebox
import random

class GuessNumberGame:
    def __init__(self, master):
        self.master = master
        self.master.title("GuessMe")
        self.master.geometry("300x250")

        self.secret_number = 0
        self.attempts = 0
        self.total_attempts = 0
        self.total_games = 0
        self.best_score = float('inf')

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.master, text="Welcome to GuessMe!")
        self.label.pack(pady=10)

        self.entry = tk.Entry(self.master)
        self.entry.pack(pady=5)

        self.guess_button = tk.Button(self.master, text="Try to Guess", command=self.check_guess)
        self.guess_button.pack(pady=5)

        self.restart_button = tk.Button(self.master, text="Restart", command=self.restart_game)
        self.restart_button.pack(pady=5)

        self.stats_button = tk.Button(self.master, text="Statistics", command=self.show_stats)
        self.stats_button.pack(pady=5)

        self.quit_button = tk.Button(self.master, text="Quit", command=self.master.destroy)
        self.quit_button.pack(pady=5)

        self.stats_label = tk.Label(self.master, text="")
        self.stats_label.pack(pady=10)

        self.restart_game()

    def restart_game(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.label.config(text="Welcome to GuessMe!")

    def check_guess(self):
        try:
            guess = int(self.entry.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter an integer.")
            return

        self.attempts += 1

        if guess == self.secret_number:
            messagebox.showinfo("Congratulations", f"You guessed the number {self.secret_number} in {self.attempts} attempts!")

            self.total_attempts += self.attempts
            self.total_games += 1

            if self.attempts < self.best_score:
                self.best_score = self.attempts
                messagebox.showinfo("New Record", f"New record! Best attempts: {self.best_score}")
            else:
                messagebox.showinfo("Best Attempts", f"Best attempts: {self.best_score}")

            self.restart_game()
        elif guess < self.secret_number:
            messagebox.showinfo("Try Again", "Your guess is less than the secret number. Try again.")
        else:
            messagebox.showinfo("Try Again", "Your guess is greater than the secret number. Try again.")

    def show_stats(self):
        if self.total_games == 0:
            avg_attempts = "N/A"
        else:
            avg_attempts = self.total_attempts / self.total_games

        stats_message = f"Total games: {self.total_games}\nAverage attempts: {avg_attempts:.2f}\nBest attempts: {self.best_score}"
        messagebox.showinfo("Statistics", stats_message)

if __name__ == "__main__":
    root = tk.Tk()
    app = GuessNumberGame(root)
    root.mainloop()
