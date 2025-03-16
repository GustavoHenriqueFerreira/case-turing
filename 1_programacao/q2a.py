def organiza_listas(qtd_projetos, episodios, min_passos):
    """
    Organiza os episódios dos projetos, verificando ordem cronológica e filtrando por duração mínima.

    Parâmetros:
        qtd_projetos (int): Número total de projetos.
        episodios (list): Lista de episódios no formato [id_projeto, indice, passos].
        min_passos (int): Número mínimo de passos para considerar um projeto válido.

    Retorno:
        tuple: ("sim" ou "nao", lista de episódios organizados por projeto).
    """
    projetos, ultima_ordem = _inicializar_estruturas(qtd_projetos)
    
    if not _processar_episodios(episodios, projetos, ultima_ordem):
        return "nao", [[] for _ in range(qtd_projetos)]
    
    resultado, pelo_menos_um_valido = _filtrar_projetos(qtd_projetos, projetos, min_passos)
    
    return ("sim" if pelo_menos_um_valido else "nao", resultado)


def _inicializar_estruturas(qtd_projetos):
    """
    Inicializa as estruturas de dados necessárias.

    Parâmetros:
        qtd_projetos (int): Número total de projetos.

    Retorno:
        tuple: (projetos, ultima_ordem)
    """
    projetos = {i: [] for i in range(1, qtd_projetos + 1)}
    ultima_ordem = {}
    return projetos, ultima_ordem


def _processar_episodios(episodios, projetos, ultima_ordem):
    """
    Processa os episódios, verificando a ordem cronológica e organizando-os por projeto.

    Parâmetros:
        episodios (list): Lista de episódios no formato [id_projeto, indice, passos].
        projetos (dict): Dicionário para armazenar episódios por projeto.
        ultima_ordem (dict): Dicionário para rastrear o último índice de cada projeto.

    Retorno:
        bool: True se a ordem cronológica for válida, False caso contrário.
    """
    for episodio in episodios:
        projeto_id, indice, passos = episodio

        if projeto_id in ultima_ordem and indice < ultima_ordem[projeto_id]:
            return False

        ultima_ordem[projeto_id] = indice
        projetos[projeto_id].append(episodio)
    
    return True


def _filtrar_projetos(qtd_projetos, projetos, min_passos):
    """
    Filtra os projetos com base no número mínimo de passos.

    Parâmetros:
        qtd_projetos (int): Número total de projetos.
        projetos (dict): Dicionário com episódios organizados por projeto.
        min_passos (int): Número mínimo de passos para considerar um projeto válido.

    Retorno:
        tuple: (resultado, pelo_menos_um_valido)
    """
    resultado = []
    pelo_menos_um_valido = False

    for projeto_id in range(1, qtd_projetos + 1):
        total_passos = sum(episodio[2] for episodio in projetos[projeto_id])

        if total_passos >= min_passos:
            resultado.append(projetos[projeto_id])
            pelo_menos_um_valido = True
        else:
            resultado.append([])
    
    return resultado, pelo_menos_um_valido