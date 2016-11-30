clientes = []

class GestorClientes:

    @classmethod
    def add_cliente(cls, c):
        clientes.append(c)

    @classmethod
    def devolver_clientes(cls):
        suma = 0.0

        for cliente in clientes:
            suma += float(cliente.facturado)

        promedio = suma / clientes.__len__()

        for cliente in clientes:
            cliente.facturado = promedio

        return clientes

