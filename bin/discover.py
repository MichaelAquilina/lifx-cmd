# -*- encoding: utf8 -*-
from __future__ import division, print_function, unicode_literals

import datetime as dt
import socket

import bitstring
import netifaces
import pylifx

_BROADCAST_PORT = 56700

# TODO: Broadcast on all available ports?
broadcast_address = netifaces.ifaddresses('wlan0')[socket.AF_INET][0]['broadcast']

broadcast_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
broadcast_socket.settimeout(5)
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

# How do we gracefully give up in the case of no bulbs in the area?
while True:
    data = broadcast_socket.recvfrom(41)
    try:
        data = pylifx.packet.decode(data[0])
        if data[0] == 'panGateway':
            print(data[1]['bulb_addr'])
            break
    except Exception as e:
        pass
