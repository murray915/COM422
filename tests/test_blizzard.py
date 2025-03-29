import pytest
from test_fixtures import * 
from blizzard import Blizzard


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
                          ("test_8",0,0,"Snow Storm"),
                          ("test_8",34,0,"Snow Storm")
                          ])
def test_blizzard_calculate_classification(name, wind_speed, temp, expected_result, bliz):    
    """ Run for all top/bottom values for storm cat """
    
    bliz.name = name
    bliz.wind_speed = wind_speed
    bliz.temp = temp

    output = bliz.calculate_classification()
    assert output == expected_result


# -- advice function --
def test_blizzard_get_advice_bliz(bliz):
    expected_result = "Keep warm, Do not travel unless absolutely essential."
    output = bliz.get_advice()

    assert output == expected_result

def test_blizzard_get_advice_sev_bliz(Sev_bliz):
    expected_result = "Keep warm, avoid all travel."
    output = Sev_bliz.get_advice()

    assert output == expected_result

def test_blizzard_get_advice_sno_stor(sno_stor):
    expected_result = "Take care and avoid travel if possible."
    output = sno_stor.get_advice()

    assert output == expected_result