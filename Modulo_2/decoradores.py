# Decorador = Tipo funcional de funções que podemos adicionar funcionalidades que não necessariamente
# temos que mexer no código já feito 

def meu_decorador(func):
  def wrapper():
    print("Antes da função ser chamada")
    func()
    print("Depois da função ser chamada")
  return wrapper

@meu_decorador
def minha_funcao():
  print("Minha função foi chamada")


minha_funcao()