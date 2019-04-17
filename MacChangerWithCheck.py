import subprocess
import argparse
import re

parser = argparse.ArgumentParser(description='Process commands')
parser.add_argument("-i", "--interface", dest="interface", help="Interface to change MAC Address")
parser.add_argument("-m", "--mac", dest="new_mac", help="New MAC Address")
args = parser.parse_args()

interface = args.interface
new_mac = args.new_mac

print("[+] Changing MAC Address to " + new_mac + " on " + interface)
subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])

# Does a search of the ifconfig output after the change and prints the current MAC
ifconfig_data = subprocess.check_output(["ifconfig", interface])
mac_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_data)
print("Current MAC Address is " + str(mac_search_result.group(0)))


