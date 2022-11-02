from pytube import YouTube

def music_download(link):
    music = YouTube(link)
    stream = music.streams.get_audio_only()
    stream.download()
    
def video_download(link):
    video = YouTube(link)
    stream = video.streams.get_highest_resolution()
    stream.download()

music_download('link aqui')

video_download('link aqui')
