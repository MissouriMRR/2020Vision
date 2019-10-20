#!/bin/bash
sudo apt-get -y upgrade
sudo apt-get update

git clone https://github.com/IntelRealSense/librealsense.git
cd librealsense

sudo apt-get install -y git libssl-dev libusb-1.0-0-dev pkg-config libgtk-3-dev

# ubuntu 18
sudo apt-get install -y libglfw3-dev libgl1-mesa-dev libglu1-mesa-dev

./scripts/setup_udev_rules.sh

./scripts/patch-realsense-ubuntu-lts.sh
./scripts/patch-ubuntu-kernel-4.16.sh

mkdir build && cd build

cmake ../ -DCMAKE_BUILD_TYPE=Release

sudo make uninstall && make clean && make -j4 && sudo make -j4 install

