import divisibility
import pytest

@pytest.mark.parametrize("num,output",[(5,True),(2,False),(10,True),(7,False)])
def test_div5_1(num, output):
    # x=10
    r=divisibility.divisibleby5(num)
    assert r == output

@pytest.mark.parametrize("num,output",[(7,True),(2,False),(35,True),(5,False)])
def test_div7_1(num, output):
    # x=14
    r=divisibility.divisibleby7(num)
    assert r == output

@pytest.mark.parametrize("num,output",[(18,True),(2,False),(9,True),(7,False)])
def test_div9_1(num, output):
    # x=27
    r=divisibility.divisibleby9(num)
    assert r == output

@pytest.mark.parametrize("num,output",[(22,True),(2,False),(99,True),(7,False)])
def test_div11_1(num, output):
    # x=55
    r=divisibility.divisibleby11(num)
    assert r == output
