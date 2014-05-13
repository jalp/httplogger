""" Simple Flask log server
"""
from flask import Flask, jsonify, request
from urllib import unquote_plus
from time import asctime, gmtime

app = Flask(__name__)


@app.route('/remotelog', methods=['POST'])
def log():
    data = request.get_data()
    d = dict((x.split('=')[0], (x.split('=')[1])) for x in data.split('&'))
    d['msg'] = unquote_plus(d['msg'])
    d['created'] = asctime(gmtime(float(d['created'])))
    print d
    return jsonify({'ret': d})


if __name__ == '__main__':
    app.debug = True
    app.run(port=8888)
