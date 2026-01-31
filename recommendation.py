import tkinter as tk
from tkinter import ttk, messagebox
import random

movies = [
    {"title": "3 Idiots", "genres": ["Comedy", "Drama"]},
    {"title": "Andhadhun", "genres": ["Thriller", "Crime"]},
    {"title": "Dangal", "genres": ["Drama", "Action"]},
    {"title": "Bhool Bhulaiyaa", "genres": ["Comedy", "Horror"]},
    {"title": "Hera Pheri", "genres": ["Comedy"]},
    {"title": "Drishyam", "genres": ["Thriller", "Crime"]},
    {"title": "ZNMD", "genres": ["Comedy", "Drama"]},
    {"title": "War", "genres": ["Action", "Thriller"]},
    {"title": "PK", "genres": ["Comedy", "Drama"]},
    {"title": "Stree", "genres": ["Comedy", "Horror"]},
    {"title": "Krrish", "genres": ["Sci-Fi", "Action"]},
    {"title": "Queen", "genres": ["Comedy", "Drama"]},
    {"title": "Article 15", "genres": ["Crime", "Drama"]},
    {"title": "Welcome", "genres": ["Comedy"]},
    {"title": "Special 26", "genres": ["Crime", "Thriller"]},
]

all_genres = sorted({g for m in movies for g in m["genres"]})

def recommend_one_genre(genre):
    matched = [m["title"] for m in movies if genre in m["genres"]]
    if len(matched) < 5:
        others = [m["title"] for m in movies if m["title"] not in matched]
        random.shuffle(others)
        matched.extend(others[:5 - len(matched)])
    random.shuffle(matched)
    return matched[:5]

class RoundedButton(tk.Canvas):
    def __init__(self, parent, text, command, width=220, height=50,
                 radius=25, bg="#2563eb", fg="white"):
        super().__init__(parent, width=width, height=height,
                         bg=parent["bg"], highlightthickness=0)
        self.command = command
        self.radius = radius
        self.bg_color = bg
        self.fg_color = fg
        self.rect = self.create_rounded_rect(2, 2, width-2, height-2, radius, fill=bg)
        self.label = self.create_text(width/2, height/2,
                                      text=text,
                                      fill=fg,
                                      font=("Segoe UI", 12, "bold"))
        self.bind("<Button-1>", lambda e: self.command())
        self.bind("<Enter>", self.on_hover)
        self.bind("<Leave>", self.on_leave)

    def create_rounded_rect(self, x1, y1, x2, y2, r, **kwargs):
        points = [
            x1+r, y1,
            x2-r, y1,
            x2, y1,
            x2, y1+r,
            x2, y2-r,
            x2, y2,
            x2-r, y2,
            x1+r, y2,
            x1, y2,
            x1, y2-r,
            x1, y1+r,
            x1, y1
        ]
        return self.create_polygon(points, smooth=True, **kwargs)

    def on_hover(self, _):
        self.itemconfig(self.rect, fill="#1d4ed8")

    def on_leave(self, _):
        self.itemconfig(self.rect, fill=self.bg_color)

root = tk.Tk()
root.title("Indian Movie Recommender")
root.geometry("560x600")
root.configure(bg="#eaf2ff")

style = ttk.Style()
style.theme_use("clam")

style.configure("TLabel",
                background="#eaf2ff",
                foreground="#0f172a",
                font=("Segoe UI", 11))

style.configure("Header.TLabel",
                font=("Segoe UI", 20, "bold"),
                foreground="#1e3a8a")

style.configure("TRadiobutton",
                background="#ffffff",
                font=("Segoe UI", 11))

ttk.Label(root,
          text="🎬 Indian Movie Recommender",
          style="Header.TLabel").pack(pady=20)

ttk.Label(root,
          text="Pick one genre and get curated Indian movie picks").pack()

card = tk.Frame(root, bg="white", bd=0)
card.pack(pady=20, padx=30, fill="x")

shadow = tk.Frame(root, bg="#dbeafe")
shadow.place(in_=card, relx=0.01, rely=0.02, relwidth=1, relheight=1)

card.lift()

selected_genre = tk.StringVar()

for g in all_genres:
    ttk.Radiobutton(card,
                    text=g,
                    value=g,
                    variable=selected_genre).pack(anchor="w",
                                                  padx=30,
                                                  pady=6)

def get_recommendations():
    genre = selected_genre.get()
    if not genre:
        messagebox.showwarning("Select Genre", "Please select one genre")
        return
    recs = recommend_one_genre(genre)
    result_box.delete(*result_box.get_children())
    for r in recs:
        result_box.insert("", "end", values=(r,))

btn = RoundedButton(root,
                    text="Recommend Movies",
                    command=get_recommendations)
btn.pack(pady=15)

result_frame = tk.Frame(root, bg="white")
result_frame.pack(padx=30, pady=15, fill="both", expand=True)

ttk.Label(result_frame,
          text="Top 5 Indian Movies",
          font=("Segoe UI", 12, "bold")).pack(pady=10)

result_box = ttk.Treeview(result_frame,
                          columns=("Movie",),
                          show="headings",
                          height=8)

result_box.heading("Movie", text="Recommendations")
result_box.column("Movie", width=460, anchor="center")
result_box.pack(pady=10)

root.mainloop()
