# -*- coding: utf-8 -*-
"""
Some simple unit tests of the AndrewDev device, exercising the device from
another host using a DeviceProxy.
"""
import pytest
import tango


@pytest.fixture
def andrew_dev():
    """Create DeviceProxy for tests"""
    database = tango.Database()
    instance_list = database.get_device_exported_for_class('AndrewDev')
    for instance in instance_list.value_string:
        try:
            return tango.DeviceProxy(instance)
        except tango.DevFailed:
            continue
    pytest.fail('failed to create proxy')


def test_andrew_dev_is_alive(andrew_dev):
    """Sanity check: test device on remote host is responsive"""
    try:
        andrew_dev.ping()
    except tango.ConnectionFailed:
        pytest.fail('Could not contact andrew_dev')


def test_init(andrew_dev):
    """Test device goes into STANDBY when initialised"""
    andrew_dev.Init()
    assert andrew_dev.state() == tango.DevState.STANDBY


def test_turn_on(andrew_dev):
    """Test device turns on when requested"""
    andrew_dev.Init()
    assert andrew_dev.state() != tango.DevState.ON
    andrew_dev.current = 5.0
    andrew_dev.turn_on()
    assert andrew_dev.state() == tango.DevState.ON


def test_turn_off(andrew_dev):
    """Test device turns off when requested"""
    andrew_dev.Init()
    assert andrew_dev.state() != tango.DevState.OFF
    andrew_dev.turn_off()
    assert andrew_dev.state() == tango.DevState.OFF


def test_current_is_zero_at_init(andrew_dev):
    """Test device sets current to 0 when initialised"""
    andrew_dev.current = 5
    assert andrew_dev.current != 0
    andrew_dev.Init()
    assert andrew_dev.current == 0


def test_set_current(andrew_dev):
    """Test device sets current on request"""
    andrew_dev.current = 5.0
    assert andrew_dev.current == 5.0
    andrew_dev.current = 3.0
    assert andrew_dev.current == 3.0

def test_temperature_proportional_to_current(andrew_dev):
    """Tests thermal simulation"""
    andrew_dev.current = 0.0
    for i in range(10):
        assert round(andrew_dev.temperature/10) == 20
    andrew_dev.current = 7.0
    for i in range(10):
        assert round(andrew_dev.temperature/10) == 69
