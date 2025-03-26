import pytest
from blizzard import Blizzard

def setup_function(function):
    pass
    
def teardown_function(function):
    pass
    
def setup_module(module):
    global bliz 
    global Sev_bliz
    global sno_stor

    bliz = Blizzard("Blizzard",35,0)
    Sev_bliz = Blizzard("Severe_Blizzard",45,-12)
    sno_stor = Blizzard("Snow_Storm",0,0)
    

def teardown_module(module):
    pass 


###### Blizzard Tests ######

# -- classification function --
@pytest.mark.parametrize('name, wind_speed, temp, expected_result', 
                         [("test_1",35,0,"Blizzard"),
                          ("test_2",44,0,"Blizzard"),
                          ("test_3",45,0,"Blizzard"),
                          ("test_4",40,-12,"Blizzard"),
                          ("test_5",45,-12,"Severe Blizzard"),
                          ("test_6",50,-20,"Severe Blizzard"),
                          ("test_7",30,-20,"Snow Storm"),
                          ("test_8",0,0,"Snow Storm")
                          ])

def test_blizzard_calculate_classification(name, wind_speed, temp, expected_result):    
    
    bliz.name = name
    bliz.wind_speed = wind_speed
    bliz.temp = temp

    output = bliz.calculate_classification()

    assert output == expected_result


# -- advice function --
@pytest.mark.parametrize('name, wind_speed, temp, expected_result', 
                         [("Blizzard",35,0,"Keep warm, Do not travel unless absolutely essential."),
                          ("Severe_Blizzard",45,-12,"Keep warm, avoid all travel."),
                          ("Snow Storm",0,0,"Take care and avoid travel if possible."),
                          ])

def test_blizzard_get_advice(name, wind_speed, temp, expected_result):
    output = Blizzard(name, wind_speed, temp).get_advice()

    assert output == expected_result