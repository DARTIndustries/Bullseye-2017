sudo apt-get update
sudo apt-get upgrade

sudo apt-get install cmake libjpeg8-dev git

mkdir src
cd src

git clone https://github.com/jacksonliam/mjpg-streamer.git
cd mjpg-streamer
cd mjpg-streamer-experimental
make
sudo make install
