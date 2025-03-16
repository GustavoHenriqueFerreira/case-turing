from collections import deque

# Função para calcular a distância mínima entre dois territórios no grafo
def calcular_distancia(grafo, origem, destino):
    fila = deque([origem])
    distancias = {origem: 0}
    
    while fila:
        atual = fila.popleft()
        if atual == destino:
            return distancias[atual]
        
        for vizinho in grafo[atual]:
            if vizinho not in distancias:
                distancias[vizinho] = distancias[atual] + 1
                fila.append(vizinho)
    
    return float('inf')  # Caso não haja caminho


# Função para construir o grafo de vizinhança
def construir_grafo(vizinhos):
    grafo = {}
    for territorio1, territorio2 in vizinhos:
        if territorio1 not in grafo:
            grafo[territorio1] = []
        if territorio2 not in grafo:
            grafo[territorio2] = []
        
        grafo[territorio1].append(territorio2)
        grafo[territorio2].append(territorio1)
    
    return grafo


# Função para filtrar os territórios pertencentes ao jogador
def obter_territorios_jogador(cor, tropas):
    return {territorio: tropas_ for territorio, tropas_, dono in tropas if dono == cor}

# Função para encontrar inimigos vizinhos de um território
def encontrar_vizinhos_inimigos(grafo, tropas, cor, territorio):
    inimigos_vizinhos = []
    for vizinho in grafo.get(territorio, []):
        for nome_territorio, _, cor_dono in tropas:
            if nome_territorio == vizinho and cor_dono != cor:
                inimigos_vizinhos.append(vizinho)
                break
    return inimigos_vizinhos

# Função para calcular distancia minima para inimigos
def calcular_distancia_minima_para_inimigos(vizinho, tropas, cor, grafo):
    """
    Calcula a menor distância entre um território vizinho e qualquer inimigo.
    """
    melhor_distancia_vizinho = float('inf')
    
    # Para cada inimigo, calcula a distância e atualiza se for a menor
    for nome_territorio_inimigo, _, cor_dono_inimigo in tropas:
        if cor_dono_inimigo != cor:  # Somente inimigos
            distancia = calcular_distancia(grafo, vizinho, nome_territorio_inimigo)
            if distancia < melhor_distancia_vizinho:
                melhor_distancia_vizinho = distancia
    
    return melhor_distancia_vizinho

# Função para calcular melhor vizinho
def calcular_melhor_vizinho(territorio, vizinhos_do_territorio, tropas, cor, grafo):
    """
    Calcula o melhor vizinho para um território específico, baseado em várias condições.
    """
    melhor_vizinho = None
    melhor_distancia = float('inf')
    melhor_tropas = float('inf')
    melhor_alfabetica = None
    
    # Encontrar o número de tropas para o território atual
    tropa_atual = next(tropa for t, tropa, dono in tropas if t == territorio and dono == cor)
    
    for vizinho in vizinhos_do_territorio:
        # Verificar se o vizinho pertence ao jogador (mesmo dono)
        if not any(nome_territorio == vizinho and cor_dono == cor for nome_territorio, _, cor_dono in tropas):
            continue  # Pula vizinhos que não pertencem ao jogador
        
        # Calcular a distância mínima para os inimigos desse vizinho
        distancia_minima_inimigos = calcular_distancia_minima_para_inimigos(vizinho, tropas, cor, grafo)
        
        # Verificar se o vizinho atual é melhor com base nas condições
        considerado_melhor_caminho = (
            distancia_minima_inimigos < melhor_distancia or
            (distancia_minima_inimigos == melhor_distancia and tropa_atual < melhor_tropas) or
            (distancia_minima_inimigos == melhor_distancia and tropa_atual == melhor_tropas and vizinho < melhor_alfabetica)
        )
        
        if considerado_melhor_caminho:
            melhor_vizinho = vizinho
            melhor_distancia = distancia_minima_inimigos
            melhor_tropas = tropa_atual
            melhor_alfabetica = vizinho

    return melhor_vizinho

