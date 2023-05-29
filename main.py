def largest_sum(lista):
    if len(lista) < 2:
        return None
    maiores_numeros = sorted(lista, reverse=True)[:2]
    primeiro = maiores_numeros[1]
    segundo = maiores_numeros[0]
    tupla = (primeiro, segundo)
    return tupla