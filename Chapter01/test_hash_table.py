''' test_hash_table.py '''

import pytest
from hash_table import HashTable

def test_should_create_hashtable():
    assert HashTable(100) is not None

def test_should_report_size():
    assert len(HashTable(100))==100

def test_should_create_empty_value_slots():
    # Given
    expected_values = [None, None, None]
    hash_table = HashTable(size=3)

    # When
    actual_values = hash_table.values

    # Then
    assert actual_values == expected_values

def test_should_insert_values():
    hash_table = HashTable(size=100)

    hash_table.add("hola")
    hash_table.add(98.6)
    hash_table.add(False)

    assert "hola"==hash_table.get("hola")
    assert 98.6==hash_table.get(98.6)
    assert False==hash_table.get(False)

@pytest.mark.skip
def test_should_not_shrink_when_removing_elements():
    pass