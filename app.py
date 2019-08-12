import os
from flask import Flask, render_template, request
import recognition_system.identify_faces as rsif

app = Flask(__name__)

UPLOAD_FOLDER = os.path.basename('recognition_system')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
  return render_template('index.html')
	
@app.route('/upload', methods = ['POST', 'GET'])
def upload_file():
  if request.method == 'POST':
    img = request.files['pic']
    f = os.path.join(app.config['UPLOAD_FOLDER'], "test.jpg")
    img.save(f)
    obj = rsif.backend()
    people_found = obj.look_up_faces()
  return render_template('index.html', output_text = "People Present", people_present = people_found)

if __name__ == "__main__":
	app.run(host='0.0.0.0', port = 5000)
