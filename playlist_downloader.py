import pytube as py

def download_playlist(link, download_audio=True):
    """
    param link: link of the playlist that will be downloaded
    param download_audio: is True by default, only the audio will be downloaded, use False for download videos instead
    
    """
    
    links = py.Playlist(link)
    downloads = 0
    
    if download_audio:
        for link in links:
            try:
                music = py.YouTube(link)
                stream = music.streams.get_audio_only()
                stream.download()
                downloads += 1
            except KeyError:
                print(f"Video {link} couldn't be downloaded")
        
        print(f"{len(links)} musics found, {downloads} were downloaded")
        return True
            
    elif download_audio == False:
        for link in links:
            try:
                video = py.YouTube(link)
                stream = video.streams.get_highest_resolution()
                stream.download()
                download += 1
            except KeyError:
                print(f"Video {link} couldn't be downloaded")
        
        print(f"{len(links)} videos found, {downloads} were downloaded")
        return True


# download only the audios
download_playlist('link of the playlist')

# download the videos
download_playlist('link of the playlist', download_audio=False)
