import subprocess

def setactivewindow( process ):

    #activewindow = subprocess.check_output('xdotool getactivewindow', shell=True).strip()
    #activewindow = hex(int(activewindow))

    active = subprocess.check_output('wmctrl -lp', shell=True)
    activelines = active.splitlines()
    #activearray = []

    for line in activelines:
        if process in line:
            print 'process found'
            print line
            print 'windowactivate input=' + hex(int(line.split(None,1)[0], 16))
            subprocess.check_output('xdotool windowactivate ' + hex(int(line.split(None,1)[0], 16)), shell=True).strip()
            return;
            #subprocess.check_output('xdotool setactivewindow ' + hex)

#    if hex(int(line.split(None, 1)[0], 16)) in process
#    if hex(int(line.split(None, 1)[0], 16)) == activewindow:
#        print 'line ' + line
#        print 'line.split '+ line.split(None, 1)[0]
#        print 'line.split hex ' + hex(int(line.split(None,1)[0], 16))
#print 'activewindow ' + activewindow
