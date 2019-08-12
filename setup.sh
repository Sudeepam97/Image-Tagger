sudo apt-get install build-essential cmake pkg-config
sudo apt-get install libopenblas-dev liblapack-dev
sudo apt-get install python3-dev
virtualenv -p /usr/bin/python3 deps/
source deps/bin/activate
pip3 install flask==1.0.3
pip3 install numpy==1.16.4
pip3 install pillow==6.0.0
pip3 install imageio==2.5.0
pip3 install dlib==19.17.0
python3 recognition_system/model/download.py
bzip2 -d recognition_system/model/landmark_training.dat.bz2
bzip2 -d recognition_system/model/face_rec_resnet.dat.bz2
