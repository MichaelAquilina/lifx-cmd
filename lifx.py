# -*- encoding: utf8 -*-
from __future__ import division, print_function, division, absolute_import

import pylifx


def power(bulb, state):
    if state == 'on':
        bulb.on()
    elif state == 'off':
        bulb.off()
    else:
        raise ValueError('Invalid State specified %s' % state)


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('bulb_addr')

    subparsers = parser.add_subparsers(dest='command')

    power_parser = subparsers.add_parser('power')
    power_parser.add_argument('state', choices=('on', 'off'))

    rgb_parser = subparsers.add_parser('rgb')
    rgb_parser.add_argument('red', type=float)
    rgb_parser.add_argument('green', type=float)
    rgb_parser.add_argument('blue', type=float)

    hsb_parser = subparsers.add_parser('hsb')
    hsb_parser.add_argument('hue', type=float)
    hsb_parser.add_argument('saturation', type=float)
    hsb_parser.add_argument('brightness', type=float)

    temp_parser = subparsers.add_parser('temperature')
    temp_parser.add_argument('kelvin', type=int)

    args = parser.parse_args()

    with pylifx.LifxController(args.bulb_addr) as bulb:
        if args.command == 'power':
            power(bulb, args.state)
        elif args.command == 'rgb':
            bulb.set_rgb(args.red, args.green, args.blue)
        elif args.command == 'hsb':
            bulb.set_hsb(args.hue, args.saturation, args.brightness)
        elif args.command == 'temperature':
            bulb.set_temperature(args.kelvin)
