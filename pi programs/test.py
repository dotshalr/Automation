import sys
import time

import gpiozero

RELAY_PIN = 2

relay = gpiozero.OutputDevice(RELAY_PIN, active_high=False, initial_value=False)

print("Setting relay: ON")
relay.on()

time.sleep(5)

print("Setting relay: OFF")
relay.off()

print("Success")