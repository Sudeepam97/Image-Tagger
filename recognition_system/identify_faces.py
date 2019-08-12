import numpy as np
import pickle
from PIL import Image, ImageDraw, ImageFont
import recognition_system.find_and_embed_faces as rsembed

class backend:
  def __init__(self):
    '''
    Initialize the variables that would be used throughout this program.
    '''
    # Define the font that will be used by PIL to label faces.
    self.fnt = ImageFont.truetype("recognition_system/SourceSerifPro-Regular.ttf", 30)

    # Load the test image as a PIL object and a numpy array.
    self.pil_image = Image.open('recognition_system/test.jpg')
    self.np_image = np.array(self.pil_image)

    # Load the embeddings of faces of known people
    f = open("recognition_system/auth_images/known_embeddings", "rb")
    self.known_embeddings = pickle.load(f)
    f.close()

    # Create objects to access the backend of self made modules
    self.model = rsembed.backend()

  def find_best_match_for_face(self, face):
    '''
    Compare the embeddings of the given face with the
    embeddings of all known faces to find the name of
    the person whose face best resembeles the current one.
    '''
    current_face_embedding = np.array(self.model.embed_face(self.np_image, face))
    best_match = ""
    epsilon = 0.5 # threshold value of norm to declare a match

    for name, embedding in self.known_embeddings.items():
      diff = np.linalg.norm(embedding - current_face_embedding, axis = 0)
      if diff <= epsilon:
        epsilon = diff
        best_match = name
  
    return best_match

  def bound_and_label_face(self, face, name):
    '''
    Draw a bounding box around the `face` that has been
    recognized, and label it with the `name` provided.
    '''
    # Handle negative coordinates.
    top = max(0, face.top())
    bottom = min(face.bottom(), self.np_image.shape[0])
    left = max(0, face.left())
    right = min(face.right(), self.np_image.shape[1])
    
    # Draw and label.
    d = ImageDraw.Draw(self.pil_image)
    d.rectangle(((left, top), (right, bottom)), outline = (0, 255, 0))
    d.text((left, bottom), name, font = self.fnt, fill = (0, 255, 0))

  def look_up_faces(self):
    # Initialize a list of people present
    present = []

    # Locate all the faces that are present in the test image
    faces_in_input_image = self.model.find_faces(self.np_image)

    # Loop through the faces found and search for a match.
    for face in faces_in_input_image:
      best_match = self.find_best_match_for_face(face)
      if best_match != '':
        present.append(best_match)
        self.bound_and_label_face(face, best_match)
    
    # Save the image with faces with bounding boxes.
    self.pil_image.save ("static/tagged_image.jpg")

    return present
