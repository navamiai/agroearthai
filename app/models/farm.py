"""
Farm model for AgroEarth AI.
"""
from models.crop import Crop
from models.soil import Soil

class Farm:
    """
    Represents a farm and its current state.
    """
    def __init__(self, farm_id:int, name: str, 
                location: str, crop: Crop, soil: Soil) -> None:
        self.farm_id=farm_id
        self.name=name
        self.location=location
        self.crop=crop
        self.soil=soil
        
    def display_status(self) -> None:
        print("\n==== FARM STATUS ====")
        print(f"Farm ID: {self.farm_id}")
        print(f"Farm Name: {self.name}")
        print(f"Location: {self.location}")
        print(self.crop.get_info())
        print(self.soil.get_info())
        print("\n==== =========== ====")