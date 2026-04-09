import tkinter as tk
from PIL import Image, ImageTk, ImageSequence
import pygame
import sys
import os

# Ścieżki do plików (zakładamy instalację w /opt/my_gif_app/)
BASE_PATH = "/opt/Israel_app"
GIF_PATH = os.path.join(BASE_PATH, "Gifen.gif")
MUSIC_PATH = os.path.join(BASE_PATH, "music.mp3")

class GifMusicApp:
    def __init__(self, root):
        self.root = root
        self.root.overrideredirect(True)  # Usuwa ramkę okna
        self.root.attributes("-topmost", True)  # Zawsze na wierzchu

        # Opcjonalnie: przeźroczystość (zależy od kompozytora okien w Linuxie)
        self.root.wait_visibility(self.root)
        self.root.attributes("-alpha", 0.9)

        # Inicjalizacja muzyki przez pygame
        pygame.mixer.init()
        if os.path.exists(MUSIC_PATH):
            pygame.mixer.music.load(MUSIC_PATH)
            pygame.mixer.music.play()
        else:
            print(f"Błąd: Nie znaleziono pliku muzyki w {MUSIC_PATH}")
            sys.exit()

        # Obsługa GIFa przez PIL
        self.img = Image.open(GIF_PATH)
        self.frames = [ImageTk.PhotoImage(frame.copy().convert('RGBA'))
                       for frame in ImageSequence.Iterator(self.img)]
        self.current_frame = 0

        self.label = tk.Label(root, image=self.frames[0], bd=0, bg='black')
        self.label.pack()

        # Wyśrodkowanie na ekranie
        self.root.update_idletasks()
        w, h = self.img.size
        x = (self.root.winfo_screenwidth() // 2) - (w // 2)
        y = (self.root.winfo_screenheight() // 2) - (h // 2)
        self.root.geometry(f'{w}x{h}+{x}+{y}')

        self.animate()
        self.check_music()

    def animate(self):
        self.current_frame = (self.current_frame + 1) % len(self.frames)
        self.label.configure(image=self.frames[self.current_frame])
        self.root.after(100, self.animate)

    def check_music(self):
        # Jeśli muzyka przestała grać, zamknij aplikację
        if not pygame.mixer.music.get_busy():
            self.root.destroy()
            sys.exit()
        self.root.after(500, self.check_music)

if __name__ == "__main__":
    root = tk.Tk()
    app = GifMusicApp(root)
    root.mainloop()
