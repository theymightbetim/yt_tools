import os.path
from pytube import YouTube
from sys import argv

base_link = "https://www.youtube.com/watch?v="

if argv[1] == 'help':
    print('''
    video_downloader.py <youtube link>
    
    downloads the youtube link
    ''')
    quit()

link = base_link + argv[1]
yt = YouTube(link, use_oauth=True)
DOWNLOADS = '/Users/timmackenzie/Downloads'
print("Title: ", yt.title)

run= True
while run == True:
    dl = input("(D)ownload/(I)nfo: ")
    if dl.lower() == 'd':
        output_folder = f'{DOWNLOADS}/{str(yt.title).replace("/", "")}/'
        if not os.path.isdir(output_folder):
            os.mkdir(output_folder)
        print("Downloading...")
        ystream = yt.streams.get_highest_resolution()
        ystream.download(output_folder)
        if 'en' in yt.captions:
            caption = yt.captions['en']
            subs = str(caption.generate_srt_captions())
            filename = f'{output_folder}/{yt.title}.srt'
            with open(filename, 'w') as f:
                f.write(subs)
        elif 'a.en' in yt.captions:
            caption = yt.captions['a.en']
            subs = str(caption.generate_srt_captions())
            filename = f'{output_folder}/{yt.title}.srt'
            with open(filename, 'w') as f:
                f.write(subs)
        print("Download Complete.")
    if dl.lower() == 'i':
        print("Author: ", yt.author)
        print("Channel ID: ", yt.channel_id)
        print("Published: ", yt.publish_date)
        print("Views: ", yt.views)
        print("Description: ", yt.description)
    else:
        run = False




