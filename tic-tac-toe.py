import tkinter as tk
from tkinter import messagebox

# Main window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Game state
current_player = "X"
board = [""] * 9
buttons = []

# Check win
def check_win(player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8], #It define the rows
        [0,3,6], [1,4,7], [2,5,8], #It defines the colume
        [0,4,8], [2,4,6]           #It define the cross match  
    ]
    return any(all(board[i] == player for i in cond) for cond in win_conditions)

# Check draw
def check_draw():
    return all(cell != "" for cell in board)

# On button click
def on_click(index):
    global current_player
    if board[index] == "":
        board[index] = current_player
        buttons[index].config(text=current_player, state="disabled")

        if check_win(current_player):
            messagebox.showinfo("Game Over", f"🎉 Player {current_player} wins!")
            disable_all_buttons()
        elif check_draw():
            messagebox.showinfo("Game Over", "🤝 It's a draw!")
            disable_all_buttons()
        else:
            current_player = "O" if current_player == "X" else "X"

# Disable all buttons
def disable_all_buttons():
    for btn in buttons:
        btn.config(state="disabled")

# Restart game
def restart_game():
    global board, current_player
    board = [""] * 9
    current_player = "X"
    for i in range(9):
        buttons[i].config(text="", state="normal")

# Layout buttons (3x3 grid)
for i in range(9):
    btn = tk.Button(root, text="", width=10, height=3, font=("Helvetica", 20),
                    command=lambda i=i: on_click(i))
    btn.grid(row=i//3, column=i%3)
    buttons.append(btn)

# Restart button
restart_btn = tk.Button(root, text="Restart", font=("Helvetica", 14), command=restart_game)
restart_btn.grid(row=3, column=0, columnspan=3, sticky="nsew")

# Start GUI
root.mainloop()
