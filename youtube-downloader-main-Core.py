import streamlit as st
from pytube import YouTube

def main():
    st.title("YouTube Video Downloader")
    st.write("Enter the YouTube video URL below:")
   
    video_url = st.text_input("Video URL:")
    
    if st.button("Download"):
        try:
            yt = YouTube(video_url)
            st.write("Title:", yt.title)
            st.write("Length:", yt.length)
           
            stream = yt.streams.get_highest_resolution()
           
            st.write("Downloading...")
            stream.download(output_path='downloads')  # Change the output path if needed
            st.success("Download complete!")
        except Exception as e:
            st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    st.set_page_config(page_title="YouTube Downloader")

    main()
