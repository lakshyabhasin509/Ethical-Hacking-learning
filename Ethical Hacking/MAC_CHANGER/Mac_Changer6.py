# !/usr/bin/env python
import subprocess
import optparse
# using functions

def change_mac(interface , new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)

    subprocess.call(["sudo","ifconfig",interface,"down"])
    subprocess.call(["sudo","ifconfig",interface,"hw","ether",new_mac])
    subprocess.call(["sudo","ifconfig",interface,"up"])
    subprocess.call(["ifconfig"])

def get_args():

    parser = optparse.OptionParser()

    parser.add_option("-i","--interface",dest="interface",help="Interface to change its MAC address")
    parser.add_option("-m","--mac",dest="new_mac",help="new MAC address")
    (options,arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface , use --help for more info")
    elif not options.new_mac:
        parser.error("[-] Please specify a new mac ,use --help for more info")
    return options




# interface =options.interface
# new_ma=options.new_mac

options = get_args()
change_mac(options.interface,options.new_mac)