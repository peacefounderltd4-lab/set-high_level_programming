#!/usr/bin/python3
from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        body = b"my index page is so cool! Mainly because it's in Python" if self.path == "/" else b"Not found"
        self.send_response(200 if self.path == "/" else 404)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_PUT(self):
        body = b"You find me!" if self.path == "/catch_me" else b"Not found"
        self.send_response(200 if self.path == "/catch_me" else 404)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

HTTPServer(("0.0.0.0", 5000), Handler).serve_forever()
