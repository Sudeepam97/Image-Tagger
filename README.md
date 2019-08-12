# Image Tagger
* Start by adding photos of faces of people that you want to recognize, to the `recognition_system/auth_images` directory, and also append their names in the file `recognition_system/auth_images/unique_ids.txt`. Take a look at the current state of aformentioned directory and file for an example.

* Next, set-up the project by running `setup.sh` and `embed_known.sh` as follows:
```sh
chmod +x setup.sh   # executable permissions, need to be done only once.
./setup.sh          # Run
chmod +x embed_known.sh
./embed_known.sh
```

* Finally run the program as follows:
```sh
chmod +x run.sh   # executable permissions, need to be done only once.
./run.sh          # Run
```

* Next, visit  http://localhost:5000 in your browser, choose a file and then click, submit to see all the faces that have been recognized and tagged in the image.

![Output](sample_input_and_output/tagged_image.jpg?raw=true "Title")
