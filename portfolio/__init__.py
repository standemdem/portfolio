from flask import Flask

app = Flask(__name__)

# This import is to be located at the end, otherwise it creates a circular import Error
from portfolio import routes
