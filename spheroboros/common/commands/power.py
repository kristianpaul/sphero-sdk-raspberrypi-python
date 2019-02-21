#!/usr/bin/env python3
# This file is automatically generated!
# Source File:        0x13-power.json
# Device ID:          0x13
# Device Name:        power
# Timestamp:          02/21/2019 @ 22:23:44.205597 (UTC)

from enum import IntEnum


__all__ = ['BatteryVoltageAndStateStatesEnum',
           'BatteryVoltageStatesEnum',
           'ChargerStatesEnum',
           'PowerOptionsBitMask']


class CommandsEnum(IntEnum):
    enter_deep_sleep = 0x00
    enter_soft_sleep = 0x01
    wake = 0x0D
    get_battery_percentage = 0x10
    get_battery_voltage_state = 0x17
    will_sleep_notify = 0x19
    did_sleep_notify = 0x1A
    enable_battery_voltage_state_change_notify = 0x1B
    battery_voltage_state_change_notify = 0x1C


class BatteryVoltageAndStateStatesEnum(IntEnum):
    ''' '''
    charged = 0  #: 
    charging = 1  #: 
    not_charging = 2  #: 
    ok = 3  #: 
    low = 4  #: 
    critical = 5  #: 
    reserved = 6  #: 
    unused = 7  #: 


class BatteryVoltageStatesEnum(IntEnum):
    ''' '''
    unknown = 0  #: 
    ok = 1  #: 
    low = 2  #: 
    critical = 3  #: 


class ChargerStatesEnum(IntEnum):
    ''' '''
    unknown = 0  #: 
    not_charging = 1  #: 
    charging = 2  #: 
    charged = 3  #: 


class PowerOptionsBitMask(IntEnum):
    ''' '''
    sleep_while_charging = 1 #: 
    double_tap_to_wake = 2 #: 
