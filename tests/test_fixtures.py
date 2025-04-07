import pytest
from tornado import Tornado
from hurricane import Hurricane
from blizzard import Blizzard
from storm_centre import StormCentre

##### Storm Centre(s) #####
@pytest.fixture
def centre_exp():
    obj = StormCentre()
    return obj


##### Blizzard #####
@pytest.fixture
def bliz():
    obj = Blizzard("bliz",35,0)
    return obj

@pytest.fixture
def Sev_bliz():
    obj = Blizzard("Severe_Blizzard",45,-12)
    return obj

@pytest.fixture
def sno_stor():
    obj = Blizzard("Snow_Storm",0,0)
    return obj


##### Hurricane #####
@pytest.fixture
def Cat_1():
    obj = Hurricane("Cat_1",95)
    return obj

@pytest.fixture
def Cat_2():
    obj = Hurricane("Cat_1",95)
    return obj

@pytest.fixture
def Cat_3():
    obj = Hurricane("Cat_3",129)
    return obj

@pytest.fixture
def Cat_4():
    obj = Hurricane("Cat_4",156)
    return obj

@pytest.fixture
def Cat_5():
    obj = Hurricane("Cat_5",157)
    return obj

@pytest.fixture
def Top_Stor():
    obj = Hurricane("Top_Stor",5)
    return obj

@pytest.fixture
def Test_hurr():
    obj = Hurricane("Top_Stor",0)
    return obj


##### Tornado #####
@pytest.fixture
def F0():
    obj = Tornado("F0",72)
    return obj

@pytest.fixture
def F1():
    obj = Tornado("F1",112)
    return obj

@pytest.fixture
def F2():
    obj = Tornado("F2",157)
    return obj

@pytest.fixture
def F3():
    obj = Tornado("F3",205)
    return obj

@pytest.fixture
def F4():
    obj = Tornado("F4",260)
    return obj

@pytest.fixture
def F5():
    obj = Tornado("F5",261)
    return obj

@pytest.fixture
def Unclassified():
    obj = Tornado("Unclassified",0)   
    return obj

@pytest.fixture
def Test_Tor():
    obj = Tornado("Test_Tor",0)
    return obj