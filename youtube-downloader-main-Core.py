import streamlit as st
from pytube import YouTube
import time

# Set Streamlit page configuration
st.set_page_config(page_title="Mokhlese Mehdi's Youtube Video Downloader", page_icon="🎥")

def main():
    st.title("Mokhlese Mehdi's Youtube Video Downloader")
    st.markdown("Download YouTube videos easily! 🎬 by HOMAN 🧑‍💻")
    st.write("")

    # Get the video URL from user input
    video_url = st.text_input("Enter the YouTube video URL:", help="Paste the URL here")

    if st.button("Download"):
        if not video_url:
            st.warning("Please enter a YouTube video URL. 🙄")
            return

        try:
            yt = YouTube(video_url)
            st.subheader("Video Information")
            st.write(f"**Title:** {yt.title}")
            st.write(f"**Duration:** {yt.length} seconds")

            # Choose the highest resolution stream
            stream = yt.streams.get_highest_resolution()

            # Display video thumbnail with improved styling
            thumbnail_html = f"""
            <div style="
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                max-width: 200px;
                border: 1px solid #ccc;
                border-radius: 10px;
                padding: 10px;
                box-shadow: 0px 2px 8px rgba(0, 0, 0, 0.2);
            ">
                <img src="{yt.thumbnail_url}" alt="Video Thumbnail" style="width: 100%; border-radius: 10px;">
                <p style="font-weight: bold; margin-top: 10px;">{yt.title} 📽️</p>
            </div>
            """
            st.markdown(thumbnail_html, unsafe_allow_html=True)

            # Download the video
            with st.spinner("Downloading... ⏳"):
                stream.download(output_path='downloads')  # Change the output path if needed
                time.sleep(2)  # Simulate a delay
            st.success("Download complete! ✅")
        except Exception as e:
            st.error(f"An error occurred: {e} ❌")

if __name__ == "__main__":
    main()
