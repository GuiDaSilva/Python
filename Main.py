import carro,moto

uno_vermelho = carro.Carro("vermelho", "Flex", 1.0, 4)
uno_vermelho.ligar()
uno_vermelho.abastecer(50)
uno_vermelho.abastecer(10)
uno_vermelho.acelerar(20)
uno_vermelho.pintar("azul")
print(uno_vermelho.cor)
print(f"A quantidade de combustível do carro é:")

moto_vermelha = moto.Moto("vermelho", "Gasolina", 125, 2)
moto_vermelha.ligar()
moto_vermelha.abastecer(30)
moto_vermelha.abastecer(10)
