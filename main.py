from stats import contador, silabador, lista_dicio
def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def main():
    path = "books/frankenstein.txt"
    texto = get_book_text(path)
    numbers = contador(texto)
    dicio = silabador (texto)
    lista = lista_dicio(dicio)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {numbers} total words")
    print("--------- Character Count -------")
    for item in lista:
        print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")
main()
