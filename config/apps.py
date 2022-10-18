#################### Information
##
## Semua config APPs subcommand.
## 
## => Support: https://trakteer.id/arzhavz/tip
## => My website: https://arzxh.deta.dev
## => @Sandy Pratama
##
####################

import typer, os
from pathlib import Path

########## YTDL Section ##########
"""

YouTube downloader menggunakan library Pytube. 

"""
from lib.youtube import YouTube

YTDL = typer.Typer()


@YTDL.command()
def audio(url: str):
	"""
	Download your favorite Audio in YouTube
	"""
	try: 
		os.chdir(Path(Path(__file__).parent.parent, "tmp"))
		YouTube(url, "audio")
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
		YouTube(url, "video")
		return
	except Exception as e:
		raise e
########## End Section ##########

########## IGDL Section ##########
"""

Instagram helper mengikis dari https://downloadgram.org.

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