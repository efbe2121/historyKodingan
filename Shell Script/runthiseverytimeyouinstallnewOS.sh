sudo add-apt-repository ppa:persepolis/ppa -y
sudo add-apt-repository universe -y

sudo apt-get update -y

sudo apt-get install -y \
persepolis preload ttf-mscorefonts-installer \
libsdl2-dev mingw-w64 gedit gparted snapd \
libsdl-image1.2 libsdl-image1.2-dev guile-2.0 \
guile-2.0-dev libsdl1.2debian libart-2.0-dev libaudiofile-dev \
libesd0-dev libdirectfb-dev libdirectfb-extra libfreetype6-dev \
libxext-dev x11proto-xext-dev libfreetype6 libaa1 libaa1-dev \
libslang2-dev libasound2 libasound2-dev openjdk-11-jdk g++ \
build-essential gcc

sudo snap install whatsdesk
sudo snap install mailspring
sudo snap install discord

python3 --version &> dev/null/
if [ $? -ne 0 ];then
  sudo apt-get install python3 -y
fi

pip -h &> dev/null/
if [ $? -ne 0 ];then
  sudo apt-get install python3-pip
fi

wget -h &> dev/null/
if [ $? -ne 0 ];then
  sudo apt-get install wget -y
fi

mkdir ~/Lite
wget -O lite.zip -P ~/Lite/ https://github.com/rxi/lite/archive/v1.11.zip
cd ~/Lite/
unzip lite.zip
./build.sh

wget -O wps.deb -P ~/Downloads/ https://wdl1.pcfg.cache.wpscdn.com/wpsdl/wpsoffice/download/linux/9719/wps-office_11.1.0.9719.XA_amd64.deb
wget -O chrome.deb -P ~/Downloads/ https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i ~/Downloads/wps.deb
sudo dpkg -i ~/Downloads/chrome.deb

# THIS IS TO FIX EVERYTHING IF ANYTHING FAILS
sudo apt-get install -f -y

#sudo echo "alias code='cd ~/Lite && ./lite'" >> ~/.bash_aliases
#sudo echo "alias python='python3'" >> ~/.bash_aliases
