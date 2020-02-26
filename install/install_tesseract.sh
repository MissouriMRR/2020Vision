#!/bin/bash
## Necessary packages
sudo apt-get install g++ autoconf automake libtool pkg-config libpng-dev libjpeg8-dev libtiff5-dev zlib1g-dev

## Build leptonica from source
git clone https://github.com/DanBloomberg/leptonica.git

cd leptonica

./autogen.sh
./configure --prefix=$HOME/local/
make -j8
sudo make install -j8

cd ..

## Install
git clone https://github.com/tesseract-ocr/tesseract.git

cd tesseract

./autogen.sh
./configure --prefix=$HOME/local/
make -j8
sudo make install -j8
sudo ldconfig

