#!/usr/bin/env python
# coding: utf-8

# # Download videos and/or audios from playlists on YouTube

# ## Imports

# In[1]:


import pytube as py


# ## Code

# In[19]:


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


# In[ ]:


# download only the audios
download_playlist('https://www.youtube.com/playlist?list=PL2M0f7eTUkTqsiyF87or1zg4MtHZP0A2y')


# In[ ]:


# download the videos
download_playlist('https://www.youtube.com/playlist?list=PL2M0f7eTUkTqsiyF87or1zg4MtHZP0A2y', download_audio=False)


# In[ ]:




