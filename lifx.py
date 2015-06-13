# -*- encoding: utf8 -*-
from __future__ import division, print_function, division

import pylifx


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('bulb_addr')
    parser.add_argument('state', choices=('on', 'off'))

    args = parser.parse_args()

    with pylifx.LifxController(args.bulb_addr) as bulb:
        if args.state == 'on':
            bulb.on()
        else:
            bulb.off()
