lista = [1, 2, 3, 4, 5]
for elemento in lista :
  print(elemento)

  tupla = (1, 2, 3, 4, 5)
  for elemento in tupla:
    print(elemento)

  pessoa = {"nome":"Grazielli", "idade": 27, "cidade": "São Paulo"}
  print("For utilizando dicionario - chaves")
  for chave in pessoa.keys():
    print(chave)

  for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")


# range = Intervalo numérico em formato de lista 
print(list(range(1, 10)))

for numero in range(5):
  print("Numero: ", numero)

# lenght - quantidade de items que temos nessa lista
lista = [1, 2, 3, 4, 5, 6]
for indice in range(0, len(lista)):
  print(indice)

# enumerate()
lista_enumerate = ["a", "b", "c"]
for indice, valor in enumerate(lista_enumerate):
  print(f"{indice}:{valor}")