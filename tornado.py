from Storm import Storm


class Tornado(Storm):
    def __init__(self, name, wind_speed):
        super().__init__("none", 261)

    def calculate_classification(self) -> str:
        if self.wind_speed <= 40:
            return "Unclassified"
        elif self.wind_speed <= 72:
            return "F0"
        elif self.wind_speed >= 73 and self.wind_speed <= 112:
            return "F1"
        elif self.wind_speed >= 113 and self.wind_speed <= 157:
            return "F2"
        elif self.wind_speed >= 158 and self.wind_speed <= 205:
            return "F3"
        elif self.wind_speed >= 206 and self.wind_speed <= 260:
            return "F4"
        elif self.wind_speed >= 261:
            return "F5"
        return "Unclassified"

    def get_advice(self) -> str:
        classification = self.calculate_classification()

        if classification in ["Unclassified", "F0", "F1"]:
            return "Find safe room/shelter, shield yourself from debris"
        elif classification in ["F2", "F3", "F4" "F5"]:
            return "Find underground shelter, crouch near to the floor covering your head with your hands"
        return "There is no need to panic"
