class Auto:
    def __init__(self,marca,modello,serbatoio):
        self.marca = marca
        self.modello = modello
        self.serbatoio = serbatoio

    def rifornimento(self,litri):
        self.serbatoio += litri