from Storm import Storm
from tornado import Tornado
from hurricane import Hurricane

class SunnyDay(Storm):
    def __init__(self, name, wind_speed):
        super().__init__(name, wind_speed)   

    def calculate_classification(self) -> str:
        return "Snow Storm"

    def get_advice(self) -> str:
        return "Sunny"


class Blizzard(Storm):
    def __init__(self, name, wind_speed, temp):
        self.temp = temp
        super().__init__(name, wind_speed)

    def calculate_classification(self) -> str:
        if self.wind_speed >= 45 and self.temp <= -12:
            return "Severe Blizzard"
        elif self.wind_speed >= 35:
            return "Blizzard"            
        return "Snow Storm"

    def get_advice(self) -> str:
        classification = self.calculate_classification()

        if classification == "Blizzard":
            return "Keep warm, Do not travel unless absolutely essential."
        elif classification == "Severe Blizzard":
            return "Keep warm, avoid all travel."
        return "Take care and avoid travel if possible."