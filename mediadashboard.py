from flask import Flask
from flask_cors import CORS
from startprocess import startprocess
from setactivewindow import setactivewindow
app = Flask(__name__)
CORS(app)

@app.route('/dashboard/start/<program>')
def startstuff(program):
    x = ['google-chrome', 'steam', 'kodi']
    if program in x:
        if startprocess(program):
            return 'Started'
        else:
            return 'Already Running'
    else:
        return 'Program_not_allowed'

@app.route('/dashboard/switch/<process>')
def setcurrentwindow(process):
    x = ['google-chrome', 'Steam', 'Kodi', 'chromium']
    if process in x:
        return setactivewindow(process)
    else:
        return 'error'

if __name__ == '__main__':
    app.run(debug =True, host='0.0.0.0')
