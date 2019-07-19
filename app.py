from tornado import ioloop, web
import sys
import os
import base64
import json
from io import StringIO

my_port = 50505
if len(sys.argv) > 1:
    my_port = sys.argv[1]

settings = {
    "autoreload": True
}

class ExampleHandler(web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    def get(self):
        self.write("Hello World")

def make_app():
    return web.Application([(r"/", ExampleHandler)], **settings)

if __name__ == "__main__":
    app = make_app()
    app.listen(my_port)
    ioloop.IOLoop.current().start()
