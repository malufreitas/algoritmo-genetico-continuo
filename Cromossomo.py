import math

class Cromossomo:
    def __init__(self,valor_continuo):
        self.valor_continuo = valor_continuo
        self.aptidao = self.calcula_aptidao(self.valor_continuo)

    def get_aptidao(self):
        return self.aptidao

    def get_valorcontinuo(self):
        return self.valor_continuo

    def calcula_aptidao(self,valor_continuo):
        return (math.cos(valor_continuo) * valor_continuo) + 2