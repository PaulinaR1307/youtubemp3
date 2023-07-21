from pytube import YouTube
import os

yt = YouTube(input("Enter the URL of the video: \n>>"))

video = yt.streams.filter(only_audio=True).first()

destination = "/Users/LENOVO/Desktop/DESCARGAR LINK YOUTUBE PYTHON/DESCARGAS"

out_file = video.download(output_path=destination)

base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'
os.rename(out_file, new_file)

print(yt.title + " has been successfully downloaded")