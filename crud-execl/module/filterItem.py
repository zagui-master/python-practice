
def filtrar(info: dict, filtro: str):
    aux = {}

    for i in info:
        if info[1]["estado"] == filtro:
            aux.setdefault(i, info[i])
    return aux