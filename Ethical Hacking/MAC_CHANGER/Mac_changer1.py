#!usr/bin/env python
import subprocess
subprocess.call("sudo su", shell=True)
subprocess.call("ifconfig", shell=True)
subprocess.call("ifconfig eno1 down", shell=True)
subprocess.call("ifconfig eno1 hw ether 00:22:11:33:44:55 ", shell=True)
subprocess.call("ifconfig eno1 up", shell=True)
subprocess.call("ifconfig", shell=True)