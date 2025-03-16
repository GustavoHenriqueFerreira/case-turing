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
    # Inicializa estruturas de dados
    projetos = {i: [] for i in range(1, qtd_projetos + 1)}
    ultima_ordem = {}
    
    # Processa os episódios
    for projeto_id, indice, passos in episodios:
        if projeto_id in ultima_ordem and indice < ultima_ordem[projeto_id]:
            return "nao", [[] for _ in range(qtd_projetos)]  # Descarte total se a ordem for incorreta
        
        ultima_ordem[projeto_id] = indice  # Atualiza a última ordem registrada
        projetos[projeto_id].append([projeto_id, indice, passos])
    
    # Filtra projetos com duração mínima
    resultado = []
    pelo_menos_um_valido = False
    
    for i in range(1, qtd_projetos + 1):
        total_passos = sum(ep[2] for ep in projetos[i])
        if total_passos >= min_passos:
            resultado.append(projetos[i])
            pelo_menos_um_valido = True
        else:
            resultado.append([])
    
    return ("sim" if pelo_menos_um_valido else "nao", resultado)

# Exemplo de teste:
print(organiza_listas(5, [[2, 128, 30], [3, 10, 100], [1, 13, 200], [1, 78, 80], [2, 256, 70],
                           [1, 130, 120], [5, 1, 40], [2, 512, 50], [3, 100, 150], [5, 680, 200],
                           [5, 681, 60], [1, 198, 300]], 250))

print(organiza_listas(3, [[1, 1, 10],
[1, 2, 20],
[2, 5, 30],
[3, 10, 50],
[3, 12, 100],
[1, 8, 60],
[2, 6, 100],
[1, 25, 100],
[3, 15, 100],
[1, 30, 80]], 250))

# Output: ("sim",
# [[[1, 1, 10], [1, 2, 20], [1, 8, 60], [1, 25, 100], [1, 30, 80]],
# [],
# [[3, 10, 50], [3, 12, 100], [3, 15, 100]]])

print(organiza_listas(3, [[1, 1, 10],
[1, 2, 20],
[2, 5, 30],
[3, 10, 50],
[3, 12, 100],
[1, 8, 60],
[2, 6, 100],
[1, 25, 100],
[3, 15, 100],
[1, 30, 80]], 300))

# Output: ("nao", [[], [], []])

print(organiza_listas(3, [[1, 1, 10],
[1, 2, 20],
[2, 5, 30],
[3, 10, 50],
[3, 12, 100],
[1, 8, 60],
[2, 6, 100],
[1, 25, 100],
[3, 15, 100],
[1, 30, 80],
[2, 4, 150],
[1, 40, 100],
[1, 50, 150]], 250))

# Output: ("nao", [[], [], []])