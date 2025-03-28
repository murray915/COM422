import pytest
from tornado import Tornado
from blizzard import Blizzard
from hurricane import Hurricane
from storm_centre import StormCentre


def setup_function(function):
    global bliz 
    global hurr
    global torr
    global sc

    # Within boundary Bliz Classifications
    bliz = Blizzard("bliz",35,0)
    hurr = Hurricane("hurr",45)
    torr = Tornado("torr",40)
    sc = StormCentre()


def teardown_function(function):
    pass
    
def setup_module(module):
    pass

def teardown_module(module):
    pass 




# -- classification function --
def test_stormcentre_add_list():    
    """ Run for all top/bottom values for storm cat """
    
    sc_01 = StormCentre()

    for i in range(0,9):
        stormnam = 'Storm_' + str(i)
        stormnam = Blizzard(stormnam,0,0)

        sc_01.add_storm(stormnam)
        
    output = sc_01.add_storm(bliz)
    expected_result = True
    sc_01.print()

    assert output == expected_result