#!/usr/bin/env python, SerialModel
# -*- coding: utf-8 -*-

"""Andrew's experimental tango device server"""

import time
from random import randint
#import numpy
from tango import AttrQuality, AttrWriteType, DispLevel, DevState #, DebugIt  # GreenMode
from tango.server import Device, attribute, command, device_property


class AndrewDev(Device):
    """
    Andrew's hack of example power supply device from the PyTango documentation.
    """
    # green_mode = GreenMode.Asyncio

    voltage = attribute(label="Voltage", dtype=float,
                        display_level=DispLevel.OPERATOR,
                        access=AttrWriteType.READ,
                        unit="V", format="%4.2f",
                        doc="output voltage")

    current = attribute(label="Current", dtype=float,
                        display_level=DispLevel.EXPERT,
                        access=AttrWriteType.READ_WRITE,
                        unit="A", format="%3.2f",
                        min_value=0.0, max_value=8.5,
                        min_alarm=0.1, max_alarm=8.4,
                        min_warning=0.5, max_warning=8.0,
                        abs_change=0.01,
                        fget="get_current",
                        fset="set_current",
                        doc="output current")

    temperature = attribute(label="Temperature", dtype=int,
                            display_level=DispLevel.EXPERT,
                            access=AttrWriteType.READ,
                            unit="degC", format="%3.1f", # '°' symbol displays strangely on GUI?
                            display_unit=0.1, # tells UI to divide by 10
                            abs_change=50,
                            doc="internal temperature")

    host = device_property(dtype=str)
    port = device_property(dtype=int, default_value=9788)

    def __init__(self, device_class, device_name):
        super().__init__(device_class, device_name)
        self.__current = 0.0
        self.__temperature = 200

    def init_device(self):
        """Initialise device"""
        Device.init_device(self)
        self.set_current(0.0)
        self.set_state(DevState.STANDBY)

    def read_voltage(self):
        """Read voltage"""
        self.info_stream("read_voltage(%s, %d)", self.host, self.port)
        return 240, time.time(), AttrQuality.ATTR_VALID

    def get_current(self):
        """Get the current"""
        return self.__current

    def set_current(self, current):
        """Set the current"""
        self.__current = current

    def always_executed_hook(self):
        """Runs before every command"""
        # very coarse thermal loss simulation
        if(self.get_state() in [DevState.STANDBY, DevState.OFF]):
            self.__temperature = 200
        else:
            self.__temperature = 200 + (self.__current**2)*10

    def read_temperature(self):
        """Read internal temperature"""
        return self.__temperature + randint(-4,4)

    def coverage_accuracy_check(self):
        """Not used, just checking if pytest-cov is doing the right thing"""
        return self.__temperature

#    def read_info(self):
#        """Get device information"""
#        return 'Information', dict(manufacturer='Andrew',
#                                   model='PSU001',
#                                   version_number=1)
# ### can't see this anywhere on the GUI - is it used anywhere? ??

    @command
    def turn_on(self):
        """Turn the device on"""
        # turn on the actual power supply here
        self.set_state(DevState.ON)

    @command
    def turn_off(self):
        """Turn the device off"""
        # turn off the actual power supply here
        self.set_state(DevState.OFF)

    @command(dtype_in=float, doc_in="Ramp target current",
             dtype_out=bool, doc_out="True if ramping went well, "
                                     "False otherwise")
    def ramp(self, target_current):
        """Ramp voltage to the target current"""
        # should do the ramping. This doesn't.
        self.set_current(target_current)
        return True


if __name__ == "__main__":
    AndrewDev.run_server()
