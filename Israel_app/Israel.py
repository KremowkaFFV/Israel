import tkinter as tk
from PIL import Image, ImageTk, ImageSequence
import pygame
import os
import sys

# === ŚCIEŻKI ===
BASE_PATH = os.path.dirname(os.path.abspath(__file__))
GIF_PATH = os.path.join(BASE_PATH, "Gifen.gif")
MUSIC_PATH = os.path.join(BASE_PATH, "music.mp3")


class GifMusicApp:
    def __init__(self, root):
        self.root = root

        # === OKNO ===
        self.root.title("🇮🇱Israel Dance!🇮🇱")
        self.root.configure(bg="black")
        self.root.attributes("-topmost", True)
        self.root.resizable(False, False)

        # zamknięcie okna przez X
        self.root.protocol("WM_DELETE_WINDOW", self.close_app)

        # === AUDIO ===
        try:
            pygame.mixer.init()

            if os.path.exists(MUSIC_PATH):
                pygame.mixer.music.load(MUSIC_PATH)
                pygame.mixer.music.play(-1)   # nieskończona pętla
            else:
                print("Brak pliku:", MUSIC_PATH)

        except Exception as e:
            print("Audio nie działa:", e)

        # === GIF ===
        if not os.path.exists(GIF_PATH):
            print("Nie znaleziono GIFa:", GIF_PATH)
            sys.exit()

        try:
            self.img = Image.open(GIF_PATH)
        except Exception as e:
            print("Błąd GIF:", e)
            sys.exit()

        self.frames = []
        self.delays = []

        for frame in ImageSequence.Iterator(self.img):
            self.frames.append(
                ImageTk.PhotoImage(frame.copy().convert("RGBA"))
            )

            delay = frame.info.get("duration", 100)
            if delay < 20:
                delay = 100

            self.delays.append(delay)

        self.current_frame = 0

        # === LABEL ===
        self.label = tk.Label(self.root, bg="black", bd=0)
        self.label.pack()

        # === WYŚRODKOWANIE ===
        w, h = self.img.size
        x = (self.root.winfo_screenwidth() // 2) - (w // 2)
        y = (self.root.winfo_screenheight() // 2) - (h // 2)

        self.root.geometry(f"{w}x{h}+{x}+{y}")

        # === START ===
        self.animate()

    def animate(self):
        self.label.config(image=self.frames[self.current_frame])

        delay = self.delays[self.current_frame]
        self.current_frame = (self.current_frame + 1) % len(self.frames)

        self.root.after(delay, self.animate)

    def close_app(self):
        try:
            pygame.mixer.music.stop()
            pygame.mixer.quit()
        except:
            pass

        self.root.destroy()
        sys.exit()


if __name__ == "__main__":
    root = tk.Tk()
    app = GifMusicApp(root)
    root.mainloop()
