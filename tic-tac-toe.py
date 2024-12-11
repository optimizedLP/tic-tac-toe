import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Unbeatable Tic-Tac-Toe")
        self.board = [" " for _ in range(9)]
        self.current_player = "X"
        
        self.buttons = []
        for i in range(3):
            for j in range(3):
                button = tk.Button(master, text=" ", font=('Arial', 20), width=5, height=2,
                                   command=lambda row=i, col=j: self.make_move(row, col))
                button.grid(row=i, column=j)
                self.buttons.append(button)
        
    def make_move(self, row, col):
        index = 3 * row + col
        if self.board[index] == " ":
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            if self.check_winner(self.current_player):
                messagebox.showinfo("Game Over", f"{self.current_player} wins!")
                self.master.quit()
            elif " " not in self.board:
                messagebox.showinfo("Game Over", "It's a tie!")
                self.master.quit()
            else:
                self.current_player = "O"
                self.computer_move()

    def computer_move(self):
        best_score = float('-inf')
        best_move = None
        for i in range(9):
            if self.board[i] == " ":
                self.board[i] = "O"
                score = self.minimax(self.board, 0, False)
                self.board[i] = " "
                if score > best_score:
                    best_score = score
                    best_move = i
        
        self.board[best_move] = "O"
        self.buttons[best_move].config(text="O")
        if self.check_winner("O"):
            messagebox.showinfo("Game Over", "Computer wins!")
            self.master.quit()
        elif " " not in self.board:
            messagebox.showinfo("Game Over", "It's a tie!")
            self.master.quit()
        else:
            self.current_player = "X"

    def minimax(self, board, depth, is_maximizing):
        if self.check_winner("O"):
            return 1
        if self.check_winner("X"):
            return -1
        if " " not in board:
            return 0
        
        if is_maximizing:
            best_score = float('-inf')
            for i in range(9):
                if board[i] == " ":
                    board[i] = "O"
                    score = self.minimax(board, depth + 1, False)
                    board[i] = " "
                    best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(9):
                if board[i] == " ":
                    board[i] = "X"
                    score = self.minimax(board, depth + 1, True)
                    board[i] = " "
                    best_score = min(score, best_score)
            return best_score

    def check_winner(self, player):
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]  # Diagonals
        ]
        return any(all(self.board[i] == player for i in condition) for condition in win_conditions)

root = tk.Tk()
game = TicTacToe(root)
root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()