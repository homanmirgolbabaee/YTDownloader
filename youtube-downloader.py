import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from pytube import YouTube
from threading import Thread

class YouTubeDownloaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube Video Downloader")
        self.root.geometry("400x300")

        self.create_widgets()

    def create_widgets(self):
        title_label = tk.Label(
            self.root, text="Welcome to YouTube Video Downloader", font=("Helvetica", 16)
        )
        title_label.pack(pady=15)

        self.url_entry = tk.Entry(self.root, width=40, font=("Helvetica", 12))
        self.url_entry.pack()

        self.download_button = tk.Button(
            self.root,
            text="Download Video",
            command=self.start_download_thread,
            bg="#FF5733",
            fg="white",
            font=("Helvetica", 12, "bold"),
            relief=tk.FLAT,
        )
        self.download_button.pack(pady=10)

        self.progress_bar = ttk.Progressbar(
            self.root,
            orient="horizontal",
            length=300,
            mode="determinate",
            value=0,
            maximum=100,
        )

    def start_download_thread(self):
        self.download_button.config(state=tk.DISABLED)
        self.progress_bar.pack(pady=10)
        
        url = self.url_entry.get()
        if url:
            self.download_thread = Thread(target=self.download_video, args=(url,))
            self.download_thread.start()
        else:
            messagebox.showwarning("Warning", "Please enter a valid YouTube URL")
            self.download_button.config(state=tk.NORMAL)
        
    def update_progress_bar(self, stream, chunk, bytes_remaining):
        total_size = stream.filesize
        downloaded_size = total_size - bytes_remaining
        progress = int((downloaded_size / total_size) * 100)
        self.progress_bar["value"] = progress
        self.root.update_idletasks()

    def download_video(self, url):
        try:
            yt = YouTube(url)
            video_stream = yt.streams.get_highest_resolution()
            
            self.show_loading_animation()  # Call the loading animation function

            video_stream.download(output_path="downloads/")
            messagebox.showinfo("Download Complete", "Download completed!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

        self.progress_bar.pack_forget()
        self.download_button.config(state=tk.NORMAL)

    def show_loading_animation(self):
        loading_label = tk.Label(self.root, text="Downloading...")
        loading_label.pack()

        def update_progress():
            current_value = self.progress_bar["value"]
            if current_value < 100:
                self.progress_bar["value"] = current_value + 10
                self.root.after(1000, update_progress)
            else:
                loading_label.config(text="Download Complete!")

        update_progress()

def main():
    root = tk.Tk()
    app = YouTubeDownloaderApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
