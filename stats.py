def contador(texto):
    palavras = texto.split()
    numbers = len(palavras)
    return numbers

def silabador(texto):
    minus = texto.lower()
    alfabeto=list('abcdefghijklmnopqrstuvwxyzæâêëô')
    dicio={}
    for l in minus:
        if l in dicio:
            dicio[l] += 1
        elif l in alfabeto:
            dicio[l] = 1
    return dicio

def sort_on (item):
    return item["num"]

def lista_dicio(dicio):
    lista_dicio = []
    for chave in dicio:
        lista_dicio.append({"char": chave, "num": dicio[chave]})
    lista_dicio.sort(reverse=True, key=sort_on)
    return lista_dicio