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