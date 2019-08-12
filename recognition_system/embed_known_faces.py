import imageio
import pickle
import find_and_embed_faces
import numpy as np

def get_embeddings_for_known_faces():
  '''
  Compute the embeddings for known faces and store them in a file.
  '''
  model = find_and_embed_faces.backend(True)

  f = open ("auth_images/names.txt", "r")
  names = f.readlines()
  f.close()

  known_faces = {}
  for i in range(0, len(names)):
    names[i] = names[i].replace('\n', '')
    img = imageio.imread("auth_images/" + names[i] + ".jpg")
    faces_found = model.find_faces(img)
    embeddings = model.embed_face(img, faces_found[0])
    known_faces[names[i]] = np.array(embeddings)

  f = open("auth_images/known_embeddings", "wb")
  pickle.dump(known_faces, f, protocol = pickle.HIGHEST_PROTOCOL)
  f.close()

get_embeddings_for_known_faces()
print("Done! Embeddings of known faces are stored in 'auth_images/known_embeddings'")