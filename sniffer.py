import socket
import struct
import binascii

# This will work on *nix only.
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.ntohs(0x0800))

while True:
    packet = s.recvfrom(65565)

    print("\n\n------------ Ethernet Header----- [+]")

    for i in eth_header(packet[0][0:14]).iteritems():
        a,b=i
        print("{} : {} | ".format(a,b))

def eth_header(data):
    fragment = struct.unpack("!6s6sH", data)
    destination_mac = binascii.hexlify(fragment[0])
    source_mac = binascii.hexlify(fragment[1])
    protocol = fragment[2]

    result = {
      "Destination MAC": destination_mac,
      "Source MAC": source_mac,
      "Protocol": protocol
    }

    return result


