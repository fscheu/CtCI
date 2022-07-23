import pytest
from array_list import ArrayList

def test_creation():
    a_list = ArrayList()
    assert a_list is not None

def test_add():
    a_list = ArrayList()
    a_list.add("la chaucha")
    assert a_list.get() == "la chaucha"

def test_add_double_size():
    a_list = ArrayList()
    a_list.add("la chaucha")
    a_list.add(" renga")
    assert a_list.get() == "la chaucha renga"
