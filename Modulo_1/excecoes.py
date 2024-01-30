# Tratativa genérica

while True: 
  try: 
    numero = int(input("Digite um número inteiro: "))
    resultado = 10 / numero
    print(resultado)
  
  except ValueError as errorValue:
    # print(f"Erro de value error {ValueError}")
    raise ValueError("Tipo de variáveis incompatíveis")

  except Exception as e:
    print(f"Erro {e}")

  else: 
    print(f"Resultado: {resultado}")
  
  finally: 
    print("Operação finalizada!")
