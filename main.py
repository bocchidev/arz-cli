import re
from lib.api import YouTube
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root() -> dict:
    return {"message":"read tutorials on https://facebook.com/sndyarz"}

@app.get("/youtube")
def youtube(url: str) -> dict:
    if not url:
        return {"message":"Invalid URL!"}
    return YouTube(url)

@app.get("/{pages}")
def validate() -> dict:
    return {"message":"page not found!"}

if __name__ == __name__:
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=2006)