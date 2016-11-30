import re

class Cliente(object):
    def __init__(self, id, nombre, email, facturado, localidad):
        self.id = id
        self.nombre = re.sub('[0-9a-zA-Z]', 'X', nombre)
        self.email = re.sub('[0-9a-zA-Z ]', 'X', email)
        self.facturado = re.sub('[ ]', '0', facturado)
        self.localidad = localidad