"""
Soil model for AgroEarth AI.
"""
class Soil:
    def __init__(self, soil_type: str, moisture: float, ph: float) -> None:
        self.soil_type=soil_type
        self.moisture=moisture
        self.ph=ph
    def get_info(self) -> str:
        return (f"Soil Type: {self.soil_type},"
                f" Moisture: {self.moisture}%,"
                f" pH: {self.ph}"
        )