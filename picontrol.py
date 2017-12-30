import subprocess
def shutdown_pi():
    subprocess.Popen(['sudo','poweroff'])