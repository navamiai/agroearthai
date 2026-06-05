"""
Main entry point for AgroEarth AI.
"""

#print("AgroEarth AI initialized.")

from models.crop import Crop
from models.soil import Soil
from models.farm import Farm

def main_entry() -> None:
    crop = Crop(
        name="Rice", growth_stage="Vegetative",
        water_requirement=25.0
               )
    soil = Soil(
        soil_type="Clay",
        moisture=48.5,
        ph=6.8
    )
    farm = Farm(
        farm_id=1, name= "Green Valley Farm",
        location="Kochi", crop=crop,
        soil=soil
    )
    farm.display_status()

if __name__=="__main__":
    main_entry()