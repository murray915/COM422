import pytest
from hurricane import Hurricane

def setup_function(function):
    global Cat_1 
    global Cat_2
    global Cat_3
    global Cat_4
    global Cat_5
    global Cat_5
    global Top_Stor
    global Test_hurr

    # Within boundary Hurricane Classifications
    Cat_1 = Hurricane("Cat_1",95)
    Cat_2 = Hurricane("Cat_2",110)
    Cat_3 = Hurricane("Cat_3",129)
    Cat_4 = Hurricane("Cat_4",156)
    Cat_5 = Hurricane("Cat_5",157)
    Top_Stor = Hurricane("Top_Stor",5)
    Test_hurr = Hurricane("Top_Stor",0)

def teardown_function(function):
    pass
    
def setup_module(module):
    pass

def teardown_module(module):
    pass 

###### Hurricane Tests ######

# -- classification function --
@pytest.mark.parametrize('name, wind_speed, expected_result', 
                         [("test_1",74,"Category one"),
                          ("test_2",95,"Category one"),
                          ("test_3",96,"Category two"),
                          ("test_4",110,"Category two"),
                          ("test_5",111,"Category three"),
                          ("test_6",129,"Category three"),
                          ("test_7",130,"Category four"),
                          ("test_8",156,"Category four"),
                          ("test_9",157,"Category five"),
                          ("test_10",73,"Tropical Storm"),
                          ("test_11",0,"Tropical Storm"),
                          ("test_12",-10,"Tropical Storm")
                          ])
def test_hurricane_calculate_classification(name, wind_speed, expected_result):    
    """ Run for all top/bottom values for storm cat """
    
    Test_hurr.name = name
    Test_hurr.wind_speed = wind_speed

    output = Test_hurr.calculate_classification()

    assert output == expected_result

# -- advice function --
def test_hurricane_get_advice_classification_1():
    """ Cat 1 / 2 and Topical Storm return Cat 1 """
    expected_result = "Close storm shutters and stay away from windows"
    output_list = []

    output_list.append(Cat_1.get_advice())
    output_list.append(Cat_2.get_advice())
    output_list.append(Top_Stor.get_advice())

    for i in output_list:
        assert i == expected_result

def test_hurricane_get_advice_classification_2():
    """ Cat 3 only return Cat 2 """
    expected_result = "Coastal regions are encouraged to evacuate"

    output = Cat_3.get_advice()

    assert output == expected_result

def test_hurricane_get_advice_classification_3():
    """ Cat 4 / 5 return Cat 3 """
    expected_result = "Evacuate"
    output_list = []

    output_list.append(Cat_4.get_advice())
    output_list.append(Cat_5.get_advice())

    for i in output_list:
        assert i == expected_result