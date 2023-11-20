
from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\Visual Studio Code\Kuliah SMT 3\KB2\build\assets\frame4")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x_center = 100
y_center = 40
# Set the window position to be centered
window.geometry(f"1280x720+{x_center}+{y_center}")
window.configure(bg="#4D7C8A")


canvas = Canvas(
    window,
    bg = "#4D7C8A",
    height = 720,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_text(
    500.0,
    10.0,
    anchor="nw",
    text="Hasil",
    fill="#FFFFFF",
    font=("AnekLatin Regular", 64)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    889.0,
    387.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=574.0,
    y=121.0,
    width=630.0,
    height=530.0
)

canvas.create_text(
    70.0,
    150.0,
    anchor="nw",
    text="KATEGORI BMI ANDA:",
    fill="#FFFFFF",
    font=("AnekLatin Regular", 30)
)

canvas.create_text(
    120.0,
    546.0,
    anchor="nw",
    text="overweight",
    fill="#FFFFFF",
    font=("Cornerstone", 64 * -1)
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    284.0,
    357.0,
    image=image_image_1
)
window.resizable(False, False)
window.mainloop()
