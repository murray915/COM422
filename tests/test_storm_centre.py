import pytest
from test_fixtures import *
from storm_centre import StormCentre
from Storm import Storm
from blizzard import SunnyDay

# -- classification function --
@pytest.mark.parametrize('add_list_num, storm_nam, expected_result', 
                         [(20,"Test-1",True),
                          (10,"Test-2",True),
                          (21,"Test-3",False),
                          (100,"Test-4",False)
                          ])
def test_stormcentre_add_list(add_list_num, storm_nam, expected_result, bliz):    
    """ Add to storm list capacity test """    
    storm_cen = StormCentre()

    for i in range(0,add_list_num -1):
        storm_obj = Blizzard((storm_nam + '-' + str(i)),0,0) 
        storm_cen.add_storm(storm_obj)
        
    output = storm_cen.add_storm(bliz)
    assert output == expected_result

# def test_stormcentre_add_and_remove_list_negative_test(bliz):    
#     #"" Add & Remove storm list, input false storm name (negative test) ""    
#     storm_cen = StormCentre()

#     storm_cen.add_storm(bliz)
#     output = storm_cen.remove_storm('Remove')

#     assert output == False

# def test_stormcentre_add_and_remove_list(bliz):    
#     """ Add to storm list capacity test """  
#     storm_cen = StormCentre()
#     output_list = []

#     # Add 10 storms to list
#     for i in range(0,9):
#         storm_nam = "Storm_" + str(i)
#         storm_obj = Blizzard((storm_nam + '-' + str(i)),0,0) 
#         storm_cen.add_storm(storm_obj)

#     # Remove 10 storms to list
#     for i in range(0,9):
#         storm_nam = "Storm_" + str(i)
#         output_list.append(storm_cen.remove_storm(storm_nam))

#     for i in range(len(output_list)):
#         assert output_list[i] == True


def test_reject_storm():

    storm_cen = StormCentre()
    obj = SunnyDay('Test',100)

    assert storm_cen.add_storm(obj) == False

