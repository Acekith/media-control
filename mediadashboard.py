from flask import Flask
from startprocess import startprocess
from setactivewindow import setactivewindow
app = Flask(__name__)



@app.route('/dashboard/start/<program>')
def startstuff(program):
    x = ['wireshark', 'steam', 'kodi']
    if program in x: 
        if startprocess(program):
            return 'Started'
        else:
            return 'Already Running'
    else:
        return 'I\'m sorry Dave, I\'m afraid I can\'t do that'

@app.route('/dashboard/switch/<process>')
def setcurrentwindow(process):
    x = ['Wireshark', 'steam', 'kodi']
    if process in x: 
        setactivewindow(process)
        return 'Switch sucessful'
    else:
        return 'I\'m sorry Dave, I\'m afraid I can\'t do that'
if __name__ == '__main__':
    app.run(debug =True)
