"""
Temperature sensor implementation
"""

import random
from sensors.sensor import Sensor

class TemperatureSensor(Sensor):
    """
    Simulates a temperature sensor
    """
    def read(self) -> float:
        return round(random.uniform(20.0, 40.0), 2)