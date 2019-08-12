import dlib

class backend:
  def __init__(self, flag = False):
    '''
    Creates an instance of dlib's..
    * HOG face detector.
    * Facial landmarks detector.
    * Embedding generator.
    '''
    self.face_detector = dlib.get_frontal_face_detector()
    if not flag:
      self.landmark_detector = dlib.shape_predictor("recognition_system/model/landmark_training.dat")
      self.embedding_resnet = dlib.face_recognition_model_v1("recognition_system/model/face_rec_resnet.dat")
    else:
      self.landmark_detector = dlib.shape_predictor("model/landmark_training.dat")
      self.embedding_resnet = dlib.face_recognition_model_v1("model/face_rec_resnet.dat")

  def find_faces(self, image):
    '''
    Uses an instance of dlib's HOG face detector to find
    the location of all faces that present in `image`.
    May fail to detect a blurry/unclear face. 
    '''
    faces_found = self.face_detector(image, 1)
    return faces_found

  def embed_face(self, image, face):
    '''
    Uses an instance of dlib's facial landmarks detector
    to find 68 landmarks in the given `face` and feeds
    these landmarks to dlib's embedding ResNet to generate
    the embeddings of the face provided.
    '''
    landmarks = self.landmark_detector(image, face)
    embeddings = self.embedding_resnet.compute_face_descriptor(image, landmarks, 1)
    return embeddings
