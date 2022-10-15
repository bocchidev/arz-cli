#################### Information
##
## Instagram Downloader.
#3 Mengikis dari https://downloadgram.org.
## Semua file unduhan akan disimpan di folder /tmp.
##
## Script ini saya tulis serapi mungkin
## Agar semua orang bisa mengembangkannya.
## 
## => Support: https://trakteer.id/arzhavz/tip
## => My website: https://arzxh.deta.sh
## => @Sandy Pratama
##
####################


import os, shutil
from tqdm.auto import tqdm
from bs4 import BeautifulSoup as bs
from requests import *
from pathlib import Path
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


class Instagram:
	
	def Reel(url) -> dict:
		load = {"url": url}
		try:
			title = url.split("reel/")[1] 
			title = title.split("/")[0] # Mengambil id post
			data = post("https://downloadgram.org/reel-downloader.php#downloadhere", data=load)
			html = bs(data.text, "html.parser")
			video = html.find("video")
			if not video:
				pass
			else:
				try:
					os.mkdir(title)
				except:
					pass
				source = video.find("source").get("src")
				os.chdir(Path(Path(__file__).parent.parent, f"tmp/{title}"))
				with get(source, stream=True) as r:
					total_length = int(r.headers.get("Content-Length"))
					with tqdm.wrapattr(r.raw, "read", total=total_length, desc="") as raw:
						with open(f"{title}.mp4", 'wb') as output:
							shutil.copyfileobj(raw, output)
				os.chdir(Path(Path(__file__).parent.parent, "tmp"))
				open("log.txt", "a").write(LOG_MESSAGE.format(title, str(total_length), NOW, "MP4"))
				print("\nUnduhan selesai! Video tersimpan di:\n", Path(Path(__file__).parent.parent, f"tmp/{title}"))
			return 
		except Exception as e:
			raise e
			
	def Photo(url) -> dict:
		load = {"url": url}
		try:
			title = url.split("p/")[1] 
			title = title.split("/")[0] # Mengambil id post
			data = post("https://downloadgram.org/photo-downloader.php#downloadhere", data=load)
			html = bs(data.text, "html.parser")
			downloadhere = html.find("div", {"id": "downloadhere"})
			if not downloadhere:
				pass
			else:	
				href = downloadhere.find_all("a")
				try:
					os.mkdir(title)
				except:
					pass
				for i in range(len(href)):
					os.chdir(Path(Path(__file__).parent.parent, f"tmp/{title}"))
					with get(href[i].get("href"), stream=True) as r:
						total_length = int(r.headers.get("Content-Length"))
						with tqdm.wrapattr(r.raw, "read", total=total_length, desc="") as raw:
							with open(title + "_" + str(i) + ".jpg", 'wb') as output:
								shutil.copyfileobj(raw, output)
					os.chdir(Path(Path(__file__).parent.parent, "tmp"))
					open("log.txt", "a").write(LOG_MESSAGE.format(title, str(total_length), NOW, "JPG"))
				print("\nUnduhan selesai! Gambar tersimpan di:\n", Path(Path(__file__).parent.parent, f"tmp/{title}"))
			return 
		except Exception as e:
			raise e
			
	def IGTV(url) -> dict:
		load = {"url": url}
		try:
			title = url.split("tv/")[1] 
			title = title.split("/")[0] # Mengambil id post
			data = post("https://downloadgram.org/igtv-downloader.php#downloadhere", data=load)
			html = bs(data.text, "html.parser")
			video = html.find("video")
			if not video:
				pass
			else:
				try:
					os.mkdir(title)
				except:
					pass
				source = video.find("source").get("src")
				os.chdir(Path(Path(__file__).parent.parent, f"tmp/{title}"))
				with get(source, stream=True) as r:
					total_length = int(r.headers.get("Content-Length"))
					with tqdm.wrapattr(r.raw, "read", total=total_length, desc="") as raw:
						with open(f"{title}.mp4", 'wb') as output:
							shutil.copyfileobj(raw, output)
				os.chdir(Path(Path(__file__).parent.parent, "tmp"))
				open("log.txt", "a").write(LOG_MESSAGE.format(title, str(total_length), NOW, "MP4"))
				print("\nUnduhan selesai! Video tersimpan di:\n", Path(Path(__file__).parent.parent, f"tmp/{title}"))
			return 
		except Exception as e:
			raise e