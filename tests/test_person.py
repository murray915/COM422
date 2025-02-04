import pytest
import person as Person

class TestPerson:

    def test_rest_energy_changes(self, default_person_adult):
        default_person_adult.rest()
        assert default_person_adult.energy == 2

    def test_rest_hunger_changes(self, default_person_adult):
        default_person_adult.rest()
        assert default_person_adult.hunger == 51

    def test_energy_changes(self, default_person_adult):
        default_person_adult.run(2)
        assert default_person_adult.energy == 1

    @pytest.mark.parametrize('age, age_look, expected_result', [(18,26,True),(17,26,True),(16,20,False)])
    def test_age_look_ranges(self, default_person_adult, age, age_look, expected_result):
        default_person_adult.age = age
        default_person_adult.age_look = age_look

        assert default_person_adult.can_buy_alcohol() == expected_result

