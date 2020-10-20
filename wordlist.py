# Avaa tiedoston ja lukee sen
def get_words():
    with open('kotus-sanalista-suomi.txt', encoding='utf-8') as file:
        return file.read().lower().splitlines()
