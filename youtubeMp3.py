from youtubesearchpython import VideosSearch
import json
import youtube_dl
import os

os.chdir('') #give specific location u need


def youtube(name, link):
    video_info = youtube_dl.YoutubeDL().extract_info(url = link,download=False)
    filename = f"{video_info['title']}"
    options={
        'format':'bestaudio/best',
        'keepvideo':False,
        'outtmpl':filename,
    }
    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])

    return filename


file1 = open('export.txt', 'r',encoding='utf8')
count = 0
error = []

for line in file1:
    count += 1
    name = line.strip()
    videosSearch = VideosSearch(f'{name}', limit = 2)
    feed = json.dumps(videosSearch.result())
    search = json.loads(feed)
    try:
        link = search["result"][0]["link"]
    except IndexError:
        pass
    try:
        filename = youtube(name, link)
    except youtube_dl.utils.DownloadError:
        error.append(name)
        os.remove(filename)
        print(count)
        pass
    print(count, name, f"\t Download Complete {name} ----> {filename}" )
file1.close()


