from pytube import Channel, YouTube
from datetime import datetime, timedelta
import os

DOWNLOADS = '/Users/timmackenzie/Downloads'


def strip_url(url):
    return url.replace('https://youtube.com/watch?v=', '')

def download(watch_url):
    video = YouTube(watch_url, use_oauth=True)
    output_folder = f'{DOWNLOADS}/{video.title}/'
    if not os.path.isdir(output_folder):
        os.mkdir(output_folder)
    print("Downloading...")
    ystream = video.streams.get_highest_resolution()
    ystream.download(output_folder)
    if 'en' in video.captions:
        caption = video.captions['en']
        subs = str(caption.generate_srt_captions())
        filename = f'{output_folder}/{video.title}.srt'
        with open(filename, 'w') as f:
            f.write(subs)
    elif 'a.en' in video.captions:
        caption = video.captions['a.en']
        subs = str(caption.generate_srt_captions())
        filename = f'{output_folder}/{video.title}.srt'
        with open(filename, 'w') as f:
            f.write(subs)
    print("Download Complete.")

output_path = '/Users/timmackenzie/Downloads/'
channels = [
            'https://www.youtube.com/c/LinusTechTips',
            'https://www.youtube.com/channel/UCi8C7TNs2ohrc6hnRQ5Sn2w/videos',
            'https://www.youtube.com/c/RyanGeorge',
            'https://www.youtube.com/user/LastWeekTonight/videos',
            'https://www.youtube.com/c/Exil22/videos',
            'https://www.youtube.com/c/NicolaiLol/videos',
            'https://www.youtube.com/channel/UC9Kq-yEt1iYsbUzNOoIRK0g/videos',
            'https://www.youtube.com/c/TechWithTim/videos',
            'https://www.youtube.com/c/djslopesroom/videos',
            'https://www.youtube.com/c/larry/videos',
            'https://www.youtube.com/channel/UCQMyhrt92_8XM0KgZH6VnRg/videos',
            'https://www.youtube.com/c/MarkRober/videos'
            ]

all_channels = []

for channel in channels:
    c = Channel(channel)
    for video in c.videos:
        video_date = video.publish_date
        hash = strip_url(video.watch_url)
        if channel not in all_channels:
            if video_date > datetime.now() - timedelta(1):
                print(f'new video today on {video.author}! {video.title}')
                download(video.watch_url)
            if video_date < datetime.now() - timedelta(1):
                print(f'finished checking for new videos on {video.author}.')
                break
        else:
            print(f'new video today on {video.author}! {video.title}')
            download(video.watch_url)
