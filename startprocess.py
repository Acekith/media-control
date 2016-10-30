import subprocess

def startprocess( program ):

    try:
        subprocess.check_call('pgrep ' + program + ' > /dev/null', shell=True )
        print program + ' is running'
        return False
    except:
        subprocess.Popen(program + ' &', shell=True)
        return True
