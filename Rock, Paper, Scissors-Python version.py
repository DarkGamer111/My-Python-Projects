import random
import tkinter as tk

def get_user_choice():
    user_choice = user_entry.get().lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        user_choice = user_entry.get().lower()
    return user_choice

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'paper' and computer_choice == 'rock') or
        (user_choice == 'scissors' and computer_choice == 'paper')
    ):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    result_var.set(f"You chose {user_choice.capitalize()}.\nComputer chose {computer_choice.capitalize()}.\n{determine_winner(user_choice, computer_choice)}")
    restart_button.pack()

def restart_game():
    user_entry.delete(0, tk.END)
    result_var.set("")
    restart_button.pack_forget()

# GUI setup
root = tk.Tk()
root.title("Rock, Paper, Scissors Game")

user_label = tk.Label(root, text="Enter choice (Rock, Paper, Scissors):")
user_entry = tk.Entry(root)
user_label.pack()
user_entry.pack()

play_button = tk.Button(root, text="Play", command=play_game)
play_button.pack()

result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var)
result_label.pack()

restart_button = tk.Button(root, text="Restart Game", command=restart_game)

root.mainloop()

