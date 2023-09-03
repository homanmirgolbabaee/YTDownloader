import tldextract
from pytube import YouTube, exceptions as pytube_exceptions
import streamlit as st

st.title("Youtube Video Downloader")
st.subheader("Enter the URL:")
url = st.text_input(label='URL')

try:
    yt = YouTube(url)
except pytube_exceptions.RegexMatchError:
    st.subheader("Invalid YouTube URL. Please enter a valid URL.")

if url != '':
    st.image(yt.thumbnail_url, width=300)
    st.subheader('''
    {}
    ## Length: {} seconds
    ## Rating: {} 
    '''.format(yt.title, yt.length, yt.rating))
    video = yt.streams
    if len(video) > 0:
        downloaded, download_audio = False, False
        download_video = st.button("Download Video")
        if yt.streams.filter(only_audio=True):
            download_audio = st.button("Download Audio Only")
        if download_video:
            video.get_lowest_resolution().download()
            downloaded = True
        if download_audio:
            video.filter(only_audio=True).first().download()
            downloaded = True
        if downloaded:
            st.subheader("Download Complete")
    else:
        st.subheader("Sorry, this video can not be downloaded")
