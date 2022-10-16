#################### Information
##
## Semua config APPs subcommand.
## 
## => Support: https://trakteer.id/arzhavz/tip
## => My website: https://arzxh.deta.sh
## => @Sandy Pratama
##
####################

import typer, os
from requests import *
from pathlib import Path

########## YTDL Section ##########
"""

YouTube downloader menggunakan library Pytube. 
Kamu juga bisa mengeditnya di /lib/youtube.py.

"""
from lib.youtube import yt

YTDL = typer.Typer()


@YTDL.command()
def audio(url: str):
	"""
	Download your favorite Audio in YouTube
	"""
	try: 
		os.chdir(Path(Path(__file__).parent.parent, "tmp"))
		yt(url, "audio")
		return
	except Exception as e:
		raise e
		
@YTDL.command()
def video(url: str):
	"""
	Download your favorite Video in YouTube
	"""
	try: 
		os.chdir(Path(Path(__file__).parent.parent, "tmp"))
		yt(url, "video")
		return
	except Exception as e:
		raise e
########## End Section ##########

########## IGDL Section ##########
"""

Instagram helper mengikis dari https://downloadgram.org.
Kamu juga bisa mengeditnya di /lib/instagram.py

"""
from lib.instagram import Instagram

IGDL = typer.Typer()


@IGDL.command()
def photo(url: str):
	"""
	Download your favorite Instagram photos
	"""
	try: 
		os.chdir(Path(Path(__file__).parent.parent, "tmp"))
		Instagram.Photo(url)
		return
	except Exception as e:
		raise e
		
@IGDL.command()
def reel(url: str):
	"""
	Download your favorite Instagram reels
	"""
	try: 
		os.chdir(Path(Path(__file__).parent.parent, "tmp"))
		Instagram.Reel(url)
		return
	except Exception as e:
		raise e
		
@IGDL.command()
def igtv(url: str):
	"""
	Download your favorite Instagram videos
	"""
	try: 
		os.chdir(Path(Path(__file__).parent.parent, "tmp"))
		Instagram.IGTV(url)
		return
	except Exception as e:
		raise e
		
########## End Section ##########
