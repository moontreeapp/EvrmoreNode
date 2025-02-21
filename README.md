# EvrmoreNode
containerized evrmored + electrumx with startup command so its easy to run an evrmore node


## run with:
note: make sure you replace the -v locations with a folder on your machine
```
docker run -d --name EvrmoreNode \
  -p 8819:8819 \
  -p 50001:50001 \
  -p 50002:50002 \
  -p 50004:50004 \
  -p 8000:8000 \
  -v %APPDATA%\\EvrmoreNode\\evrmore:/home/evr/.evrmore \
  -v %APPDATA%\\Satori\\electrumx:/home/evr/electrumx \
  sebawilq/evrx:latest
```
