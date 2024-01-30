# Lista = Uma coleção de elementos ordenados e multáveis 

# Declaração 

minha_lista = [1, 2, 3, 4, 5, "Grazielli", True]

# Exibindo a lista
print(minha_lista)
print(minha_lista[3])

# Fateamento da lista
print(minha_lista[1:7])
print(minha_lista[:5])
print(minha_lista[4:])

# minha_lista multável
minha_lista[0] = "python"
print("minha_lista multável:", minha_lista)

# Método append() = Adiciona um elemento ao final da lista 
minha_lista.append(6)
print("minha_lista após o append", minha_lista)

# Método index
indice = minha_lista.index(6)
print("Indíce do elemento 6: ", indice)

# Método insert: Inseri um elemento em um index específico
minha_lista.insert(2, 10)
print("Após o insert(2,10): ", minha_lista)

# Método pop = Remove/Retorna o elemento de um indice especi1fico
elemento_removido = minha_lista.pop(2)
print("Removendo o elemento do indíce 2: ", elemento_removido)
print("Após pop(2)", minha_lista)

# Método remove 
minha_lista.remove(True)
print("Após remove(True):", minha_lista)

# Método sort = Organizar a nossa lista em ordem crescente
minha_lista_com_numeros = [30, 40, 1, 4, 7, 10, 2]
minha_lista_com_numeros.sort()
print("minha_lista depois do sort: ", minha_lista_com_numeros) 
