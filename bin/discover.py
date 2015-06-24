# -*- encoding: utf8 -*-
from __future__ import division, print_function, unicode_literals

import socket

import bitstring
import netifaces
import pylifx

_BROADCAST_PORT = 56700
_TIMEOUT = 3


def find_master_bulbs(broadcast_address):
    try:
        broadcast_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        broadcast_socket.settimeout(_TIMEOUT)
        broadcast_socket.bind(('', _BROADCAST_PORT))

        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

        sock.sendto(
            pylifx.packet.encode(
                'getPanGateway',
                protocol=pylifx.networking._LIFX_PROTO_TOBULB,
                bulb_addr=pylifx.networking._processMAC(pylifx.networking._BLANK_MAC),
                site_addr=pylifx.networking._processMAC(pylifx.networking._BLANK_MAC),
            ).bytes,
            (broadcast_address, _BROADCAST_PORT)
        )

        while True:
            data = broadcast_socket.recvfrom(41)
            try:
                lifx_data = pylifx.packet.decode(data[0])
                if lifx_data[0] == 'panGateway':
                    return {'site_addr': lifx_data[1]['site_addr'], 'ip': data[1][0]}
            except bitstring.ReadError:
                # Unable to decode message means something else replied
                pass
    finally:
        broadcast_socket.close()
        sock.close()


def to_mac_address(addr):
    return ':'.join(addr[i:i+2] for i in xrange(0, 11, 2))


def main():
    for interface in netifaces.interfaces():
        interface_addr = netifaces.ifaddresses(interface)
        if socket.AF_INET in interface_addr:
            if 'broadcast' in interface_addr[socket.AF_INET][0]:
                broadcast_address = interface_addr[socket.AF_INET][0]['broadcast']

                print("'{}' interface (broadcast address {})".format(interface, broadcast_address))

                for retry_count in xrange(3):
                    try:
                        bulb = find_master_bulbs(broadcast_address)
                        print("  IP Address:  ", bulb['ip'])
                        print("  MAC Address: ", to_mac_address(bulb['site_addr']))
                        break
                    except socket.timeout:
                        print("Didnt receive a reply. Trying again... (retry=%d)" % retry_count)
                else:
                    print("Gave up waiting for a reply")
                    return


if __name__ == '__main__':
    main()
