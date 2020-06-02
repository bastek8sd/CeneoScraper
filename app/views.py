#import apki
from app import app

#routing dla strony głównej
@app.route('/')
@app.rout('/index')
def index():
    return "Hello World"