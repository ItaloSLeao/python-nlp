# Aula 02: funcoes
#
# Em Python, funcoes sao criadas com def.
# O bloco da funcao depende da indentacao, nao de chaves.

def normalize_name(name):
    return name.strip().title()


def hello(to="world"):
    print(f"Hello, {to}")


def count_words(text):
    words = text.split()
    return len(words)


def main():
    name = input("Name? ")
    normalized_name = normalize_name(name)
    hello(normalized_name)

    sentence = input("Write a sentence: ")
    total_words = count_words(sentence)
    print(f"Your sentence has {total_words} words.")


main()

# Desafio:
# Crie uma funcao chamada contains_python(text)
# que retorna True se a palavra "python" aparecer no texto,
# ignorando maiusculas e minusculas.

def contains_python(text):
    words = text.lower().split()
    for w in words:
        if w == "python":
            return True

    return False
        
