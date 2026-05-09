nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
num_tel = input("Digite seu número de telefone: ")

# Indetifica a posição da primeira ocorrência do caracter
resultado = nome.find("R")
print(resultado)

# Identifica a última ocorrência
resultado = nome.rfind("R")
print(resultado)

# Deixa a primeira letra da string maiúscula
nome = nome.capitalize()
print(nome)

# Deixa a string maiúscula
print(nome.upper())

# Deixa a string minúscula
print(nome.lower())

# Verifica se possui apenas numeros
verificacao_numero = idade.isdigit()
print(verificacao_numero)

# Verifica se possui apenas letras do alfabeto sem contar espaços
verificacao_letra = nome.isdigit()
print(verificacao_letra)

# Retorna o numero de repetição de um caracter
repe_caracter = num_tel.count("-")

# Substitui qualquer caracter por outro
num_tel = num_tel.replace("-","")
print(num_tel)

# Exibe o tamanho da string
print(len(nome))