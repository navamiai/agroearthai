"""
Abstract sensor definition for AgroEarth AI.
"""
from abc import ABC, abstractmethod

class Sensor(ABC):
    """
    Base class for all sensors
    """
    def __init__(self, sensor_id: int, name: str) -> None:
        self.sensor_id = sensor_id
        self.name = name
     
    @abstractmethod
    def read(self) -> float:
        """
        Read data from the sensor
        """
        pass