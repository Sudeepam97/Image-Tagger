source deps/bin/activate
python3 serve_static.py & python3 app.py && kill $!
