import tkinter as tk
import math
import random

HUMAN = "X"
AI = "O"
EMPTY = ""
AI_MISTAKE_RATE = 0.3

BG = "#0b1220"
CELL = "#1f2933"
X_COLOR = "#38bdf8"
O_COLOR = "#f87171"
TEXT = "#e5e7eb"
ACCENT = "#22c55e"

board = [EMPTY]*9
buttons = []
game_over = False
ai_starts = False

def is_winner(p):
    wins = [(0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)]
    return any(board[a]==board[b]==board[c]==p for a,b,c in wins)

def is_draw():
    return EMPTY not in board

def minimax(is_max):
    if is_winner(AI): return 1
    if is_winner(HUMAN): return -1
    if is_draw(): return 0

    if is_max:
        best=-math.inf
        for i in range(9):
            if board[i]==EMPTY:
                board[i]=AI
                best=max(best,minimax(False))
                board[i]=EMPTY
        return best
    else:
        best=math.inf
        for i in range(9):
            if board[i]==EMPTY:
                board[i]=HUMAN
                best=min(best,minimax(True))
                board[i]=EMPTY
        return best

def best_move():
    if random.random() < AI_MISTAKE_RATE:
        return random.choice([i for i in range(9) if board[i]==EMPTY])

    best=-math.inf
    move=0
    for i in range(9):
        if board[i]==EMPTY:
            board[i]=AI
            score=minimax(False)
            board[i]=EMPTY
            if score>best:
                best=score
                move=i
    return move

def end_game(msg):
    global game_over
    game_over = True
    status.config(text=msg)
    for b in buttons:
        b.config(state=tk.DISABLED)

def reset_game():
    global board, game_over
    board=[EMPTY]*9
    game_over=False

    for b in buttons:
        b.config(text="", state=tk.NORMAL, fg=TEXT)

    status.config(text="Your turn" if not ai_starts else "AI thinking...")

    if ai_starts:
        root.after(300, ai_turn)

def ai_turn():
    if game_over: return
    status.config(text="AI thinking...")
    root.after(300, play_ai)

def play_ai():
    if game_over: return
    m = best_move()
    board[m]=AI
    buttons[m].config(text=AI, fg=O_COLOR, state=tk.DISABLED)

    if is_winner(AI):
        end_game("AI WON")
    elif is_draw():
        end_game("DRAW")
    else:
        status.config(text="Your turn")

def click(i):
    if board[i]!=EMPTY or game_over:
        return

    board[i]=HUMAN
    buttons[i].config(text=HUMAN, fg=X_COLOR, state=tk.DISABLED)

    if is_winner(HUMAN):
        end_game("YOU WON")
    elif is_draw():
        end_game("DRAW")
    else:
        ai_turn()

def start_match(ai_first):
    global ai_starts
    ai_starts = ai_first
    start_frame.pack_forget()
    game_frame.pack()
    reset_game()

root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry("420x520")
root.configure(bg=BG)
root.resizable(False, False)

start_frame = tk.Frame(root, bg=BG)
start_frame.pack(expand=True)

tk.Label(
    start_frame,
    text="Tic Tac Toe",
    font=("Segoe UI", 20, "bold"),
    fg=TEXT,
    bg=BG
).pack(pady=20)

tk.Label(
    start_frame,
    text="Who should begin?",
    font=("Segoe UI", 13),
    fg="#9ca3af",
    bg=BG
).pack(pady=10)

tk.Button(
    start_frame,
    text="You Begin",
    font=("Segoe UI", 12, "bold"),
    bg=ACCENT,
    fg="black",
    width=16,
    height=2,
    command=lambda: start_match(False)
).pack(pady=8)

tk.Button(
    start_frame,
    text="AI Begins",
    font=("Segoe UI", 12, "bold"),
    bg=CELL,
    fg=TEXT,
    width=16,
    height=2,
    command=lambda: start_match(True)
).pack(pady=8)

game_frame = tk.Frame(root, bg=BG)

reset_btn = tk.Button(
    game_frame,
    text="New Match",
    font=("Segoe UI", 12, "bold"),
    bg=ACCENT,
    fg="black",
    width=16,
    command=reset_game
)
reset_btn.pack(pady=10)

status = tk.Label(
    game_frame,
    text="",
    font=("Segoe UI", 14, "bold"),
    fg=ACCENT,
    bg=BG
)
status.pack()

grid = tk.Frame(game_frame, bg=BG)
grid.pack(pady=10)

for i in range(9):
    b = tk.Button(
        grid,
        text="",
        font=("Segoe UI", 26, "bold"),
        width=3,
        height=2,
        bg=CELL,
        fg=TEXT,
        command=lambda i=i: click(i)
    )
    b.grid(row=i//3, column=i%3, padx=8, pady=8)
    buttons.append(b)

root.mainloop()
