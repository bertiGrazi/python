# Herança, Polimorfismo e Encapsulamento

## Exemplo de Herança

class Animal:
  def __init__(self, nome) -> None:
    self.nome = nome

    def andou(self):
      print (f"O animal {self.nome} andou.")

    def emitir_som(self):
      pass


class Cachorro(Animal):
      def emitir_som(self):
        print("Au Au")

class Gato(Animal):
      def emitir_som(self):
        print("Miau Miau")

# Polimorfismo = Mesmo metodo mas em cada objeto ele faz uma coisa (emitir_som). 
        
dog = Cachorro(nome="Mel")
cat = Gato(nome="Jeronima")

print("\nExemplo de Polimorfismo: ")
animais = [dog, cat]

for animal in animais:
    print(f"Animal {animal.nome} faz ", end="")
    animal.emitir_som()

print("\nExemplo de Encampsulamento:\n")
class ContaBancaria: 
  def __init__(self, saldo) -> None:
      self.__saldo = saldo # Atributo privado

  def depositar(self, valor):
      if valor > 0:
          self.__saldo += valor
  
  def sacar(self, valor):
     if valor > 0 and valor <= self.__saldo:
        self.__saldo -= valor
  
  def consultar_saldo(self):
     return self.__saldo
  

conta = ContaBancaria(1000)
print(f"Saldo da CC: {conta.consultar_saldo()}" )

conta.depositar(valor=500)
print(f"Saldo da CC: {conta.consultar_saldo()}" )

conta.sacar(valor=200)
print(f"Saldo da CC: {conta.consultar_saldo()}" )
