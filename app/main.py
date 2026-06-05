"""
Main entry point for AgroEarth AI.
"""

#print("AgroEarth AI initialized.")

from models.crop import Crop
from models.soil import Soil
from models.farm import Farm

from sensors.temperature_sensor import TemperatureSensor
from sensors.moisture_sensor import MoistureSensor

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
    
    temp_sensor=TemperatureSensor(sensor_id=101,
                                  name="Temperature Sensor"
                                 )
    moisture_sensor=MoistureSensor(sensor_id=102,
                                   name="Moisture Sensor"
                                  )
    print("===== SENSOR READINGS =====")
    print(f"Temperature: {temp_sensor.read()} degC")
    print(f"Moisture: {moisture_sensor.read()} %")
    print("======================================")

if __name__=="__main__":
    main_entry()