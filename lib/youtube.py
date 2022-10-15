#################### Information
##
## YouTube Downloader.
## Semua file unduhan akan disimpan di folder /tmp.
## Khusus untuk audio, menggunakan software ffmpeg
## Harap install ffmpeg dahulu di https://ffmpeg.org
##
## Script ini saya tulis serapi mungkin
## Agar semua orang bisa mengembangkannya.
## 
## => Support: https://trakteer.id/arzhavz/tip
## => My website: https://arzxh.deta.sh
## => @Sandy Pratama
##
####################

import re, os
from urllib.parse import quote, unquote
from pytube.cli import on_progress
from pytube import YouTube
from datetime import datetime

NOW = str(datetime.now())

LOG_MESSAGE = """
#################### History ####################
##												   
## => Name: {}
## => Size: {}
## => Date: {}
## => Type: {}
## 
## => Support: https://trakteer.id/arzhavz/tip
## => My website: https://arzxh.deta.sh
## => @Sandy Pratama
##
#################################################
"""


def yt(url: str, ext: str):
	if not re.search(r"http[s]\:\/\/", url):
		return "Invalid URL"
	try:
		data = YouTube(url, on_progress_callback=on_progress)
		if ext.lower() == "audio":
			streams = data.streams.get_by_itag(22)
			file = streams.download()
			filename = file.split("tmp/")[1] # mengambil nama file, karena ini adalah path
			title, extension = os.path.splitext(filename)
			encoded_title = quote(title)
			os.rename(filename, f"{encoded_title}.mp4") # mengubah nama file, agar tidak terjadi error
			os.system(f"ffmpeg -i {encoded_title}.mp4 {encoded_title}.mp3")
			os.rename(f"{encoded_title}.mp3", f"{unquote(encoded_title)}.mp3")
			os.unlink(f"{encoded_title}.mp4") # menghapus file awal
			open("log.txt", "a").write(LOG_MESSAGE.format(title, str(streams.filesize), NOW, "MP3"))
			print("\n", LOG_MESSAGE.format(title, str(streams.filesize), NOW, "MP3"), "\nSaved at /tmp folder")
		elif ext.lower() == "video":
			streams = data.streams.get_by_itag(22)
			file = streams.download()
			filename = file.split("tmp/")[1] # mengambil nama file, karena ini adalah path
			title, extension = os.path.splitext(filename)
			open("log.txt", "a").write(LOG_MESSAGE.format(title, str(streams.filesize), NOW, "MP4"))
			print("\n", LOG_MESSAGE.format(title, str(streams.filesize), NOW, "MP4"), "\nSaved at /tmp folder")
		else:
			return "Invalid extension!"
	except Exception as e:
		raise e
