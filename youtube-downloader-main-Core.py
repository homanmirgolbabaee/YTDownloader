import streamlit as st

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

        st.subheader("You clicked the Download button!")
        st.write(f"Video URL: {video_url}")

if __name__ == "__main__":
    main()
