# Módulos = Blocos de códigos que podemos utilizar em outros arquivos

print("Exemplo de importação de módulo padrão: ")
import math
from math import sqrt # Recomendado


# raiz_quadrada = math.sqrt(25)
raiz_quadrada = sqrt(25)
print(f"A raiz quadrade de 25 é {raiz_quadrada}")

print("\n Exemplo de criação e utilização de um módulo personalizado: ")
import meu_modulo

mensagem = meu_modulo.saudacao("Grazi")
print(mensagem)

dobro = meu_modulo.dobro(raiz_quadrada)
print(dobro)