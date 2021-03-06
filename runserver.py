#!/usr/bin/env python
# -*- coding: utf-8 -*-

#=======================================
# Auther : NareN
# git    : https://github.com/DEVELByte
#=======================================

import os
from application import app
from flask_cors import CORS

CORS(app)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8002))
    app.run('0.0.0.0', port=port, threaded=True)
    # app.run