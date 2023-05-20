from pytube import YouTube
# Paste the URL of the YouTube video you want to download
video_url = input("Enter the YouTube video URL: ")

# Create a YouTube object
yt = YouTube(video_url)

# Get the highest resolution video stream
stream = yt.streams.get_highest_resolution()

# Download the video
stream.download()

print("Video downloaded successfully!")