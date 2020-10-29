import pytest
import Piskvorky_rozdelene as pr


def test_vyhodnot_o():
    assert pr.vyhodnot("--------ooo---------") == "o"
    
def test_vyhodnot_x():
    assert pr.vyhodnot("--------xxx---------") == "x"

def test_vyhodnot_remiza():
    assert pr.vyhodnot("xoxoxoxoxoxoxoxoxoxo") == "!"


def test_tah():
    assert pr.util.tah("--------------------", 0, "x") == "x-------------------"
    assert pr.util.tah("--------------------", 0, "o") == "o-------------------"
    
    
def test_symbol_pocitace_x():

    pole = 20*"-"
    symbol_pocitace = "x"
    x = pr.ai.tah_pocitace(pole,symbol_pocitace)
    print(x)
    assert len(x) == 20
    assert x.count("x") == 1
    assert x.count("-") == 19

def test_symbol_pocitace_o():

    pole = 20*"-"
    symbol_pocitace = "o"
    x = pr.ai.tah_pocitace(pole,symbol_pocitace)
    assert len(x) == 20
    assert x.count("-") == 19
    assert x.count("o") == 1
    
def test_delka_10():

    pole = 10*"-"
    symbol_pocitace = "o"
    x = pr.ai.tah_pocitace(pole,symbol_pocitace)
    assert len(x) == 10
    assert x.count("-") == 9
    assert x.count("o") == 1


def test_delka_pole_0():

    pole = ""
    symbol_pocitace = "x"
    with pytest.raises(IndexError):
        pr.ai.tah_pocitace(pole,symbol_pocitace)

