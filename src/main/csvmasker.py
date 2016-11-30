import csv
import sys

from domain.cliente import Cliente
from service.gestorclientes import GestorClientes


def main(path):
    with open(path) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')

        next(csvreader, None)
        for row in csvreader:
            c = Cliente(row[0], row[1], row[2], row[3], row[4])
            GestorClientes.add_cliente(c)

    with open('clientes_masked.csv', 'wb') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(['ID', 'Nombre', 'Email', 'Facturado', 'Localidad'])
        for cliente in GestorClientes.devolver_clientes():
            spamwriter.writerow([cliente.id, cliente.nombre, cliente.email, cliente.facturado, cliente.localidad])

if __name__=='__main__':
    sys.exit(main(sys.argv[1]))