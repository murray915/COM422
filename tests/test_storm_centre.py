import pytest
from test_fixtures import *
from storm_centre import StormCentre
from Storm import Storm

# -- classification function --
@pytest.mark.parametrize('add_list_num, storm_nam, expected_result', 
                         [(20,"Test-1",True),
                          (10,"Test-2",True),
                          (21,"Test-3",False),
                          (100,"Test-4",False)
                          ])
def test_stormcentre_add_list(add_list_num, storm_nam, expected_result, bliz, centre_exp):    
    """ Add to storm list capacity test """

    for i in range(0,add_list_num -1):
        storm_obj = Blizzard((storm_nam + '-' + str(i)),0,0) 
        centre_exp.add_storm(storm_obj)
        
    output = centre_exp.add_storm(bliz)
    assert output == expected_result


def test_reject_storm_false_storm_class(centre_exp):
    """ Add false storm class into List """ 

    class SunnyDay(Storm):
        def __init__(self, name, wind_speed):
            super().__init__(name, wind_speed)   

        def calculate_classification(self) -> str:
            return "Blinding day"

        def get_advice(self) -> str:
            return "Sunny"

    obj = SunnyDay('Test',100)
    assert centre_exp.add_storm(obj) == False


def test_add_all_storm_classes_into_list(F0, Cat_1, bliz, centre_exp):
    """ Add all list types to list. All return ture """ 
    output_list = []

    output_list.append((centre_exp.add_storm(bliz), bliz.name))
    output_list.append((centre_exp.add_storm(F0), F0.name))
    output_list.append((centre_exp.add_storm(Cat_1), Cat_1.name))    

    for i in range(len(output_list)):
        print(output_list[i][1], output_list[i][0])
        assert output_list[i][0] == True


def test_add_all_storm_classes_into_list(bliz, Cat_1, centre_exp):
    """ Add two different types of storm, with same name, expect false""" 

    centre_exp.add_storm(bliz)
    Cat_1.name = "bliz"
    output = centre_exp.add_storm(Cat_1)

    assert output == False


def test_add_remove_storm_into_list_negative_test(bliz, F2, F1, centre_exp):
    """ Add storm, and remove non-input storm. False expected return as nothing removed """ 
    
    centre_exp.add_storm(bliz)
    centre_exp.add_storm(F2)
    output = centre_exp.remove_storm(F1.name)

    assert output == False    


def test_add_storms_into_list_enmass(F4, Cat_3, F2, centre_exp):
    """ Add all list of storms to list. All moved, return true """
    output_list_add = []
    output_list_remove = []

    output_list_add.append(centre_exp.add_storm(F2))
    output_list_add.append(centre_exp.add_storm(F4))
    output_list_add.append(centre_exp.add_storm(Cat_3))

    output_list_remove.append((centre_exp.remove_storm(F2.name), F2.name))
    output_list_remove.append((centre_exp.remove_storm(F4.name), F4.name))
    output_list_remove.append((centre_exp.remove_storm(Cat_3.name), Cat_3.name))  

    for i in range(len(output_list_remove)):       
        print(output_list_remove[i][1], output_list_remove[i][0])
        assert output_list_remove[i][0] == True


def test_add_and_view_storms_inc_negative_test(bliz, Cat_1, centre_exp):
    """ Add storm, and view storm not added. None expected return as nothing removed """     
    centre_exp.add_storm(bliz)
    output = centre_exp.view_storm(Cat_1.name)
    output_1 = centre_exp.view_storm(bliz.name)
    
    assert output == None
    assert output_1 == bliz


def test_add_and_update_storm(bliz, centre_exp):
    """ Add storm, update wind_speed to 100. View storm to confirm update was successful """     
    centre_exp.add_storm(bliz)
    centre_exp.update_storm(bliz.name, {"name": "Bliz", "wind_speed":  100, "temp": 0})
    
    output = centre_exp.view_storm(bliz.name)

    assert output.wind_speed == 100


def test_add_and_update_storm_non_dictionary_input(bliz, centre_exp):
    """ Add storm, update wind_speed to 100. Input passed non-dictionary. Exceptions Expected """     
    
    with pytest.raises(Exception, match="Values must be provided as a dictionary"):        
        centre_exp.add_storm(bliz)
        centre_exp.update_storm(bliz.name, 100)


def test_add_and_update_storm_not_within_list(bliz, Cat_1, centre_exp):
    """ Add storm, update wind_speed to 100 for storm not within list. Expected False returned (control inc bliz update = true)"""     
    centre_exp.add_storm(bliz)
    output_cat = centre_exp.update_storm(Cat_1.name, {"name": "Bliz", "wind_speed":  100})
    output_bliz = centre_exp.update_storm(bliz.name, {"name": "Bliz", "wind_speed":  100})

    assert output_cat == False
    assert output_bliz == True