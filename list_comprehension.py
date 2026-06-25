# Aula: list comprehension
#
# List comprehension e uma forma curta de criar listas a partir
# de outra colecao.
#
# Ela aparece muito em codigo Python para dados, ML e NLP.
# A ideia principal e:
#
# nova_lista = [transformacao for elemento in colecao]
#
# Tambem pode ter uma condicao:
#
# nova_lista = [transformacao for elemento in colecao if condicao]
#
# Exercicio 1: normalizar palavras
#
# 1. Crie uma lista de palavras com algumas letras maiusculas.
# 2. Crie uma nova lista com todas as palavras em minusculas.
# 3. Mostre a lista original.
# 4. Mostre a lista nova.
#
# Estrutura do conceito:
# [algo_transformado for item in colecao]
palavras = ["Mito", "eRlinG", "haAlAnD"]
minusculas = [palavra.lower() for palavra in palavras]
print(palavras)
print(minusculas)
#
#
# Exercicio 2: filtrar palavras
#
# 1. Crie uma lista de palavras.
# 2. Crie uma nova lista contendo apenas palavras com mais de 4 caracteres.
# 3. Mostre a nova lista.
#
# Estrutura do conceito:
# [item for item in colecao if alguma_condicao]
lista = ["carro", "caminhao", "trigo", "tigre", "arvore"]
outra = [item for item in lista if len(item) > 4]
print(outra)
#
#
# Exercicio 3: limpar uma frase
#
# 1. Crie uma frase fixa no codigo.
# 2. Transforme a frase em minusculas.
# 3. Separe a frase em palavras.
# 4. Crie uma nova lista removendo palavras pequenas.
#    Considere pequenas as palavras com 2 caracteres ou menos.
# 5. Mostre a lista final.
#
# Estrutura do conceito:
# texto -> normalizacao -> lista -> filtro -> resultado
frase = "o rato roeu a roupa do rei de roma e dirigiu um sonic"
frase = frase.lower()
palavras = frase.split()
nova = [palavra for palavra in palavras if len(palavra) > 2]
print(nova)
#
#
# Exercicio 4: tamanhos das palavras
#
# 1. Crie uma lista de palavras.
# 2. Crie uma nova lista contendo o tamanho de cada palavra.
# 3. Mostre a lista de tamanhos.
#
# Estrutura do conceito:
# [valor_calculado for item in colecao]

# Escreva suas solucoes abaixo:
palavras = ["randon", "veiculo", "longo", "comprimento"]
tamanho = [len(palavra) for palavra in palavras]
print(tamanho)
