import tkinter as tk
from tkinter import messagebox
from pytube import YouTube

def download_video(url, output_path='.'):
    try:
        yt = YouTube(url)
        video_stream = yt.streams.get_highest_resolution()
        video_stream.download(output_path)
        messagebox.showinfo("Download Complete", "Download completed!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def get_url():
    url = url_entry.get()
    download_video(url)
    url_entry.delete(0, tk.END)  # Clear the entry field after downloading

root = tk.Tk()
root.title("YouTube Video Downloader")

url_label = tk.Label(root, text="Enter YouTube Video URL:")
url_label.pack()

url_entry = tk.Entry(root, width=40)
url_entry.pack()

download_button = tk.Button(root, text="Download", command=get_url)
download_button.pack()

root.mainloop()
