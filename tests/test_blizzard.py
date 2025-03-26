import pytest
import blizzard

def setup_function(function):
    global Blizzard
    global Severe_Blizzard
    global Snow_Storm   

    Blizzard = blizzard("Blizzard",35,0)
    Severe_Blizzard = blizzard("Severe_Blizzard",45,-12)
    Snow_Storm = blizzard("Snow_Storm",0,0)

    
def teardown_function(function):
    pass
    
def setup_module(module):
    pass
    
def teardown_module(module):
    pass



def test_snow_storm_classification():
    classification = Snow_Storm.calculate_classification()
    assert classification == "Snow Storm"