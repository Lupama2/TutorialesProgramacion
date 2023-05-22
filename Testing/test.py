from ejemplo import suma

def test(suma):
    a = 1
    b = 2
    assert suma(a,b) == 3

test(suma)