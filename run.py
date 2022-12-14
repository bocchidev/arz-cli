#################### Information
##
## Selamat datang di ARZ-CLI
## Ini adalah program sederhana yang akan membantu kamu
## Harap teliti saat mengedit agar tidak terjadi error
## Terimakasih telah berkunjung
## 
## => Support: https://trakteer.id/arzhavz/tip
## => My website: https://arzxh.deta.dev
## => @Sandy Pratama
##
####################

import typer
from config.apps import YTDL, IGDL
from lib.mediafire import Mediafire
from lib.zippyshare import Zippyshare

APP = typer.Typer(pretty_exceptions_enable=False)

########## Commands Section ##########
@APP.command()
def mediafire(url: str):
	"""
	Mediafire downloader.
	"""
	Mediafire(url)
	
@APP.command()
def zippyshare(url: str):
	"""
	Zippyshare downloader.
	"""
	Zippyshare(url)
######################################

APP.add_typer(YTDL, name="ytdl", help="YouTube downloader")
APP.add_typer(IGDL, name="igdl", help="Instagram downloader")
		
if __name__ == "__main__":
	APP()