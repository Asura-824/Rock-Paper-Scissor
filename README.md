# 🪨📄✂️ Rock, Paper, Scissors Game

A simple command-line and **partially integrated GUI** implementation of the classic Rock, Paper, Scissors game in Python. This version attempts to incorporate a graphical user interface (using `tkinter` and `Pillow`) to display a "YOU WON" GIF when the user wins.

**Note:** The current game flow still primarily uses **command-line input** for the player's choice, and the GUI elements like the result label and "Play Again" button are meant to display the outcome and handle the restart.

## ✨ Features

* Classic Rock, Paper, Scissors logic against the computer.
* Uses `tkinter` for displaying the result and a "Play Again" button.
* Attempts to display a **winner GIF** upon winning (requires a file named `winner.gif`).

## 🛠️ Prerequisites

To run this game, you need Python installed, along with the `tkinter` library (usually included with standard Python installations) and the `Pillow` library for handling image and GIF files.

* **Python 3.x**
* **Pillow** (`PIL`)

## 💻 Installation

1.  **Clone the repository** (if you're hosting this on GitHub):
    ```bash
    git clone https://github.com/Asura-824/Rock-Paper-Scissor.git
    cd rock-paper-scissors-game
    ```

2.  **Install the required Python library:**
    ```bash
    pip install Pillow
    ```

3.  **Add the GIF file:**
    Place a GIF file named `winner.gif` in the same directory as the Python script. This GIF will be displayed when the player wins.

## 🚀 How to Run

1.  Save the provided code as a Python file (e.g., `rps_game.py`).
2.  Run the script from your terminal:
    ```bash
    python rps_game.py
    ```

3.  **Interaction:**
    * The game will start, and the console will prompt you to **ENTER THE CHOICE (rock, paper, scissor)**.
    * Enter your choice in the terminal.
    * The computer's choice and the result ("TIE", "YOU WON", or "YOU LOST") will be displayed in both the console and the GUI window.
    * If you win, the `winner.gif` will attempt to play in the GUI window.
    * If the result is "TIE" or "YOU LOST", a "Play Again" button will appear in the GUI window to restart the game.

## 📁 Code Overview

The script combines command-line input with a `tkinter` GUI:

* **`prs()`:** Contains the core game logic, takes command-line input, determines the winner, and updates the GUI labels.
* **`play_again()`:** Resets the GUI and calls `prs()` to start a new round.
* **`display_gif(gif_path)`:** Handles opening and continuously animating the GIF using `PIL.ImageTk`.
* **GUI Setup:** Initializes the main `tkinter` window (`root`), result label, GIF display label, and the "Play Again" button.

---

## 🛑 Known Limitations

* Player input (`input()`) is still purely command-line based, which interrupts the GUI's responsiveness until input is provided. A better GUI design would use `tkinter` buttons for player choices.
* Requires a local file named `winner.gif` to display the winning animation.
