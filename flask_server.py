from flask import Flask
from aiohttp import web
from aiohttp_wagi import WSGIHandler

app = Flask(__name__)

@app.route('/')
def home():
    return 'Home page'

def make_aiohttp_app(app):
    wsgi_handler = WSGIHandler
    aioapp = web.application()
    aioapp.router.add_route('*', '/{path_info:.*}', wsgi_handler)
    return aioapp

aioapp = make_aiohttp_app(app)


# if __name__ == '__main__':
#     app.run(debug=True)