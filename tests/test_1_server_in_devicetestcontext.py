# -*- coding: utf-8 -*-
"""
Some simple unit tests of the AndrewDev device, exercising the device from
the same host as the tests by using a DeviceTestContext.
"""
from tango import DevState
from tango.test_utils import DeviceTestContext

from andrewdev.andrewdev import AndrewDev

def test_init():
    """Test device goes into STANDBY when initialised"""
    with DeviceTestContext(AndrewDev, process=True) as proxy:
        proxy.Init()
        assert proxy.state() == DevState.STANDBY


def test_turn_on():
    """Test device turns on when requested"""
    with DeviceTestContext(AndrewDev, process=True) as proxy:
        proxy.Init()
        assert proxy.state() != DevState.ON
        proxy.current = 5.0
        proxy.turn_on()
        assert proxy.state() == DevState.ON


def test_turn_off():
    """Test device turns off when requested"""
    with DeviceTestContext(AndrewDev, process=True) as proxy:
        proxy.Init()
        assert proxy.state() != DevState.OFF
        proxy.turn_off()
        assert proxy.state() == DevState.OFF


def test_current_is_zero_at_init():
    """Test device sets current to 0 when initialised"""
    with DeviceTestContext(AndrewDev, process=True) as proxy:
        proxy.Init()
        proxy.current = 5
        assert proxy.current != 0
        proxy.Init()
        assert proxy.current == 0

def test_voltage_is_240():
    """Test device has hard-coded voltage of 240"""
    with DeviceTestContext(AndrewDev, process=True) as proxy:
        proxy.Init()
        assert proxy.voltage == 240

def test_set_current():
    """Test device sets current on request"""
    with DeviceTestContext(AndrewDev, process=True) as proxy:
        proxy.current = 5.0
        assert proxy.current == 5.0
        proxy.current = 3.0
        assert proxy.current == 3.0

def test_temperature_is_200_at_init():
    """Test device sets temperature to 200 when initialised"""
    with DeviceTestContext(AndrewDev, process=True) as proxy:
        proxy.Init()
        # TODO use scale factor reported by object, not the hard-coded 10
        # we scale and round here because the object simulates noise
        assert round(proxy.temperature/10) == 20
