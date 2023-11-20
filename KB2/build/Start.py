from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(
    r"D:\Visual Studio Code\Kuliah SMT 3\KB2\build\assets\frame0"
)

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
    bg="#4D7C8A",
    height=720,
    width=1280,
    bd=0,
    highlightthickness=0,
    relief="ridge",
)

canvas.place(x=0, y=0)
canvas.create_text(
    250.0,
    62.0,
    anchor="nw",
    text="BODY MASS INDEX",
    fill="#FFFFFF",
    font=("Cornerstone", 64 )
)

image_image_start = PhotoImage(file=relative_to_assets("image_start.png"))
image_start = canvas.create_image(639.0, 346.0, image=image_image_start)

button_image_start = PhotoImage(file=relative_to_assets("button_start.png"))

button_start = Button(
    image=button_image_start,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_start clicked"),
    relief="flat",
    bg = "#4D7C8A",
    activebackground = "#4D7C8A",
)
button_start.place(x=262.0, y=605.0, width=280.0, height=56.0)

button_image_2 = PhotoImage(file=relative_to_assets("button_penggunaan.png"))
button_penggunaan = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_penggunaan clicked"),
    relief="flat",
    bg = "#4D7C8A",
    activebackground = "#4D7C8A",
)
button_penggunaan.place(x=737.0, y=605.0, width=280.0, height=56.0)
window.resizable(False, False)
window.mainloop()