# Função principal que organiza a movimentação das tropas
def mover_tropas(cor, vizinhos, tropas):
    grafo = construir_grafo(vizinhos)  # Construir o grafo de vizinhança
    territorios_jogador = obter_territorios_jogador(cor, tropas)  # Filtrar os territórios do jogador
    movimentacoes = []

    # Percorrer os territórios do jogador
    for territorio, tropa in territorios_jogador.items():
        if tropa > 1:  # Só movimenta se houver mais de 1 tropa
            vizinhos_do_territorio = grafo.get(territorio, [])
            
            # Encontrar inimigos vizinhos
            inimigos_vizinhos = encontrar_vizinhos_inimigos(grafo, tropas, cor, territorio)
            
            if not inimigos_vizinhos:  # Se não há inimigos vizinhos, considerar movimentação
                melhor_vizinho = calcular_melhor_vizinho(territorio, vizinhos_do_territorio, tropas, cor, grafo)
                
                if melhor_vizinho:
                    movimentacoes.append((territorio, melhor_vizinho))

    return movimentacoes


# Função principal que organiza a movimentação das tropas
def mover_tropas(cor, vizinhos, tropas):
    # Construir o grafo de vizinhança
    grafo = construir_grafo(vizinhos)
    
    # Filtrar os territórios do jogador
    territorios_jogador = obter_territorios_jogador(cor, tropas)
    
    # Lista para armazenar as movimentações sugeridas
    movimentacoes = []

    # Percorrer os territórios do jogador
    for territorio, tropa in territorios_jogador.items():
        if tropa > 1:  # Só movimenta se houver mais de 1 tropa
            vizinhos_do_territorio = grafo.get(territorio, [])
            
            # Encontrar inimigos vizinhos
            inimigos_vizinhos = encontrar_vizinhos_inimigos(grafo, tropas, cor, territorio)
            
            if not inimigos_vizinhos:  # Se não há inimigos vizinhos, considerar movimentação
                melhor_vizinho = calcular_melhor_vizinho(territorio, vizinhos_do_territorio, tropas, cor, grafo)
                
                if melhor_vizinho:
                    movimentacoes.append((territorio, melhor_vizinho))

    return movimentacoes

# Exemplo de teste
resultado = mover_tropas(
    "verde",
    [["Venezuela", "Brasil"], ["Venezuela", "Peru"], ["Peru", "Brasil"], ["Peru", "Argentina"], ["Brasil", "Argentina"]],
    [["Venezuela", 30, "roxo"], ["Brasil", 1, "verde"], ["Peru", 3, "verde"], ["Argentina", 42, "verde"]]
)

print(resultado)

print(mover_tropas("verde",
[["Egito", "Argelia"], ["Egito", "Sudao"], ["Argelia", "Sudao"],
["Argelia", "Congo"], ["Sudao", "Congo"], ["Sudao", "Madagascar"],
["Sudao", "Africa_do_Sul"],["Congo", "Africa_do_Sul"], ["Madagascar",
"Africa_do_Sul"]],
[["Egito", 4, "azul"], ["Argelia", 1, "azul"], ["Sudao", 7, "verde"],
["Congo", 3, "amarelo"],["Africa_do_Sul", 4, "verde"], ["Madagascar", 5,
"verde"]])) # [("Madagascar", "Africa_do_Sul")]

print(mover_tropas("azul",[["Venezuela","Brasil"],["Venezuela","Peru"],["Peru",
"Brasil"],["Peru","Argentina"],["Brasil","Argentina"]],
[["Venezuela",10,"verde"],["Brasil",20,"verde"],["Peru",30,"verde"],
["Argentina", 40, "verde"]])) # []

print(mover_tropas("amarelo", [["RS", "SC"], ["SC", "PR"], ["PR", "SP"], ["SP",
"MG"], ["SP", "RJ"], ["MG", "BA"], ["RJ", "BA"], ["RJ", "ES"], ["ES",
"MG"], ["ES", "BA"], ["SE", "BA"]],
[["RS", 100, "amarelo"], ["SC", 40, "amarelo"], ["PR", 80, "verde"],
["SP", 200, "rosa"],
["RJ", 150, "amarelo"], ["MG", 120, "amarelo"], ["BA", 150, "amarelo"],
["ES", 50, "amarelo"], ["SE", 30, "branco"]])) # [("RS", “SC”), ("ES", “MG”)]