# arz-cli
Program sederhana yang mengijinkanmu mengunduh dari Instagram dan YouTube.

# Tutorial termux:
Update termux menggunakan:
```sh
apt-get update -y
```
Lalu upgrade semua package:
```sh
apt-get upgrade -y
```
Kemudian install package yang diperlukan (termasuk menyalin repo ini):
```sh
apt-get install git ffmpeg python -y && git clone https://github.com/KurniawanIDX/arz-cli && cd arz-cli
```
Jika sudah, install pip package:
```sh
python -m pip install -r requirements.txt --upgrade
```

# Tutorial Windows
Untuk di Windows:
Install FFmpeg, CMDer, dan Python dahulu.
Atau kalian bisa mengunduh MSYS2 (Aku menggunakan ini).
Setelah itu, paste perintah berikut:
```sh
git clone https://github.com/KurniawanIDX/arz-cli && cd arz-cli && python -m pip install -r requirements.txt --upgrade
```

# Penggunaan
Untuk mengunduh audio YouTube:
```sh
python run.py ytdl audio https://youtube.com/
```
Untuk mengunduh video YouTube:
```sh
python run.py ytdl video https://youtube.com/
```
Untuk mengunduh video Instagram:
```sh
python run.py igdl igtv https://instagram.com/
```
Untuk mengunduh reel Instagram:
```sh
python run.py igdl reel https://instagram.com/
```
Untuk mengunduh foto Instagram:
```sh
python run.py igdl photo https://instagram.com/
```

Semua file unduhan akan berada di folder /tmp.
Kamu juga bisa memeriksa log unduhan kamu di /tmp/log.txt
