import scapy.all as scapy

#TODO Add command line argument functionality

# Basic scan which is not hidden, will ping every computer.
def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_req_brd = broadcast/arp_request
    ans = scapy.srp(arp_req_brd, timeout=1, verbose=False)[0]
    list_clients = []
    for single in ans:
        dict_client = {"IP": single[1].psrc, "MAC": single[1].hwsrc}
        list_clients.append(dict_client)
    return list_clients


def print_all(result):
    print("IP\t\t\tMAC Address")
    print("-----------------------------------------------------------")
    for single in result:
        print(single["IP"] + "\t\t" + single["MAC"])


scan_result = scan("1.11.1.1/24")
print_all(scan_result)


