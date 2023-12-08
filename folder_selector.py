from tkinter import filedialog
from tkinter import Tk
import os

def select_folder():
    root = Tk()
    root.withdraw()  # Ocultar la ventana principal de Tkinter
    folder_selected = filedialog.askdirectory()
    root.destroy()
    return folder_selected

if __name__ == '__main__':
    folder_path = select_folder()
    if folder_path:
        with open('download_path.txt', 'w') as file:
            file.write(folder_path)
