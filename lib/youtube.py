#################### Information
##
## YouTube Downloader.
## Semua file unduhan akan disimpan di folder /tmp.
## Khusus untuk audio, menggunakan software ffmpeg
## Harap install ffmpeg dahulu di https://ffmpeg.org
##
## => Support: https://trakteer.id/arzhavz/tip
## => My website: https://arzxh.deta.dev
## => @Sandy Pratama
##
####################
	

import base64, codecs
magic = 'IyMjIyMjIyMjIyMjIyMjIyMjIyMgSW5mb3JtYXRpb24KIyMKIyMgWW91VHViZSBEb3dubG9hZGVyLgojIyBTZW11YSBmaWxlIHVuZHVoYW4gYWthbiBkaXNpbXBhbiBkaSBmb2xkZXIgL3RtcC4KIyMgS2h1c3VzIHVudHVrIGF1ZGlvLCBtZW5nZ3VuYWthbiBzb2Z0d2FyZSBmZm1wZWcKIyMgSGFyYXAgaW5zdGFsbCBmZm1wZWcgZGFodWx1IGRpIGh0dHBzOi8vZmZtcGVnLm9yZwojIwojIyA9PiBTdXBwb3J0OiBodHRwczovL3RyYWt0ZWVyLmlkL2FyemhhdnovdGlwCiMjID0+IE15IHdlYnNpdGU6IGh0dHBzOi8vYXJ6eGguZGV0YS5kZXYKIyMgPT4gQFNhbmR5IFByYXRhbWEKIyMKIyMjIyMjIyMjIyMjIyMjIyMjIyMKCQoKaW1wb3J0IHJlLCBvcwpmcm9tIHBhdGhsaWIgaW1wb3J0IFBhdGgKZnJvbSB1cmxsaWIucGFyc2UgaW1wb3J0IHF1b3RlLCB1bnF1b3RlCmZyb20gcHl0dWJlLmNsaSBpbXBvcnQgb25fcHJvZ3Jlc3MKZnJvbSBweXR1YmUgaW1wb3J0IFlvdVR1YmUgYXMgWVQKZnJvbSBkYXRldGltZSBpbXBvcnQgZGF0ZXRpbWUKZnJvbSBodXJyeS5maWxlc2l6ZSBpbXBvcnQgc2l6ZSwgYWx0ZXJuYXRpdmUKCk5PVyA9IHN0cihkYXRldGltZS5ub3coKSkKCkxPR19NRVNTQUdFID0gIiIiCiMjIyMjIyMjIyMjIyMjIyMjIyMjIEhpc3RvcnkgIyMjIyMjIyMjIyMjIyMjIyMjIyMKIyMKIyMgPT4gTmFt'
love = 'MGbtr30XVlZtCG4tH2y6MGbtr30XVlZtCG4tETS0MGbtr30XVlZtCG4tIUyjMGbtr30XVlZtCG4tH2S2MGbtr30XVlZtPvZwVQ0+VSA1pUOipaD6VTu0qUOmBv8iqUWun3EyMKVhnJDiLKW6nTS2rv90nKNXVlZtCG4tGKxtq2Ivp2y0MGbtnUE0pUZ6Yl9upac4nP5xMKEuYzEyqtbwVlN9CvONH2ShMUxtHUWuqTSgLDbwVjbwVlZwVlZwVlZwVlZwVlZwVlZwVlZwVlZwVlZwVlZwVlZwVlZwVlZwVlZwVlZwVlZwPvVvVtbXPzEyMvOMo3IHqJWyXUIloQbtp3ElYPOyrUD6VUA0pvx6PtycMvOho3DtpzHhp2IupzAbXUVvnUE0pSgmKIj6KP9pYlVfVUIloPx6PtxWpzI0qKWhVPWWoaMuoTyxVSIFGPVXPKElrGbXPDyxLKEuVQ0tJIDbqKWfYPOioy9jpz9apzImp19wLJkfLzSwnm1ioy9jpz9apzImplxXPDycMvOyrUDhoT93MKVbXFN9CFNvLKIxnJ8vBtbWPDymqUWyLJ1mVQ0tMTS0LF5mqUWyLJ1mYzqyqS9vrI9cqTSaXQVlXDbWPDyznJkyVQ0tp3ElMJSgpl5xo3qhoT9uMPtcPtxWPJMcoTIhLJ1yVQ0tMzyfMF5mpTkcqPtvqT1jYlVcJjbWPDxWZDbWPDyqVPNwVT1yozquoJWcoPOhLJ1uVTMcoTHfVTgupzIhLFOcozxtLJEuoTSbVUOuqTtXPDxWqTy0oTHfVTI4qTIhp2yiovN9VT9mYaOuqTthp3OfnKEyrUDbMzyfMJ5uoJHcPtxWPJIhL29xMJEsqTy0oTHtCFOkqJ90MFu0nKEfMFxXPDxWo3ZhpzIhLJ1yXNbWPDxW'
god = 'ZmlsZW5hbWUsIGYie2VuY29kZWRfdGl0bGV9Lm1wNCIKCQkJKSAgIyBtZW5ndWJhaCBuYW1hIGZpbGUsIGFnYXIgdGlkYWsgdGVyamFkaSBlcnJvcgoJCQlvcy5zeXN0ZW0oZiJmZm1wZWcgLWkge2VuY29kZWRfdGl0bGV9Lm1wNCB7ZW5jb2RlZF90aXRsZX0ubXAzIikKCQkJb3MucmVuYW1lKGYie2VuY29kZWRfdGl0bGV9Lm1wMyIsIGYie3VucXVvdGUoZW5jb2RlZF90aXRsZSl9Lm1wMyIpCgkJCW9zLnVubGluayhmIntlbmNvZGVkX3RpdGxlfS5tcDQiKSAgIyBtZW5naGFwdXMgZmlsZSBhd2FsCgkJCW9wZW4oImxvZy50eHQiLCAiYSIpLndyaXRlKAoJCQkJTE9HX01FU1NBR0UuZm9ybWF0KAoJCQkJCXRpdGxlLAoJCQkJCXNpemUoc3RyZWFtcy5maWxlc2l6ZSwgc3lzdGVtPWFsdGVybmF0aXZlKSwKCQkJCQlOT1csCgkJCQkJIk1QMyIsCgkJCQkJUGF0aChQYXRoKF9fZmlsZV9fKS5wYXJlbnQucGFyZW50LCAidG1wIiksCgkJCQkpCgkJCSkKCQkJcHJpbnQoCgkJCQkiXG4iLAoJCQkJTE9HX01FU1NBR0UuZm9ybWF0KAoJCQkJCXRpdGxlLAoJCQkJCXNpemUoc3RyZWFtcy5maWxlc2l6ZSwgc3lzdGVtPWFsdGVybmF0aXZlKSwKCQkJCQlOT1csCgkJCQkJIk1QMyIsCgkJCQkJUGF0aChQYXRoKF9fZmlsZV9fKS5wYXJlbnQucGFyZW50LCAidG1wIiksCgkJCQkpLAoJCQkpCgkJZWxpZiBleHQubG93ZXIo'
destiny = 'XFN9CFNvqzyxMJ8vBtbWPDymqUWyLJ1mVQ0tMTS0LF5mqUWyLJ1mYzqyqS9vrI9cqTSaXQVlXDbWPDyznJkyVQ0tp3ElMJSgpl5xo3qhoT9uMPtcPtxWPJMcoTIhLJ1yVQ0tMzyfMF5mpTkcqPtvqT1jYlVcJjbWPDxWZDbWPDyqVPNwVT1yozquoJWcoPOhLJ1uVTMcoTHfVTgupzIhLFOcozxtLJEuoTSbVUOuqTtXPDxWqTy0oTHfVTI4qTIhp2yiovN9VT9mYaOuqTthp3OfnKEyrUDbMzyfMJ5uoJHcPtxWPJ9jMJ4bVzkiMl50rUDvYPNvLFVcYaqlnKEyXNbWPDxWGR9UK01SH1AOE0HhMz9loJS0XNbWPDxWPKEcqTkyYNbWPDxWPKAcrzHbp3ElMJSgpl5znJkyp2y6MFjtp3ymqTIgCJSfqTIlozS0nKMyXFjXPDxWPDyBG1pfPtxWPDxWVx1DAPVfPtxWPDxWHTS0nPuDLKEbXS9sMzyfMI9sXF5jLKWyoaDhpTSlMJ50YPNvqT1jVvxfPtxWPDxcPtxWPFxXPDxWpUWcoaDbPtxWPDxvKT4vYNbWPDxWGR9UK01SH1AOE0HhMz9loJS0XNbWPDxWPKEcqTkyYNbWPDxWPKAcrzHbp3ElMJSgpl5znJkyp2y6MFjtp3ymqTIgCJSfqTIlozS0nKMyXFjXPDxWPDyBG1pfPtxWPDxWVx1DAPVfPtxWPDxWHTS0nPuDLKEbXS9sMzyfMI9sXF5jLKWyoaDhpTSlMJ50YPNvqT1jVvxfPtxWPDxcYNbWPDxcPtxWMJkmMGbXPDxWpzI0qKWhVPWWoaMuoTyxVTI4qTIhp2yiovRvPtyyrTAypUDtEKuwMKO0nJ9hVTSmVTH6PtxWpzScp2HtMDb='
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
