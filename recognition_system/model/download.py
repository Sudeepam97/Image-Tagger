import urllib.request
print ("Downloading Face Recognition Models...")
url = "http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2"
urllib.request.urlretrieve(url, "recognition_system/model/landmark_training.dat.bz2")
url = "http://dlib.net/files/dlib_face_recognition_resnet_model_v1.dat.bz2"
urllib.request.urlretrieve(url, "recognition_system/model/face_rec_resnet.dat.bz2")
