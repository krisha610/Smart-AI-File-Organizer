import tkinter as tk
from tkinter import filedialog
from organizer import organize_files

def select_folder():

    folder = filedialog.askdirectory()

    if folder:
        organize_files(folder)
        status.config(text="Files Organized Successfully")

root = tk.Tk()
root.title("Smart File Organizer")
root.geometry("400x200")

btn = tk.Button(root, text="Select Folder", command=select_folder)
btn.pack(pady=20)

status = tk.Label(root, text="")
status.pack()

root.mainloop()