"""
Testing for the math.py module.
"""
import project07 as fcm
import pytest


def test_add():
    assert fcm.math.add(5,2) == 7
    assert fcm.math.add(2,5) == 7

def test_mult():
    assert fcm.math.mult(5,2) == 10
    assert fcm.math.mult(2,5) == 10

def test_div():
    assert fcm.math.div(8,2) == 4
    assert fcm.math.div(10,2) == 5
    
