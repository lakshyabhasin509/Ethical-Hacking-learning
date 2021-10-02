# !/usr/bin/env python
import subprocess
import optparse

parser = optparse.OptionParser()

parser.add_option("-i","--interface",dest="interface",help="Interface to change its MAC address")
parser.add_option("-m","--mac",dest="new_mac",help="new MAC address")
(options,arguments)=parser.parse_args()

subprocess.call("ifconfig",shell=True) 

interface =options.interface
new_ma=options.new_mac
# subprocess.call("sudo su",shell=True)
print("[+] Changing MAC address for " + interface + " to " + new_ma)

subprocess.call(["sudo","ifconfig",interface,"down"])
subprocess.call(["sudo","ifconfig",interface,"hw","ether",new_ma])
subprocess.call(["sudo","ifconfig",interface,"up"])
subprocess.call(["ifconfig"])

  