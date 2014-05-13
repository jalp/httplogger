""" Simple Flask log server
"""

from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/remotelog', methods=['POST'])
def log():
    data = request.get_data()
    ret = "Received data {0}".format(data)
    print ret
    return jsonify({'ret': ret})

if __name__ == '__main__':
    app.debug = True
    app.run(port=8888)
