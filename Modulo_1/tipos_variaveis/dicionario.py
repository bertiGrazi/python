#  Dicionários: Coleção NÃO ordenada de pares (chave: valor)

# Criando um dicionário de exemplo
pessoa = {"nome": "Grazielli", "idade": 27, "cidade": "Guarulhos"}
print("Meu dicionário: ", pessoa)

# Acessando valores por chaves
print("Nome: ", pessoa["nome"])
print("Idade: ", pessoa["idade"])
print("Cidade: ", pessoa["cidade"])

# Atribuindo valor a um dicionário que já foi criado
pessoa["sobrenome"] = "Berti"
print("Sobrenome: ", pessoa["sobrenome"])

# Atualizando dados
pessoa["idade"] = 28
print(pessoa)

# Removendo um par chave:valor
del pessoa["sobrenome"]
print(pessoa)

# Método keys()
chaves = list(pessoa.keys())
print("Chaves do dicionários: ", chaves)
print("Primeira chave: ", chaves[0])

# Método values()
valores = list(pessoa.values())
print("Valores do dicionário: ", valores)
print("Primeiro valor do dicionário: ", valores[0])

# Métodos items = Cada cheve valor vira uma tupla
itens = list(pessoa.items())
print("Pares chave-valor do dicionário: ", itens)
print("Primeiro chave-valor: %s = %s " % (itens[0][0], itens[0][1]))
