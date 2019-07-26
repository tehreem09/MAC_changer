import subprocess
import argparse
import re

# copy default mac here
wlp2s0_default_mac =  ""
enp0s25_default_mac = ""
wwp0s20u10i6_default_mac = ""

def change_mac(dev,mac):
    subprocess.call(["sudo", "ip", "link", "set", "dev", dev , "down"])
    subprocess.call(["sudo", "ip", "link", "set", "dev", dev , "address", mac])
    subprocess.call(["sudo", "ip", "link", "set", "dev", dev , "up"])
    subprocess.call(["ip", "link", "show" , dev])

parser = argparse.ArgumentParser(description= "Changes MAC address and/or Reset it.")
parser.add_argument("-d","--dev", dest="dev", help="dev name whose mac you want to change")
parser.add_argument("-m","--mac", dest="mac", help="new mac address, if not given then by default reset mac address")
args_values = parser.parse_args()

if not args_values.dev: print("[-] please specify dev")
elif not args_values.mac:
    if args_values.dev == "wlp2s0": change_mac(args_values.dev,wlp2s0_default_mac)
    elif args_values.dev == "enp0s25": change_mac(args_values.dev,enp0s25_default_mac)
    elif args_values.dev == "wwp0s20u10i6": change_mac(args_values.dev,wwp0s20u10i6_default_mac)
    else: print("[-] dev name is incorrect.")
elif (args_values.dev == "wlp2s0" or args_values.dev =="enp0s25" or args_values.dev =="wwp0s20u10i6") and re.match(r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w',args_values.mac):
    change_mac(args_values.dev,args_values.mac)
else: print("[-] dev and/or mac is incorrect")