import pytest
from person import Person

class TestPerson:

    def test_rest_energy_changes(self):
        p1 = Person("abc", 150, 99, 1)
        print("Person is resting")
        p1.rest()
        assert p1.energy == 2

    def test_rest_hunger_changes(self):
        p1 = Person("abc", 150, 99, 1)
        p1.rest()
        assert p1.hunger == 100

    def test_energy_changes(self):
        p1 = Person("abc", 150, 100, 10)
        p1.run(2)
        assert p1.energy == 6