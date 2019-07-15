# -*- coding: utf-8 -*-
"""
This file doesn't spawn a new process, thus coverage is actually tracked properly!
"""
from tango import DevState
from tango.test_utils import DeviceTestContext

from andrewdev.andrewdev import AndrewDev

def test_stuff():
    """Test a few things in this thread for coverage tracker"""
    with DeviceTestContext(AndrewDev, process=False) as proxy:
        proxy.Init()
        assert proxy.current == 0
        assert round(proxy.temperature/10) == 20
        assert proxy.state() == DevState.STANDBY
        proxy.current = 4
        assert proxy.current == 4
        # note, need current to be set in range to avoid alarm
        proxy.turn_on()
        assert proxy.state() == DevState.ON 
        proxy.turn_off()
        assert proxy.state() == DevState.OFF 
        assert proxy.voltage == 240
