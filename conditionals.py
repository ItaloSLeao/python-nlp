# Aula 03: condicionais aplicadas a texto
#
# Condicionais em Python usam if, elif e else.
# Repare no uso de ":" e da indentacao.

text = input("Write a sentence about what you want to learn: ").strip()

if text == "":
    print("You did not write anything.")
elif "python" in text.lower():
    print("Good start: Python is the base.")
elif "nlp" in text.lower() or "language" in text.lower():
    print("Nice: you are already thinking about language processing.")
elif "machine learning" in text.lower() or "ml" in text.lower():
    print("Great: ML will use a lot of data and math.")
else:
    print("Interesting. We can connect this topic to Python later.")

# Um detalhe importante:
# "Python" == "python" seria False.
# Por isso usamos lower() para comparar tudo em minusculo.

# Desafio:
# 1. Crie uma variavel score com um numero de 0 a 100.
# 2. Use if/elif/else para mostrar:
#    - "Beginner" se score < 40
#    - "Intermediate" se score < 80
#    - "Advanced" caso contrario

score = int(input("Type a number from 0 to 100: "))

if score < 40:
    print("Beginner")
elif score < 80:
    print("Intermediate")
else:
    print("Advanced")


# Aula 04: listas e texto
#
# Uma lista em Python guarda varios valores em uma unica variavel.
# Em NLP, listas aparecem o tempo todo: palavras, frases, tokens,
# documentos, labels e resultados de modelos.
#
# Desafio:
# 1. Peca uma frase ao usuario com input().
# 2. Transforme a frase em uma lista de palavras usando split().
# 3. Mostre a lista completa.
# 4. Mostre quantas palavras existem na frase.
# 5. Mostre a primeira palavra.
# 6. Mostre a ultima palavra.
# 7. Use if/else:
#    - se houver mais de 5 palavras, mostre "Long sentence"
#    - caso contrario, mostre "Short sentence"
#
# Dicas:
# words = sentence.split()
# len(words)
# words[0]
# words[-1]
#
# Cuidado:
# Se o usuario apertar Enter sem digitar nada, words[0] da erro.
# Tente tratar esse caso antes de acessar a primeira e a ultima palavra.

# Escreva sua solucao abaixo:
frase = input("digite uma frase: ").strip().split()
print(frase)
print(len(frase))
if frase:
    print(frase[0])
    print(frase[-1])

    if len(frase) > 5:
        print("long sentence")
    else:
        print("short sentence")
else:
    print("lista vazia")