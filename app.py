from flask import Flask, request, abort
import json
from functools import wraps
from jose import jwt
from urllib.request import urlopen


app = Flask(__name__)

AUTH0_DOMAIN = @TODO_REPLACE_WITH_YOUR_DOMAIN
ALGORITHMS = ['RS256']
API_AUDIENCE = @TODO_REPLACE_WITH_YOUR_API_AUDIENCE

class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code

