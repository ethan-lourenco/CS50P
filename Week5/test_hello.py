from hello import hello

def test_hello():
    hello("David") == "hello, David"

def test_argument():
    assert hello("David") == "hello, David"