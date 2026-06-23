# Aula 01: entrada, strings e print
#
# Em Python, voce nao precisa declarar o tipo da variavel.
# O valor retornado por input() sempre vem como string.

name = input("What's your name? ").strip().title()

# strip() remove espacos no inicio e no fim.
# title() coloca a primeira letra de cada palavra em maiuscula.

# Exemplo:
# "   ada lovelace   " -> "Ada Lovelace"

print("Hello, " + name)
print(f"hello, {name}")

# Desafio:
# 1. Crie uma variavel chamada language com o valor "Python".
# 2. Mostre uma frase usando f-string:
#    "Ada Lovelace is learning Python"

language = "Python"
print(f"ada lovelace is learning {language}")