# Aula: ordenacao
#
# Ordenar dados e uma tarefa comum em Python.
# Em NLP, depois de contar palavras, muitas vezes queremos descobrir
# quais palavras apareceram mais vezes.
#
# Exemplo de ideia:
# word_count = {
#     "python": 3,
#     "nlp": 2,
#     "data": 5
# }
#
# for word, count in word_count.items():
#     print(word, count)
#
# Desafio:
# 1. Crie um dicionario com algumas palavras e suas contagens.
# 2. Use um for com .items() para mostrar cada palavra e sua contagem.
# 3. Depois, use sorted() para mostrar as palavras em ordem alfabetica.
# 4. Depois, use sorted() com key para mostrar as palavras da maior
#    contagem para a menor.
#
# Dicas:
# word_count.items()
# sorted(word_count)
# sorted(word_count.items(), key=lambda item: item[1], reverse=True)
#
# Exemplo:
# Entrada fixa no codigo:
# {"python": 3, "nlp": 2, "data": 5}
#
# Saida esperada aproximada:
# python 3
# nlp 2
# data 5
#
# data
# nlp
# python
#
# data 5
# python 3
# nlp 2

# Escreva sua solucao abaixo:
"""word_count = {"python": 3, "nlp": 2, "data": 5}

for w,c in word_count.items():
    print(w,c)

for w in sorted(word_count):
    print(w)

for w,c in sorted(word_count.items(), key=lambda item: item[1], reverse=True):
    print(w,c)
"""

# Exercicios extras
#
# Exercicio 2: ordenar palavras por tamanho
#
# 1. Crie uma lista de palavras.
# 2. Mostre as palavras em ordem alfabetica.
# 3. Mostre as palavras da menor para a maior, considerando o tamanho.
# 4. Mostre as palavras da maior para a menor, considerando o tamanho.
#
# Estrutura do conceito:
# sorted(alguma_lista)
# sorted(alguma_lista, key=alguma_regra)
# sorted(alguma_lista, key=alguma_regra, reverse=True)
#
# A regra pode ser uma funcao que recebe um elemento e devolve
# o criterio usado para ordenar.
"""palavras = ["lionel", "messi", "corinthians", "garro", "ocho"]

for word in sorted(palavras):
    print(word)
    
for word in sorted(palavras, key=lambda word: len(word)):
    print(word)
    
for word in sorted(palavras, key=lambda word: len(word), reverse=True):
    print(word)"""
    

# Exercicio 3: ordenar frases por quantidade de palavras
#
# 1. Crie uma lista com pelo menos 4 frases.
# 2. Mostre as frases da menor para a maior, considerando
#    a quantidade de palavras em cada frase.
# 3. Depois mostre da maior para a menor.
#
# Estrutura do conceito:
# def nome_da_funcao(elemento):
#     return algum_valor_calculado
#
# sorted(colecao, key=nome_da_funcao)
#
# Lembrete:
# uma frase pode ser separada em palavras antes de contar.
"""frases = ["messi eh o melhor", "lionel eh o maior de todos",
          "corinthians maior de todos do br", "ola para voce"]

def conta_palavras(frase):
    return len(frase.split())

for frase in sorted(frases, key=conta_palavras):
    print(frase)

print("\n")

for frase in sorted(frases, key=conta_palavras, reverse=True):
    print(frase)"""


# Exercicio 4: top 3 palavras mais frequentes
#
# 1. Crie uma frase fixa no codigo.
# 2. Transforme a frase em minusculas.
# 3. Separe em palavras.
# 4. Conte a frequencia de cada palavra usando um dicionario.
# 5. Ordene os pares do dicionario pela contagem, da maior para a menor.
# 6. Mostre apenas as 3 primeiras palavras.
#
# Estrutura do conceito:
# lista[:3]
#
# Isso pega os tres primeiros elementos de uma lista.
# A ordenacao deve acontecer antes desse corte.


# Escreva suas solucoes abaixo:
frase = "Vem meu crIna negra pula pUla sem cAnsAr nessE mEu e veM"
minusculas = frase.lower()
palavras = minusculas.split()

dicionario = {}

for p in palavras:
    if p in dicionario:
        dicionario[p] = dicionario[p] + 1
    else:
        dicionario[p] = 1
        
ordenado =  sorted(dicionario.items(), key=lambda item : item[1], reverse=True)

print(ordenado[:3])