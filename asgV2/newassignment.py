from __future__ import unicode_literals

import os
import sys
import redis

from argparse import ArgumentParser

from flask import Flask, request, abort, json
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cor = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# obtain the port that heroku assigned to this app.
heroku_port = os.getenv('PORT', None)

myDict = {}

@app.route("/callback", methods=['POST'])
@cross_origin(origin='*', allow_headers=['Content-Type'])
def callback():
    header = request.headers
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    if body in myDict:
        myDict[body] += 1
    else:
        myDict[body] = 1

    replydata = {'input' : body}
    replydata['count'] = myDict[body]

    return json.dumps(replydata)


@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request. %s', e)
    return "An internal error occurs", 500

if __name__ == "__main__":
    arg_parser = ArgumentParser(
        usage='Usage: python ' + __file__ + ' [--debug] [--help]'
    )
    arg_parser.add_argument('-p', '--production', action='store_true', help='Indicate this is production, not debug')
    options = arg_parser.parse_args()

    if options.production:
        app.run(host='0.0.0.0', debug=False, port=heroku_port)
    else:
        app.run(host='127.0.0.1', debug=True)
        
        

