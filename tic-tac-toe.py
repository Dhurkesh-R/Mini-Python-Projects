import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.resizable(False, False)
        self.board = [[None for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.create_widgets()

    def create_widgets(self):
        for row in range(3):
            for col in range(3):
                button = tk.Button(self.root, text="", font=('normal', 40), width=5, height=2,
                                   command=lambda r=row, c=col: self.on_click(r, c))
                button.grid(row=row, column=col)
                self.board[row][col] = button

    def on_click(self, row, col):
        if self.board[row][col].cget("text") == "" and self.check_winner() is False:
            self.board[row][col].config(text=self.current_player)
            if self.check_winner():
                self.end_game(f"Player {self.current_player} wins!")
            elif self.check_tie():
                self.end_game("It's a tie!")
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        for row in range(3):
            if self.board[row][0].cget("text") == self.board[row][1].cget("text") == self.board[row][2].cget("text") != "":
                return True
        for col in range(3):
            if self.board[0][col].cget("text") == self.board[1][col].cget("text") == self.board[2][col].cget("text") != "":
                return True
        if self.board[0][0].cget("text") == self.board[1][1].cget("text") == self.board[2][2].cget("text") != "":
            return True
        if self.board[0][2].cget("text") == self.board[1][1].cget("text") == self.board[2][0].cget("text") != "":
            return True
        return False

    def check_tie(self):
        for row in range(3):
            for col in range(3):
                if self.board[row][col].cget("text") == "":
                    return False
        return True

    def end_game(self, message):
        messagebox.showinfo("Game Over", message)
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
