import instaloader
import tkinter as tk
from tkinter import messagebox, simpledialog
import os
import threading

def get_credentials():
    username = simpledialog.askstring("Instagram Username", "Enter your Instagram username:")
    password = simpledialog.askstring("Instagram Password", "Enter your Instagram password:", show="*")
    return username, password

def download_posts(loader, profile, status_listbox):
    os.makedirs(profile.username, exist_ok=True)
    for post in profile.get_posts():
        loader.download_post(post, target=profile.username)
        status_listbox.insert(tk.END, f"Downloading post {post.shortcode}")
        status_listbox.yview(tk.END)
        status_listbox.update_idletasks()

def login_and_download(status_listbox):
    target_profile = entry_profile.get()
    window.after(0, handle_login, target_profile, status_listbox)

def handle_login(target_profile, status_listbox):
    username, password = get_credentials()
    try:
        loader.login(username, password)
        messagebox.showinfo("Login", "Login successful!")
        window.quit()
        start_download(target_profile, status_listbox)
    except instaloader.exceptions.BadCredentialsException:
        messagebox.showerror("Error", "Invalid Instagram username or password.")
        return
    except instaloader.exceptions.TwoFactorAuthRequiredException:
        messagebox.showerror("Error", "Two-factor authentication is required.")
        return
    except instaloader.exceptions.InvalidArgumentException:
        messagebox.showerror("Error", "Invalid argument provided.")
        return

def start_download(target_profile, status_listbox):
    try:
        profile = instaloader.Profile.from_username(loader.context, target_profile)
        download_posts(loader, profile, status_listbox)
        messagebox.showinfo("Success", f"All posts downloaded successfully from {target_profile}")
    except instaloader.exceptions.ProfileNotExistsException:
        messagebox.showerror("Error", f"The profile '{target_profile}' does not exist.")
    except instaloader.exceptions.PrivateProfileNotFollowedException:
        messagebox.showerror("Error", f"The profile '{target_profile}' is private and requires following.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def start_download_thread(status_listbox):
    threading.Thread(target=login_and_download, args=(status_listbox,), daemon=True).start()

def create_gui():
    global loader, entry_profile, window

    loader = instaloader.Instaloader()

    window = tk.Tk()
    window.title("Instagram Posts Downloader")
    window.geometry("600x400")

    label_title = tk.Label(window, text="Instagram Posts Downloader", font=("Helvetica", 16))
    label_title.pack(pady=20)

    label_profile = tk.Label(window, text="Enter Instagram username to download posts from:")
    label_profile.pack(pady=5)

    entry_profile = tk.Entry(window, font=("Helvetica", 14))
    entry_profile.pack(pady=5)

    download_button = tk.Button(window, text="Start Download", font=("Helvetica", 14), command=lambda: start_download_thread(status_listbox))
    download_button.pack(pady=20)

    status_label = tk.Label(window, text="Download Status:")
    status_label.pack(pady=5)

    status_listbox = tk.Listbox(window, width=50, height=10)
    status_listbox.pack(pady=10)

    window.mainloop()

if __name__ == "__main__":
    create_gui()
