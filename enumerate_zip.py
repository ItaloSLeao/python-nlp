"""
Aula: enumerate e zip

Exercicio 1
Crie uma lista de palavras.
Use enumerate para mostrar cada palavra junto com sua posicao.

Exercicio 2
Crie uma lista de frases.
Use enumerate para mostrar apenas as frases que estao em posicoes pares.

Exercicio 3
Crie uma lista de textos e uma lista de labels.
Use zip para mostrar cada texto junto com seu label.

Exercicio 4
Crie duas listas de numeros com o mesmo tamanho.
Use zip para criar uma nova lista com a soma dos pares.

Estrutura do conceito:
for indice, valor in enumerate(colecao):
    ...

for valor_a, valor_b in zip(colecao_a, colecao_b):
    ...
"""

# Escreva suas solucoes abaixo:
#exercicio 1
lista = ["mesa", "cadeira", "roupa", "televisao", "computador"]

for i, palavra in enumerate(lista):
    print(i,palavra)
    
#exercicio 2
    
frases = ["brasil eh hexa", "messi goat", "alexa turn off music", "hahahaha", "samambaia eh top"]

for i, frase in enumerate(frases):
    if i%2==0:
        print(i,frase)
        
#exercicio 3
        
textos = []
labels = []
for i in range(5):
    textos.append(input("digite um texto: "))
    labels.append(input("digite seu label: "))

for t,l in zip(textos,labels):
    print(t,l)

#exercicio 4
    
numeros1 = [1, 2, 3, 4, 5, 6]
numeros2 = [6, 5, 4, 3, 2, 1]
nova = [n1+n2 for n1,n2 in zip(numeros1, numeros2)]
print(nova)

