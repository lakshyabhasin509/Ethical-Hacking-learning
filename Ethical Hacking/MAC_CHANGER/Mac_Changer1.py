# !/usr/bin/env python
import subprocess
subprocess.call("ifconfig",shell=True)   
interface =input("interface >>")
new_mac=input("new mac >>")
# subprocess.call("sudo su",shell=True)
print("[+] Changing MAC address for " + interface + " to " + new_mac)
          
subprocess.call("sudo ifconfig "+ interface +" down",shell=True)
subprocess.call("sudo ifconfig "+ interface + " hw ether " +new_mac,shell=True)
subprocess.call("sudo ifconfig " + interface + " up",shell=True)    
subprocess.call("ifconfig",shell=True)   