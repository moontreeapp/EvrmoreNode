# EvrmoreNode
containerized evrmored + electrumx with startup command so its easy to run an evrmore node

## build with:
```
docker build -t moontreeapp/evrmorenode:lastest .
```

## run with:
note: make sure you replace the -v locations with a folder on your machine
```
mkdir %APPDATA%/EvrmoreNode
mkdir %APPDATA%/EvrmoreNode/evrmore
mkdir %APPDATA%/EvrmoreNode/electrumx
```
command: (sebawilq/evrx:latest)
```
docker run -d --name EvrmoreNode \
  -p 8819:8819 \
  -p 50001:50001 \
  -p 50002:50002 \
  -p 50004:50004 \
  -p 8000:8000 \
  -v %APPDATA%\\EvrmoreNode\\evrmore:/home/evr/.evrmore \
  -v %APPDATA%\\EvrmoreNode\\electrumx:/home/evr/electrumx \
  moontreeapp/evrmorenode:latest

docker run -d --name EvrmoreNode -p 8819:8819 -p 50001:50001 -p 50002:50002 -p 50004:50004 -p 8000:8000 -v C:\\repos\\Moontree\\EvrmoreNode\\EvrmoreNode\\evrmore:/home/evr/.evrmore -v C:\\repos\\Moontree\\EvrmoreNode\\EvrmoreNode\\electrumx:/home/evr/electrumx moontreeapp/evrmorenode:latest
```
