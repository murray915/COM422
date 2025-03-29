import pytest
from test_fixtures import *
from tornado import Tornado

###### Tornado Tests ######
# -- classification function --
@pytest.mark.parametrize('name, wind_speed, expected_result', 
                         [("test_1",40,"F0"),
                          ("test_2",72,"F0"),
                          ("test_3",73,"F1"),
                          ("test_4",112,"F1"),
                          ("test_5",113,"F2"),
                          ("test_6",157,"F2"),
                          ("test_7",158,"F3"),
                          ("test_8",205,"F3"),
                          ("test_9",206,"F4"),  
                          ("test_10",260,"F4"),
                          ("test_11",261,"F5"),
                          ("test_12",39,"Unclassified"),
                          ("test_13",0,"Unclassified"),
                          ("test_14",-10,"Unclassified")
                          ])
def test_tornado_calculate_classification(name, wind_speed, expected_result, Test_Tor):    
    """ Run for all top/bottom values for storm cat """
    Test_Tor.name = name
    Test_Tor.wind_speed = wind_speed

    output = Test_Tor.calculate_classification()

    assert output == expected_result

# -- advice function --
def test_tornado_get_advice_classification_1(F0, F1):
    """ F0, F1 >> Clasification 1 """
    expected_result = "Find safe room/shelter, shield yourself from debris"
    output_list = []

    output_list.append(F0.get_advice())
    output_list.append(F1.get_advice())
    
    for i in output_list:
        assert i == expected_result

def test_tornado_get_advice_classification_2(F2, F3, F4, F5):
    """ F2, F3, F4, F5 >> Clasification 2 """
    expected_result = "Find underground shelter, crouch near to the floor covering your head with your hands"
    output_list = []

    output_list.append(F2.get_advice())
    output_list.append(F3.get_advice())
    output_list.append(F4.get_advice())
    output_list.append(F5.get_advice())

    for i in output_list:
        assert i == expected_result

def test_tornado_get_advice_classification_3(Test_Tor, Unclassified):
    """ Everything else >> Clasification 3 """
    expected_result = "There is no need to panic"
    output_list = []

    output_list.append(Test_Tor.get_advice())
    output_list.append(Unclassified.get_advice())

    for i in output_list:
        assert i == expected_result
