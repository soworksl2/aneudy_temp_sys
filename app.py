from flask import Flask
app: Flask = Flask(__name__, static_url_path='/static')


#pages
from temp_sys.pages import login

#api
from temp_sys.api import valid_token
