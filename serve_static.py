import http.server
import socketserver
import os

PORT = 3000

static_dir = os.path.join(os.path.dirname(__file__), 'static')
os.chdir(static_dir)

Handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("", PORT), Handler)
print("serving at port", PORT)
httpd.serve_forever()
