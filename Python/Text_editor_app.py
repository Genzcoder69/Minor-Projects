# import tkinter for windows, lables and buttons
import tkinter as tkt
from tkinter import filedialog,messagebox,colorchooser

def newFile():
    text.delete(1.0, tkt.END)

def openFile():
    file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, 'r') as file:
            text.delete(1.0,tkt.END)
            text.insert(tkt.END, file.read())

def saveFile():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files","*.txt")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text.get(1.0, tkt.END))
            messagebox.showinfo("Info", "File saves successfully !!")

def setColor(color):
    text.config(fg=color)
def chooseCustomColor():
    color = colorchooser.askcolor(title="Pick a custom color")[1]
    if color:
        text.config(fg=color)

# --- Preset colors ---
COLORS = [
    ("Black",   "#000000"),
    ("Blue",    "#1a73e8"),
    ("Red",     "#e53935"),
    ("Green",   "#2e7d32"),
    ("Purple",  "#6a1b9a"),
    ("Orange",  "#ef6c00"),
    ("Teal",    "#00695c"),
    ("Gray",    "#546e7a"),
]

root = tkt.Tk()
root.title("My Notepad")
root.geometry("800x600")

menu = tkt.Menu(root)
root.config(menu=menu)

# ---- File menu
file_menu = tkt.Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=newFile)
file_menu.add_command(label="Open", command=openFile)
file_menu.add_command(label="Save", command=saveFile)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# --- Text color menu
color_menu = tkt.Menu(menu, tearoff=0)
menu.add_cascade(label="Text Color", menu=color_menu)

for name, hex_code in COLORS:
    color_menu.add_command(
        label=f"● {name}",
        # tints the label itself
        foreground=hex_code,
        command=lambda c=hex_code: setColor(c)
    )
color_menu.add_separator()
color_menu.add_command(label="Custom color…", command=chooseCustomColor)

# --- Editor ---
text = tkt.Text(root, wrap=tkt.WORD, font=("Helvetica", 12), fg="#000000")
text.pack(expand=tkt.YES, fill=tkt.BOTH)

root.mainloop()