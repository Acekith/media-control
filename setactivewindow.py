import subprocess

def setactivewindow( process ):

    #activewindow = subprocess.check_output('xdotool getactivewindow', shell=True).strip()
    #activewindow = hex(int(activewindow))


    active = subprocess.check_output(['wmctrl', '-lp'], env={'DISPLAY': ':0'})

    activelines = active.splitlines()
    #activearray = []

    for line in activelines:
        if process in line:
            print 'process found'
            print line
            print 'windowactivate input=' + hex(int(line.split(None,1)[0], 16))
            subprocess.check_output('xdotool windowactivate ' + hex(int(line.split(None,1)[0], 16)), shell=True, env={'DISPLAY': ':0'}).strip()
            return "success"
    else:
        try:
            process = process.lower()
            subprocess.check_call('pgrep ' + process + ' > /dev/null', shell=True, env={'DISPLAY': ":0"} )
            print process + ' is running'
            return 'running'
        except:
            subprocess.Popen(process + ' &', shell=True, env={'DISPLAY': ":0"})
            return 'launched'

