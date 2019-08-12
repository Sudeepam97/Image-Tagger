# Image Tagger
* Start by adding photos of faces of people that you want to recognize, to the folder `recognition_system/auth_images` and append their names in the file
`recognition_system/auth_images/unique_ids.txt`.
* Look at the current state of `recognition_system/auth_images/` for an example.

* Next, set-up the project by running `setup.sh` and `embed_known.sh` as follows:
```sh
chmod +x setup.sh   # executable permissions, must be done only once.
./setup.sh            # Run
chmod +x embed_known.sh
./embed_known.sh
```

* Finally run the program as follows:
```sh
chmod +x run.sh   # executable permissions, must be done only once.
./run.sh          # Run
```

* Next, visit  http://localhost:5000 in your browser, choose a file and then submit to see all the recognized faces get tagged in the image.