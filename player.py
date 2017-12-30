import subprocess
import os
path = os.getcwd()

def start(song):
	global proc
	proc = subprocess.Popen(["sudo","python","PiStation.py", "-f","99",os.path.join(path,'Music',song)])
def stop():
	proc.terminate()
	x = subprocess.Popen(["sudo","pkill","-f","fm_transmitter"])
