from functions import createCypher

def test_cypher_basic():
    caesar3 = createCypher(3)
    assert caesar3("ZigZag") == "CLJCLJ"

def test_cypher_negative_displacement():
    caesar_minus2 = createCypher(-2)
    assert caesar_minus2("ALOHAMORA") == "YILEYJLOY"

def test_cypher_spaces():
    caesar3 = createCypher(3)
    assert caesar3("Pancho Villa") == "SDQFKRCYLÑÑD"

if __name__ == "__main__":
    import pytest
    pytest.main()