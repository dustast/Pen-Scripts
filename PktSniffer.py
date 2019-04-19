import scapy.all as scapy
from scapy.layers import http


def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_pkt, filter="udp")


def process_pkt(packet):
    if packet.haslayer(http.HTTPRequest):
        print(packet)


sniff("eth0")
