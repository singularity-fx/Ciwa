# -*- coding: utf-8 -*-

# =======================================
# Author : Naren
# git    : https://github.com/DEVELByte
# =======================================

__version__ = '0.1'
from flask import Flask

app = Flask('application')
app.config['SECRET_KEY'] = 'develbyte'
app.debug = True

from application.controllers import *
