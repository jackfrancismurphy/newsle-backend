# pytest newdle_api.py  
import pytest 

# function I expect to write in newdle_api:

def test_headline_empty(headline):
    assert headline != ""

def test_sheadline(scrambled_headline):
    assert "  " not in scrambled_headline

def test_difference(headline, scrambled_headline):
    assert headline != scrambled_headline

