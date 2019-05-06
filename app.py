from time import sleep
from flask import Flask, send_file


app = Flask(__name__)


@app.route('/kitten<int:i>.jpg')
def kitten(i):
    sleep(10)
    return send_file('kittens/kitten%i.jpg' % i)


app.run(host='0.0.0.0', port=80)
