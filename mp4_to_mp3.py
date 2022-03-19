import os 
from moviepy.editor import *
os.chdir('D:/Projects/Python/Spotify/music-currpted')

def rename():
    directory = os.listdir('D:/Projects/Python/Spotify/music-currpted')

    for file in directory:
        name = file[:-4]+".mp4"
        print(name)
        os.rename(file, name)
        
def convert():
    directory = os.listdir('D:/Projects/Python/Spotify/music-currpted')
    directory.remove('mp3')
    if not os.path.exists('mp3'):
        os.makedirs('mp3')
    for file in directory:
        mp3_file = file[:-4] + ".mp3"
        print(file,"-->", mp3_file)
        clip = AudioFileClip(f'{file}')
        clip.write_audiofile(f'mp3/{mp3_file}')
        clip.close()
convert()