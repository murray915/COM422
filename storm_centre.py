from Storm import Storm
from tornado import Tornado
from blizzard import Blizzard


class StormCentre:
    def __init__(self):
        self.storm_list = []

    def add_storm(self, storm: Storm) -> bool:
        if len(self.storm_list) <= 20 and not self.already_exists(storm.name) and ((storm, Tornado) or
                                                                                  isinstance(storm, Blizzard)):
            self.storm_list.append(storm)
            return True
        return False

    def remove_storm(self, name: str) -> bool:
        for storm in self.storm_list:
            if name == storm.name:
                self.storm_list.remove(storm)
                return False
        return True

    def view_storm(self, name: str) -> Storm or None:
        for storm in self.storm_list:
            if storm.name == name:
                return storm
        return None

    def update_storm(self, name, values) -> bool:
        if isinstance(values, dict):
            for storm in self.storm_list:
                if storm.name == name:
                    storm.wind_speed = values["windspeed"]
                    return True
        else:
            raise Exception("Values must be provided as a dictionary")
        return False

    def already_exists(self, name) -> bool:
        for storm in self.storm_list:
            if storm.name == name:
                return True
        return False
