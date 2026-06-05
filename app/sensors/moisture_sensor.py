"""
Soil moisture sensor implementation
"""

import random
from sensors.sensor import Sensor

class MoistureSensor(Sensor):
    """
    Simulates a moisture sensor
    """
    def read(self) -> float:
        return round(random.uniform(30.0, 80.0), 2)