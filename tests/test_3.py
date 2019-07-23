# -*- coding: utf-8 -*-
"""
*** THIS TEST METHOD IS NOT COMPATIBLE WITH POGO CODE! ***

This file doesn't spawn a new process, thus coverage is actually tracked properly!
"""
#from tango import DevState
#from tango.test_utils import DeviceTestContext
#
#from AndrewDevPogo.AndrewDevPogo import AndrewDevPogo
#
#def test_stuff():
#    """Test a few things in this thread for coverage tracker"""
#    with DeviceTestContext(AndrewDevPogo, process=False) as proxy:
#        proxy.Init()
#        assert proxy.current == 0
#        scale = float(proxy.attribute_query('temperature').display_unit)
#        assert round(proxy.temperature * scale) == 20
#        assert proxy.state() == DevState.STANDBY
#        proxy.current = 4
#        assert proxy.current == 0
#        assert round(proxy.temperature * scale) == 20
#        proxy.turn_on()
#        assert proxy.current == 4
#        assert round(proxy.temperature * scale) == 36
#        proxy.ramp(3)
#        assert proxy.current == 3
#        # note, need current to be set in range to avoid alarm
#        assert proxy.state() == DevState.ON
#        proxy.turn_off()
#        assert proxy.state() == DevState.OFF
#        assert proxy.voltage == 240
