import pytest
from src.list_prime import list_prime
from unittest.mock import patch
import os

@pytest.mark.parametrize(
    "a, exprected_result",  
    [
        (2, [2]), 
        (10, [2, 3, 5, 7]),  
        (20,  [2, 3, 5, 7, 11, 13, 17, 19]),
    ],
)
def test_functionThatCallOther(a, exprected_result):
    assert (
        list_prime(a) == exprected_result
    )

