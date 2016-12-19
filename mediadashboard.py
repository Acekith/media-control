from flask import Flask
from flask_cors import CORS
from startprocess import startprocess
from setactivewindow import setactivewindow
app = Flask(__name__)
CORS(app)

@app.route('/dashboard/start/<program>')
def startstuff(program):
    x = ['google-chrome', 'Steam', 'Kodi']
    if program in x:
        if startprocess(program):
            return 'Started'
        else:
            return 'Already Running'
    else:
        return 'I\'m sorry Dave, I\'m afraid I can\'t do that'

@app.route('/dashboard/switch/<process>')
def setcurrentwindow(process):
    x = ['google-chrome', 'Steam', 'Kodi']
    print(x)

    if process in x:
        return setactivewindow(process)
    else:
        return 'I\'m sorry Dave, I\'m afraid I can\'t do that'

if __name__ == '__main__':
    app.run(debug =True, host='0.0.0.0')
