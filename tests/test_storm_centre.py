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
def test_stormcentre_add_list(add_list_num, storm_nam, expected_result, bliz):    
    """ Add to storm list capacity test """    
    storm_cen = StormCentre()

    for i in range(0,add_list_num -1):
        storm_obj = Blizzard((storm_nam + '-' + str(i)),0,0) 
        storm_cen.add_storm(storm_obj)
        
    output = storm_cen.add_storm(bliz)
    assert output == expected_result


def test_stormcentre_reject_dup_storms(bliz):
    """ Add same storm name to storm list """
    storm_cen = StormCentre()
    #test_storm = ('bliz',0,0)
    #test_storm_2 = ('can',0)
    test_storm = Hurricane('bliz',0)
    storm_cen.add_storm(test_storm)

    output = storm_cen.add_storm(test_storm)        
    #output = storm_cen.add_storm(test_storm)

    assert output == False
