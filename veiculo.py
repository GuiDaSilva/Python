import abc

class Veiculo():
    """ Essa é a classe carro. Essa classe é utilizada para instanciar novos carros """
    def __init__(self, cor, tipo_combustivel, potencia):
        self._cor = cor
        self.__tipo_combustivel = tipo_combustivel
        self.__potencia = potencia
        self._qtd_combustivel = 0
        self.__is_ligado = False
        self.__velocidade = 0

    def __del__(self):
        print("O objeto foi removido da memória.")

    @abc.abstractmethod
    def pintar (self, cor):
        self._cor = cor

    @property
    def cor(self):
        return self._cor


    def abastecer(self, qtd_combustivel):
        self._qtd_combustivel += qtd_combustivel
    """ O método abastecer recebe como parâmetro a quantidade de combustível e incrementa o atributo qtd_combustivel """

    def ligar(self):
        if self.__is_ligado == True:
            print("O veiculo já está ligado")
        else:
            self.__is_ligado = True
            print("O veiculo foi ligado")

    def desligar(self):
        if self.__is_ligado == False:
            print("O veiculo já está desligado")
        else:
            self.__is_ligado = False
            print("O veiculo foi desligado")

    def acelerar(self, velocidade=10):
        if self.__is_ligado == True:
            self.__velocidade += velocidade
        else:
            print("O veiculo precisa estar ligado para acelerar!")
