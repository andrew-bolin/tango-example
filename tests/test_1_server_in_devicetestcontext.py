# -*- coding: utf-8 -*-
"""
*** THIS TEST METHOD IS NOT COMPATIBLE WITH THE POGO-GENERATED CODE ***
    (at least not without a lot more work than seems reasonable)


Some simple unit tests of the AndrewDevPogo device, exercising the device from
the same host as the tests by using a DeviceTestContext.
"""
#from tango import DevState
#from tango.test_utils import DeviceTestContext
#
#from AndrewDevPogo.AndrewDevPogo import AndrewDevPogo
#
#def test_init():
#    """Test device goes into STANDBY when initialised"""
#    with DeviceTestContext(AndrewDevPogo, process=True) as proxy:
#        proxy.Init()
#        assert proxy.state() == DevState.STANDBY
#
#
#def test_turn_on():
#    """Test device turns on when requested"""
#    with DeviceTestContext(AndrewDevPogo, process=True) as proxy:
#        proxy.Init()
#        assert proxy.state() != DevState.ON
#        proxy.current = 5.0
#        proxy.turn_on()
#        assert proxy.state() == DevState.ON
#
#
#def test_turn_off():
#    """Test device turns off when requested"""
#    with DeviceTestContext(AndrewDevPogo, process=True) as proxy:
#        proxy.Init()
#        assert proxy.state() != DevState.OFF
#        proxy.turn_off()
#        assert proxy.state() == DevState.OFF
#
#
#def test_current_is_zero_at_init():
#    """Test device sets current to 0 when initialised"""
#    with DeviceTestContext(AndrewDevPogo, process=True) as proxy:
#        proxy.Init()
#        proxy.turn_on()
#        proxy.current = 5
#        assert proxy.current != 0
#        proxy.Init()
#        assert proxy.current == 0
#
#def test_voltage_is_240():
#    """Test device has hard-coded voltage of 240"""
#    with DeviceTestContext(AndrewDevPogo, process=True) as proxy:
#        proxy.Init()
#        assert proxy.voltage == 240
#
#def test_set_current():
#    """Test device sets current when turned on"""
#    with DeviceTestContext(AndrewDevPogo, process=True) as proxy:
#        proxy.Init()
#        proxy.current = 5.0
#        assert proxy.current == 0
#        proxy.turn_on()
#        assert proxy.current == 5.0
#        proxy.current = 3.0
#        assert proxy.current == 3.0
#
#def test_temperature_is_200_at_init():
#    """Test device sets temperature to 200 when initialised"""
#    with DeviceTestContext(AndrewDevPogo, process=True) as proxy:
#        proxy.Init()
#        scale = float(proxy.attribute_query('temperature').display_unit)
#        # we scale and round here because the object simulates noise
#        assert round(proxy.temperature * scale) == 20
