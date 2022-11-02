from pytube import YouTube

# download only the audio of the video
def audio_download(link):
    audio = YouTube(link)
    stream = audio.streams.get_audio_only()
    stream.download()

# download the video with the audio
def video_download(link):
    video = YouTube(link)
    stream = video.streams.get_highest_resolution()
    stream.download()

audio_download('link aqui')

video_download('link aqui')
