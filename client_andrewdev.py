#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import sqrt

import tango
from tango import DevState


def format_attr(a):
    """Given the name of an attribute, format its value for display"""
    # AttributeInfo contains current value
    attr = dev.read_attribute(a)
    # AttributeInfoEx contains full configuration
    attr_ex = dev.attribute_query(a) 

    # TODO - it would be better to check for numeric types, but this works for now
    try:
        scaled = attr.value * float(attr_ex.display_unit)
    except:
        scaled = attr.value

    f = attr_ex.format
    # remove leading % symbol if present, ignore format if not.
    if '%' == f[0]:
        f = f[1:] 
    else:
        f = ""

    return "{:{fmt}} {unit}".format(scaled, fmt=f, unit=attr_ex.unit)


path = "a/b/c"
dev = tango.DeviceProxy(path)

print("Atrributes:")
for attr in dev.attribute_list_query():
    print("{:20}{:40}{:20}".format(attr.name, attr.description, format_attr(attr.name)))
print("")

if dev.state() in [DevState.STANDBY, DevState.OFF]:
    print("Turning on device via turn_on command")
    dev.turn_on()

new_current = sqrt(7)
print("Setting current to {:.3f}".format(new_current))
dev.current = new_current

# scale temperature and display as per attribute configuration
#attr_t = dev.read_attribute("temperature") # this returns an AttributeInfo, which does not hold the full config
#attr_conf = dev.attribute_query("temperature")
#
#t = attr_t.value * float(attr_conf.display_unit)
#f = attr_conf.format
#if '%' == f[0]:
#    f = f[1:] # remove leading % symbol
#else:
#    f = ""
#print("Device temperature is {:{fmt}} {unit}".format(t, fmt=f, unit=attr_conf.unit))

print("Temperature: {}".format(format_attr("temperature")))
print("")


print("Re-initialising")
dev.init()

print("Temperature: {}".format(format_attr("temperature")))
print("")
