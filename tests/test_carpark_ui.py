import pytest
import os

def setup_function(function):
    if os.path.exists("data/vehicles.json"):
        os.remove("data/vehicles.json")