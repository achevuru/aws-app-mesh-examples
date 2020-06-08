import os
import config
import time
from flask import Flask, request
from aws_xray_sdk.core import patch_all, xray_recorder
from aws_xray_sdk.ext.flask.middleware import XRayMiddleware

app = Flask(__name__)

xray_recorder.configure(
    context_missing='LOG_ERROR',
    service=config.XRAY_APP_NAME,
)
patch_all()

XRayMiddleware(app, xray_recorder)

@app.route('/ping')
def ping():
    return 'Pong'

@app.route('/')
def color():
    print('----------------')
    print(request.headers)
    print('----------------')
    time.sleep(45)
    return config.COLOR

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=config.PORT, debug=config.DEBUG_MODE)
