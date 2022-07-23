''' test_string_builder.py'''
import pytest
from string_builder import StringBuilder

def test_creation():
    a_s_builder = StringBuilder()
    assert a_s_builder is not None

def test_add():
    a_s_builder = StringBuilder()
    a_s_builder.add("la chaucha")
    a_s_builder.add(" esta renga")

    assert a_s_builder.toString() == "la chaucha esta renga"
    