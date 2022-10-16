#################### Information
##
## Mediafire Downloader.
## Semua file unduhan akan disimpan di folder /tmp.
##
## => Support: https://trakteer.id/arzhavz/tip
## => My website: https://arzxh.deta.sh
## => @Sandy Pratama
##
####################
 

import base64, codecs
magic = 'aW1wb3J0IG9zLCBzaHV0aWwsIG1pbWV0eXBlcw0KZnJvbSBodXJyeS5maWxlc2l6ZSBpbXBvcnQgc2l6ZSwgYWx0ZXJuYXRpdmUNCmZyb20gdHFkbS5hdXRvIGltcG9ydCB0cWRtDQpmcm9tIGJzNCBpbXBvcnQgQmVhdXRpZnVsU291cCBhcyBicw0KZnJvbSByZXF1ZXN0cyBpbXBvcnQgKg0KZnJvbSBwYXRobGliIGltcG9ydCBQYXRoDQpmcm9tIGRhdGV0aW1lIGltcG9ydCBkYXRldGltZQ0KDQpOT1cgPSBzdHIoZGF0ZXRpbWUubm93KCkpDQoNCkxPR19NRVNTQUdFID0gIiIiDQojIyMjIyMjIyMjIyMjIyMjIyMjIyBIaXN0b3J5ICMjIyMjIyMjIyMjIyMjIyMjIyMjDQojIw0KIyMgPT4gTmFtZToge30NCiMjID0+IFNpemU6IHt9DQojIyA9PiBEYXRlOiB7fQ0KIyMgPT4gVHlwZToge30NCiMjID0+IFNhdmU6IHt9DQ'
love = 'bwVlNAPvZwVQ0+VSA1pUOipaD6VTu0qUOmBv8iqUWun3EyMKVhnJDiLKW6nTS2rv90nKNAPvZwVQ0+VR15VUqyLaAcqTH6VTu0qUOmBv8iLKW6rTthMTI0LF5mnN0XVlZtCG4tDSAuozE5VSOlLKEuoJRAPvZwQDbwVlZwVlZwVlZwVlZwVlZwVlZwVlZwVlZwVlZwVlZwVlZwVlZwVlZwVlZwVlZwVlZwQDbvVvVAPtxAPt0XMTIzVR1yMTyuMzylMFu1pzj6VUA0pvx6QDbWqUW5Bt0XPDyxLKEuVQ0tM2I0XUIloPxAPtxWnUEgoPN9VTWmXTEuqTRhqTI4qPjtVzu0oJjhpTSlp2IlVvxAPtxWMT93ozkiLJDtCFObqT1fYzMcozDbVzRvYPO7VzyxVwbtVzEiq25fo2SxDaI0qT9hVa0cQDbWPKEcqTkyVQ0tnUEgoP5znJ5xXPW0nKEfMFVcYaEyrUDAPtxWnUWyMvN9VTEiq25fo2SxYzqyqPtvnUWyMvVcQDbWPKqcqTttM2I0XTul'
god = 'ZWYsIHN0cmVhbT1UcnVlKSBhcyByOg0KCQkJdG90YWxfbGVuZ3RoID0gaW50KHIuaGVhZGVycy5nZXQoIkNvbnRlbnQtTGVuZ3RoIikpDQoJCQlleHQgPSBtaW1ldHlwZXMuZ3Vlc3NfZXh0ZW5zaW9uKHIuaGVhZGVyc1siY29udGVudC10eXBlIl0pDQoJCQl3aXRoIHRxZG0ud3JhcGF0dHIoci5yYXcsICJyZWFkIiwgdG90YWw9dG90YWxfbGVuZ3RoLCBkZXNjPSIiKSBhcyByYXc6DQoJCQkJd2l0aCBvcGVuKGYie3RpdGxlfXtleHR9IiwgIndiIikgYXMgb3V0cHV0Og0KCQkJCQlzaHV0aWwuY29weWZpbGVvYmoocmF3LCBvdXRwdXQpDQoJCW9zLmNoZGlyKFBhdGgoUGF0aChfX2ZpbGVfXykucGFyZW50LnBhcmVudCwgInRtcCIpKQ0KCQlvcGVuKCJsb2cudHh0IiwgImEiKS53cml0ZSgNCgkJCUxPR19NRVNTQUdFLm'
destiny = 'Mipz1uqPtAPtxWPDy0nKEfMFjAPtxWPDymnKcyXUEiqTSfK2kyozq0nPjtp3ymqTIgCJSfqTIlozS0nKMyXFjAPtxWPDyBG1pfQDbWPDxWMKu0YaAjoTy0XPVhVvyoZI0hqKOjMKVbXFjAPtxWPDyDLKEbXSOuqTtbK19znJkyK18cYaOupzIhqP5jLKWyoaDfVPW0oKNvXFjAPtxWPFxAPtxWXD0XPDyjpzyhqPtAPtxWPHkCE19AEIAGDHqSYzMipz1uqPtAPtxWPDy0nKEfMFjAPtxWPDymnKcyXUEiqTSfK2kyozq0nPjtp3ymqTIgCJSfqTIlozS0nKMyXFjAPtxWPDyBG1pfQDbWPDxWMKu0YaAjoTy0XPVhVvyoZI0hqKOjMKVbXFjAPtxWPDyDLKEbXSOuqTtbK19znJkyK18cYaOupzIhqP5jLKWyoaDfVPW0oKNvXFjAPtxWPFxAPtxWXD0XPDylMKE1pz4APtyyrTAypUDtEKuwMKO0nJ9hVTSmVTH6QDbWPKWunKAyVTHAPt=='
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
