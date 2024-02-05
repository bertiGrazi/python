class MinhaClaase:
  valor = 10

  def __init__(self, nome) -> None:
    self.nome = nome
  
  def metodo_instancia(self):
    return f"Método de instância chamado para {self.nome}"
  

obj = MinhaClaase(nome="Teste")
print(obj.metodo_instancia())