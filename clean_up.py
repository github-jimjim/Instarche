import os
import tkinter as tk
from tkinter import filedialog, messagebox

def delete_files_in_directory(directory):
    allowed_extensions = {'.jpg', '.png', '.mp3', '.mp4'}

    try:
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)

            if os.path.isfile(file_path):
                file_extension = os.path.splitext(filename)[1].lower()

                if file_extension not in allowed_extensions:
                    os.remove(file_path)
                    print(f"Deleting: {file_path}")
        
        messagebox.showinfo("Success", "Succesfully cleaned up.")
    
    except Exception as e:
        messagebox.showerror("Error", f"A error occured while cleaning up: {e}")

def choose_folder():
    folder_selected = filedialog.askdirectory()

    if folder_selected:
        delete_files_in_directory(folder_selected)

root = tk.Tk()
root.withdraw()

choose_folder()
