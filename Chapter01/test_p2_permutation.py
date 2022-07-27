''' test_pw_permutation.py '''

import pytest
from p2_permutation import permutation

def test_permutation():
    assert permutation("la chaucha","la cahucha")

def test_no_permutation_empty():
    assert permutation("","a") == False

def test_no_permutation():
    assert permutation("aja","jaj") == False
    