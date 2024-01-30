# Coleção ORDENADA e IMULTÁVEL (que não podemos mudar) de elementos

# Criando uma tupla de exemplo
minha_tupla = (1, 2, 2, 3, 4)
print("minha_tupla", minha_tupla)

# Acessando os elementos
print("minha_tupla[0]", minha_tupla[0])
print("minha_tupla[-1] - Assim pega o último elemento. Funciona com Array também: ", minha_tupla[-1])

# Método count
contagem = minha_tupla.count(2)
print("Quantidade de vezes que o elemento 2 aparece: ", contagem)

# Método index
indice = minha_tupla.index(3)
print("Indice da minha primeira ocorência do elemento 3: ", indice)

