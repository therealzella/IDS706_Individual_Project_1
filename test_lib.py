import pytest
from lib import LibraryClass  

def test_library_class():
    obj = LibraryClass()
    assert obj.method() == expected_value  

