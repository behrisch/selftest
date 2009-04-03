
import subprocess

origPopen = subprocess.Popen

class MyPopen(origPopen):
    def __init__(self, cmdArgs, *args, **kwargs):
        origPopen.__init__(self, cmdArgs, *args, **kwargs)
        if cmdArgs[0] in [ "cvs", "bzr", "hg" ]:
            raise OSError, "Pretending " + cmdArgs[0].upper() + " isn't installed!"
        
subprocess.Popen = MyPopen
