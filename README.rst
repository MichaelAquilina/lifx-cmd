===============================
LifX Command Utility
===============================

.. image:: https://img.shields.io/travis/MichaelAquilina/lifx-cmd.svg
        :target: https://travis-ci.org/MichaelAquilina/lifx-cmd

.. image:: https://img.shields.io/pypi/v/lifx-cmd.svg
        :target: https://pypi.python.org/pypi/lifx-cmd


LifX command line utility to change the state of your lifx bulb. Supports powering on/off, changing RGB/HSB color and temperature.

* Free software: BSD license
* Documentation: https://lifx-cmd.readthedocs.org.

Installation
------------

The easiest way to install this utility is using pip:

   pip install lifx-cmd

Alternatively you can install by downloading this github repo and installing it manually:

   git clone https://github.com/MichaelAquilina/lifx-cmd
   cd lifx-cmd
   python setup.py install

Setup
-----

Assuming you've already connected your lifx bulb to your home network, you will now need to specify the bulb you are
communicating with. The easiest way to do this is to add a `.lifx` file to your home directory with the bulb's MAC address:

   echo "03-1F-7B-7B-64-F6" > "~/.lifx"

The command utility will automatically search for this file on execution. Alternatively you can specify the MAC address from
the environment variable LIFXBULB:

   export LIFXBULB="03-1F-7B-7B-64-F6"

Finally, you can simply specify the mac address as a command line parameter:

   lifx --bulb "03-1F-7B-7B-64-F6" power on

Features
--------

Power your bulb on and off:

   $ lifx power on
   $ lifx power off

Change its RGB state:

   $ lifx rgb 1 0 0   # Red light
   $ lifx rgb 0 1 0   # Green light
   $ lifx rgb 0 0 1   # Blue light
   $ lifx rgb 1 0 1   # Magenta light
   etc...

Same approach can be taken with HSB. For example:

   $ lifx hsb 0 1 1

The temperature of the bulb can also be set to yellow tinge or pure white LED:

   $ lifx temperature 65535   # bright white
   $ lifx temperature 0       # classic yellow

By default the bulb is set to fade in changes sent over a period of 1 second. You can change this with the -f flag:

   $ lifx -f 0 rgb 0 1 0           # Immediately change to green
   $ lifx -f 10 temperature 65535  # Change to white over a period of 10 seconds
