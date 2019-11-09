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

sensor = sensor_args[int(__settings__.getSetting('model'), base=10)]
pin = int(__settings__.getSetting('pin'), base=10)
time = int(__settings__.getSetting('time')) * 1000

# Example using a Beaglebone Black with DHT sensor
# connected to pin P8_11.
#pin = 'P8_11'

# Example using a Raspberry Pi with DHT sensor
# connected to GPIO24.
#pin = 24

# Try to grab a sensor reading.  Use the read_retry method which will retry up
# to 15 times to get a sensor reading (waiting 2 seconds between each retry).
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

# Note that sometimes you won't get a reading and
# the results will be null (because Linux can't
# guarantee the timing of calls to read the sensor).
# If this happens try again!

if humidity is not None and temperature is not None:
    line1 = 'Temp: {0:0.1f}°C '.format(temperature) + __settings__.getLocalizedString(32014) + ': {0:0.1f}%rLF'.format(humidity)

else:
    line1 = __settings__.getLocalizedString(32015)

#line1 = "This is a simple example of notifications"
#time = 8000 #in miliseconds

xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%(__addonname__,line1, time, __icon__))
