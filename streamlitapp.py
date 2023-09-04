from pytube import YouTube, exceptions as pytube_exceptions
import streamlit as st

# UI Header
st.title("YouTube Video Downloader")
st.write("This application allows you to download YouTube videos and audio.")

# URL input
st.subheader("Step 1: Enter the YouTube Video URL")
url = st.text_input("YouTube URL", "")

# Initialize variables
yt = None
video = None

# URL validation and video information
try:
    if url:
        yt = YouTube(url)
        st.subheader("Step 2: Video Information")
        
        # Display video details and thumbnail
        col1, col2 = st.columns(2)
        with col1:
            st.image(yt.thumbnail_url, width=300)
        with col2:
            st.write(f"**Title:** {yt.title}")
            st.write(f"**Length:** {yt.length} seconds")
            st.write(f"**Rating:** {yt.rating}")
            
        video = yt.streams
except pytube_exceptions.RegexMatchError:
    st.error("Invalid YouTube URL. Please enter a valid URL.")

# Download options
if video and len(video) > 0:
    st.subheader("Step 3: Download Options")
    
    # Select format
    stream_options = ["Video", "Audio Only"]
    selected_option = st.selectbox("Select Format", stream_options)
    
    # Download button
    if st.button("Download"):
        with st.spinner("Downloading..."):
            if selected_option == "Video":
                video.get_lowest_resolution().download()
            else:
                video.filter(only_audio=True).first().download()
        
        st.success("Download Complete 🎉")
else:
    if url:
        st.warning("Sorry, this video cannot be downloaded.")
