from os import link
from turtle import title
from django.shortcuts import render
from pytube import Playlist, YouTube
from time import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from .models import HomeModel
import time
# Create your views here.

def home(request):
    playlist_links = Playlist('https://www.youtube.com/playlist?list=PL3oW2tjiIxvQ1BZS58qtot3-p-lD32oWT')
    # start = time()

    def get_video_title_link(link):
        title = YouTube(link).title
        vid_id = YouTube(link).video_id
        return (title, vid_id)

    processes = []
    with ThreadPoolExecutor(max_workers=10) as executor:
        for url in playlist_links:
            processes.append(executor.submit(get_video_title_link, url))

    audio_title_link = []
    for task in as_completed(processes):
        audio_title_link.append(task.result())
        print(task.result())

    for audio, link in audio_title_link:
        
        HomeModel.objects.create(
            title = audio,
            audio_id = link
        )
        time.sleep(1)

    objs = HomeModel.objects.all()[:51]

    # print(f'Time taken: {time() - start}')
    context_data = {
        'objs': objs
    }
    return render(request, 'index.html', context_data)


def download_page(request):

    return render(request, 'download_page.html')

