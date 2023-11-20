from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\Visual Studio Code\Kuliah SMT 3\KB2\build\assets\frame1")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()

window.geometry("1280x720")
window.configure(bg = "#4D7C8A")

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
    21.0,
    12.0,
    anchor="nw",
    text="Pilih Jenis Kelamin",
    fill="#FFFFFF",
    font=("AnekLatin Regular", 32 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    384.0,
    94.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=69.0,
    y=67.0,
    width=630.0,
    height=53.0
)

canvas.create_text(
    59.0,
    123.0,
    anchor="nw",
    text="Masukkan Berat Badan",
    fill="#FFFFFF",
    font=("AnekLatin Regular", 32 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    384.0,
    206.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=69.0,
    y=179.0,
    width=630.0,
    height=53.0
)

canvas.create_text(
    59.0,
    235.0,
    anchor="nw",
    text="Masukkan  Tinggi Badan",
    fill="#FFFFFF",
    font=("AnekLatin Regular", 32 * -1)
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    387.0,
    325.5,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=72.0,
    y=298.0,
    width=630.0,
    height=53.0
)

canvas.create_text(
    62.0,
    347.0,
    anchor="nw",
    text="Masukkan Usia",
    fill="#FFFFFF",
    font=("AnekLatin Regular", 32 * -1)
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    384.0,
    437.5,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=69.0,
    y=410.0,
    width=630.0,
    height=53.0
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    383.0,
    555.5,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_5.place(
    x=68.0,
    y=528.0,
    width=630.0,
    height=53.0
)

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(
    384.0,
    669.5,
    image=entry_image_6
)
entry_6 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_6.place(
    x=69.0,
    y=642.0,
    width=630.0,
    height=53.0
)

canvas.create_text(
    58.0,
    465.0,
    anchor="nw",
    text="Masukkan Frekuensi Olah-raga/Minggu",
    fill="#FFFFFF",
    font=("AnekLatin Regular", 32 * -1)
)

canvas.create_text(
    62.0,
    578.0,
    anchor="nw",
    text="Apakah Anda Berotot",
    fill="#FFFFFF",
    font=("AnekLatin Regular", 32 * -1)
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    991.0,
    296.0,
    image=image_image_1
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=874.0,
    y=606.0,
    width=280.0,
    height=56.0
)
window.resizable(False, False)
window.mainloop()
