from functions import createCypher

def test_cypher_basic():
    caesar3 = createCypher(3)
    assert caesar3("ZigZag") == "BLJBDJ"

def test_cypher_negative_displacement():
    caesar_minus2 = createCypher(-2)
    assert caesar_minus2("ALOHAMORA") == "ZJNFZKNPZ"

def test_cypher_spaces():
    caesar3 = createCypher(3)
    assert caesar3("Pancho Villa") == "SDPFKRCYLÑÑD"

if __name__ == "__main__":
    import pytest
    pytest.main()
