# I LOVE GURA
# I LOVE GURA
# I LOVE GURA

import requests, re, json, zippyshare_downloader as zippy
from pytube import YouTube as yt
from hurry.filesize import size, alternative
from bs4 import BeautifulSoup as bs
from urllib.parse import unquote

author = "Sandy Sayang Gawr Gura"
log = {
    "invalid_url" : {
        "author" : author,
        "status" : 406,
        "message" : "Invalid URL!"
    },
    "exception" : {
        "author" : author,
        "status" : 500,
        "message" : "Whoops! Something wrong!"
    }
}

def TinyURL(url) -> dict:
    """
    URL shortener using TinyURL
    """
    if not re.search(r"http[s]\:\/\/", url):
        return log["invalid_url"]
    try:
        data = requests.get("https://tinyurl.com/api-create.php", params={ "url" : url }).text
        return {
            "author" : author,
            "status" : 200,
            "url" : data
        }
    except Exception as e:
        raise e

def YouTube(url) -> dict:
    if not re.search("youtu.be|youtube.com", url):
        return log["invalid_url"]
    try:
        data = yt(url)
        raw = data.vid_info
        resAudio = raw["streamingData"]["adaptiveFormats"]
        resAudio = [a for a in resAudio if a["itag"] == 140][0]
        resVideo = raw["streamingData"]["formats"]
        resVideo = [b for b in resVideo if b["itag"] == 22][0]
        results = {
            "author" : author,
            "status" : 200,
            "title" : data.title,
            "description" : data.description,
            "thumbnail" : data.thumbnail_url,
            "audio" : {
                "url" : resAudio["url"],
                "size" : size(data.streams.get_by_itag(140).filesize, system=alternative),
                "mimeType" : resAudio["mimeType"]
            },
            "video" : {
                "url" : resVideo["url"],
                "size" : size(data.streams.get_by_itag(22).filesize, system=alternative),
                "mimeType" : resVideo["mimeType"]
            }
        }
        return results
    except Exception as e:
        raise e

def Zippyshare(url) -> dict:
    if not re.search("zippyshare", url):
        return log["invalid_url"]
    try:
        base = zippy.get_info(url)
        if not base["download_url"]:
            return {"detail":"URL not found!"}
        results = {
            "author" : author,
            "status" : 200,
            "title" : base["name_file"],
            "size" : base["size"],
            "date_upload" : base["date_upload"],
            "url" : base["download_url"]
        }
        return results
    except Exception as e:
        raise e
        
# I LOVE GURA
# I LOVE GURA
# I LOVE GURA