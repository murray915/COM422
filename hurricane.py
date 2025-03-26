from Storm import Storm


class Hurricane(Storm):
    def __init__(self, name, wind_speed):
        super().__init__(name, wind_speed)

    def calculate_classification(self) -> str:
        if self.wind_speed <= 74 and self.wind_speed<= 95:
            return "Category one"
        elif self.wind_speed >= 96 and self.wind_speed<= 110:
            return "Category two"
        elif self.wind_speed >= 111 and self.wind_speed<= 129:
            return "Category three"
        elif self.wind_speed >= 130 and self.wind_speed <= 156:
            return "Category four"
        elif self.wind_speed > 156:
            return "Category five"
        return "Unclassified"

    def get_advice(self) -> str:
        classification = self.calculate_classification()

        if classification == "Tropical Storm" or classification == "Category one" or classification == "Category two":
            return "Close storm shutters and stay away from windows"
        elif classification == "Category three":
            return "Coastal regions are encouraged to evacuate"
        return "Evacuate"
