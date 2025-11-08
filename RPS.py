import random
import tkinter as tk
from PIL import Image, ImageTk # type: ignore

def prs():
    global result_label, gif_label, play_again_button
    print("LETS PLAY THE ROCK, PAPER, SCISSOR")
    str1 = str(input("ENTER THE CHOICE (rock, paper, scissor): "))
    str2 = random.choice(["rock", "paper", "scissor"])
    print(f"Computer chose: {str2}")

    if str1 == str2:
        result_label.config(text="TIE")
        play_again_button.pack()
    elif (str1 == "rock" and str2 == "scissor") or \
         (str1 == "paper" and str2 == "rock") or \
         (str1 == "scissor" and str2 == "paper"):
        result_label.config(text="YOU WON")
        display_gif('winner.gif')
    else:
        result_label.config(text="YOU LOST")
        play_again_button.pack()

def play_again():
    result_label.config(text="")
    gif_label.config(image="")
    gif_label.image = None
    play_again_button.pack_forget()
    prs()

def display_gif(gif_path):
    try:
        gif = Image.open(gif_path)
        frames = []
        for frame in range(gif.n_frames):
            gif.seek(frame)
            photo = ImageTk.PhotoImage(gif.copy().convert('RGBA').resize((500, 500), Image.LANCZOS))
            frames.append(photo)

        def update_gif(index=0):
            frame = frames[index]
            gif_label.config(image=frame)
            gif_label.image = frame
            root.after(gif.info['duration'], update_gif, (index + 1) % len(frames))

        update_gif()
    except FileNotFoundError:
        result_label.config(text=f"GIF not found: {gif_path}")
    except Exception as e:
        result_label.config(text=f"Error displaying GIF: {e}")

# GUI setup
root = tk.Tk()
root.title("Rock, Paper, Scissors")

result_label = tk.Label(root, text="", font=("Arial Black", 20),fg="black")
result_label.pack(pady=10)

gif_label = tk.Label(root)
gif_label.pack()

play_again_button = tk.Button(root, text="Play Again", command=play_again)

prs()
root.mainloop()
