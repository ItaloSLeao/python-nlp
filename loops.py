# Aula 05: loops com listas
#
# Em Python, o for percorre diretamente os elementos de uma lista.
# Isso e muito usado em NLP: depois de separar uma frase em palavras,
# normalmente queremos analisar cada palavra.
#
# Exemplo de ideia:
# words = ["python", "nlp", "data"]
#
# for word in words:
#     print(word)
#
# Desafio:
# 1. Peca uma frase ao usuario com input().
# 2. Transforme a frase em uma lista de palavras usando split().
# 3. Use um for para mostrar uma palavra por linha.
# 4. Conte quantas palavras tem mais de 5 caracteres.
# 5. Mostre essa quantidade no final.
#
# Dicas:
# len(word)
# counter = counter + 1
#
# Exemplo:
# Entrada:
# I am learning python for natural language processing
#
# Saida esperada aproximada:
# I
# am
# learning
# python
# for
# natural
# language
# processing
# Words with more than 5 characters: 5

# Escreva sua solucao abaixo:
words = input("digite uma frase: ").split()
counter = 0

for w in words:
    print(w + "\n")
    if len(w) > 5:
        counter = counter + 1

print(counter)