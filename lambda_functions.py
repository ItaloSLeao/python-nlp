"""
Aula: lambda

Exercicio 1
Crie uma lista de numeros.
Use sorted com uma funcao lambda para ordenar os numeros pelo valor absoluto.

Exercicio 2
Crie uma lista de palavras.
Use sorted com lambda para ordenar as palavras pela ultima letra.

Exercicio 3
Crie uma lista de pares no formato (palavra, contagem).
Use sorted com lambda para ordenar pela contagem, da maior para a menor.

Exercicio 4
Crie uma lista de frases.
Use sorted com lambda para ordenar pela quantidade de palavras de cada frase.

Estrutura do conceito:
lambda parametro: valor_retornado
"""

# Escreva suas solucoes abaixo:
numeros = [5, 9, 6, 5, 7, 4, 8, 1, 2, 0, 3]
numeros = sorted(numeros, key=lambda n : abs(n))
print(numeros)

palavras = ["yaris", "lista", "joab", "carro"]
palavras = sorted(palavras, key=lambda p : p[-1])
print(palavras)

pares = [("scorpions", 356), ("wind", 229), ("of", 9292), ("change", 9883)]
print(sorted(pares, key=lambda p : p[1], reverse=True))

frases = ["kendall is addicted", "i am watching succession series", "i like siobahn roy", "hi greg"]
print(sorted(frases, key=lambda frase : len(frase.split())))
