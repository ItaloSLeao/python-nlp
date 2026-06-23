# Aula: dicionarios
#
# Um dicionario guarda pares de chave e valor.
# Em NLP, isso e muito util para contar quantas vezes cada palavra aparece.
#
# Exemplo de ideia:
# word_count = {
#     "python": 2,
#     "nlp": 1
# }
#
# print(word_count["python"])
#
# Desafio:
# 1. Peca uma frase ao usuario com input().
# 2. Transforme a frase em minusculas com lower().
# 3. Separe a frase em palavras com split().
# 4. Crie um dicionario vazio chamado word_count.
# 5. Use um for para percorrer as palavras.
# 6. Para cada palavra:
#    - se ela ja existe no dicionario, aumente a contagem em 1
#    - se ela nao existe, adicione a palavra com contagem 1
# 7. Mostre o dicionario completo no final.
#
# Dicas:
# word_count = {}
#
# if word in word_count:
#     word_count[word] = word_count[word] + 1
# else:
#     word_count[word] = 1
#
# Exemplo:
# Entrada:
# python is fun and python is useful
#
# Saida esperada aproximada:
# {"python": 2, "is": 2, "fun": 1, "and": 1, "useful": 1}

# Escreva sua solucao abaixo:
frase = input("insira uma frase: ")
words = frase.lower().split()

word_count = {}

for w in words:
    if w in word_count:
        word_count[w] = word_count[w] + 1
    else:
        word_count[w] = 1

print(word_count)