# arz-cli
Program berbasis CLI yang memiliki beberapa fitur keren.
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
Untuk detail bisa gunakan perintah berikut:
```sh
python run.py --help
```

Semua file unduhan akan berada di folder /tmp.
Kamu juga bisa memeriksa log unduhan kamu di /tmp/log.txt
