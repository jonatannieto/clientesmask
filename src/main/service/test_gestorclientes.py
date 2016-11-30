from gestorclientes import GestorClientes

import sys
sys.path.append("..")
from domain.cliente import Cliente


def test_cliente_promedio():
    c1 = Cliente(1, 'Jonatan Nieto', 'aa@aa.com', '0', 'BCN')
    c2 = Cliente(2, 'Jonatan Nieto', 'aa@aa.com', '30', 'BCN')

    GestorClientes.add_cliente(c1)
    GestorClientes.add_cliente(c2)

    c1 = GestorClientes.devolver_clientes().pop(0)
    assert c1.facturado == 15