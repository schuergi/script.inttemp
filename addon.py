#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import xbmc
import xbmcaddon
import Adafruit_DHT

# Sensor should be set to Adafruit_DHT.DHT11,
# Adafruit_DHT.DHT22, or Adafruit_DHT.AM2302.
sensor = Adafruit_DHT.AM2302

# Example using a Beaglebone Black with DHT sensor
# connected to pin P8_11.
#pin = 'P8_11'

# Example using a Raspberry Pi with DHT sensor
# connected to GPIO24.
pin = 24

# Try to grab a sensor reading.  Use the read_retry method which will retry up
# to 15 times to get a sensor reading (waiting 2 seconds between each retry).
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

# Note that sometimes you won't get a reading and
# the results will be null (because Linux can't
# guarantee the timing of calls to read the sensor).
# If this happens try again!

__addon__ = xbmcaddon.Addon()
__addonname__ = __addon__.getAddonInfo('name')
__icon__ = __addon__.getAddonInfo('icon')

if humidity is not None and temperature is not None:
    line1 = 'Temp={0:0.1f}°C  Humidity={1:0.1f}%rLF'.format(temperature, humidity)


else:
    line1 = 'Failed to get reading. Try again!'

#line1 = "This is a simple example of notifications"
time = 5000 #in miliseconds

xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%(__addonname__,line1, time, __icon__))
