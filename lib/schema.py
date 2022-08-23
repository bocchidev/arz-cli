from pydantic import BaseModel, HttpUrl
from typing import Dict

class res_url(BaseModel):
    url: HttpUrl
    size: str
    mimeType: str

class yt_schema(BaseModel):
    author: str
    status: int
    title: str
    description: str
    thumbnail: HttpUrl
    audio: res_url 
    video: res_url
    
    class Config:
        schema_extra = {
            "example" : {
                "author" : "Sandy Sayang Gawr Gura",
                "status" : 200,
                "title" : "Judul video",
                "description" : "Deskripsi video",
                "thumbnail" : "URL thumbnail video",
                "audio" : {
                    "url" : "URL unduhan",
                    "size" : "Ukuran audio",
                    "mimeType" : "MymeType audio"
                },
                "video" : {
                    "url" : "URL unduhan",
                    "size" : "Ukuran video",
                    "mimeType" : "MymeType video"
                }
            }
        }
        
class zippy_schema(BaseModel):
    author: str
    status: int
    title: str
    size: str
    date_upload: str
    url: HttpUrl
        
    class Config:
        schema_extra = {
            "example" : {
                "author" : "Sandy Sayang Gawr Gura",
                "status" : 200,
                "title" : "Judul file",
                "size" : "Ukuran file",
                "date_upload" : "Waktu upload",
                "url" : "URL unduhan"
            }
        }
