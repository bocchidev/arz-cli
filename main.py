import re, requests, json, random
from typing import Optional
from lib.api import YouTube as YT
from fastapi import FastAPI, APIRouter, HTTPException, Request

APP = FastAPI(title="Free APIs for human",
              version="0.1.0",
              openapi_url="/openapi.json")
ROUTER = APIRouter()

@ROUTER.get("/", status_code=200)
def root(request: Request) -> dict:
    return {"detail":"For tutorials, visit  https://facebook.com/arzhavz"}

@ROUTER.get("/youtube", status_code=200)
def YouTube(url: Optional[str] = None) -> dict:
    if not url or not re.findall("youtu.be|youtube.com/watch", url):
        raise HTTPException(status_code=404, detail="Invalid url!")
    return YT(url)

@ROUTER.get("/{page}", status_code=200)
def validate():
    return {"detail":"page not found"}

APP.include_router(ROUTER)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(APP, host="127.0.0.1", port=2006)