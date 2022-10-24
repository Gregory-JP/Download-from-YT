#!/usr/bin/env python
# coding: utf-8

# In[4]:


from pytube import YouTube


# In[8]:


def music_download(link):
    music = YouTube(link)
    stream = music.streams.get_audio_only()
    stream.download()


# In[9]:


music_download('link aqui')


# In[10]:


def video_download(link):
    video = YouTube(link)
    stream = video.streams.get_highest_resolution()
    stream.download()


# In[ ]:


video_download('link aqui')

