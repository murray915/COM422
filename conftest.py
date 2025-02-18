import pytest
from person import Person

@pytest.fixture
def default_person_adult():
    return Person("abc", 150, 50, 1, 18,26)