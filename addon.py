#!/usr/bin/python
# -*- coding: utf-8 -*-

import xbmc
import xbmcaddon
import Adafruit_DHT

__addon__ = xbmcaddon.Addon()
__addonname__ = __addon__.getAddonInfo('name')
__icon__ = __addon__.getAddonInfo('icon')
__settings__ = xbmcaddon.Addon(id='script.inttemp')
__language__ = __settings__.getLocalizedString


# Sensor should be set to Adafruit_DHT.DHT11,
# Adafruit_DHT.DHT22, or Adafruit_DHT.AM2302.

sensor_args = [
     Adafruit_DHT.DHT11,
     Adafruit_DHT.DHT22,
     Adafruit_DHT.AM2302
]

sensor = sensor_args[__settings__.getSettingInt('model')]
pin = __settings__.getSettingInt('pin')
time = __settings__.getSettingInt('time') * 1000

# Try to grab a sensor reading.  Use the read_retry method which will retry up
# to 15 times to get a sensor reading (waiting 2 seconds between each retry).
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

# Note that sometimes you won't get a reading and
# the results will be null (because Linux can't
# guarantee the timing of calls to read the sensor).
# If this happens try again!

if humidity is not None and temperature is not None:
    line1 = '{0:0.1f}°C / {1:0.1f}%'.format(temperature, humidity)
    line2 = __settings__.getLocalizedString(32016) + ' / ' + __settings__.getLocalizedString(32014)

else:
    line1 = __addonname__
    line2 = __settings__.getLocalizedString(32015)

xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%(line1, line2, time, __icon__))
