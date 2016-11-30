from cliente import Cliente

def test_cliente_masked():
    c = Cliente(1,'Jonatan Nieto', 'aa@aa.com', '15', 'BCN')
    assert c.id == 1
    assert c.nombre == 'XXXXXXX XXXXX'
    assert c.email == 'XX@XX.XXX'
    assert float(c.facturado) == 15
    assert c.localidad == 'BCN'