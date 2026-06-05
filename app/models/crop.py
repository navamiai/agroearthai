"""
Crop model for AgroEarth AI.
"""

class Crop:
    """
    Represents a crop grown on a farm.
    """
    def __init__(self, name: str, growth_stage: int, water_requirement: float) -> None:
        self.name=name
        self.growth_stage=growth_stage
        self.water_requirement=water_requirement
    
    def get_info(self) -> str:
        return (f"Crop: {self.name},"
                f" Stage: {self.growth_stage},"
                f" Water Requirement: {self.water_requirement} L/day"    
        )  
    
