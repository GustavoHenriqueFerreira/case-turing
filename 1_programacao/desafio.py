from collections import deque

# Função para calcular a distância mínima entre dois territórios no grafo usando BFS
def calcular_distancia(grafo, origem, destino):
    """
    Calcula a distância mínima entre dois territórios usando busca em largura (BFS).
    
    :param grafo: Dicionário que representa o grafo de vizinhança.
    :param origem: Território de origem.
    :param destino: Território de destino.
    :return: Distância mínima entre os territórios ou infinito se não houver caminho.
    """
    fila = deque([origem])  # Fila para a busca em largura
    distancias = {origem: 0}  # Dicionário para armazenar as distâncias
    
    while fila:
        atual = fila.popleft()  # Pega o próximo território da fila
        if atual == destino:
            return distancias[atual]  # Retorna a distância se chegou ao destino
        
        for vizinho in grafo.get(atual, []):  # Percorre os vizinhos
            if vizinho not in distancias:  # Se o vizinho ainda não foi visitado
                distancias[vizinho] = distancias[atual] + 1  # Atualiza a distância
                fila.append(vizinho)  # Adiciona o vizinho à fila
    
    return float('inf')  # Retorna infinito se não houver caminho


# Função para construir o grafo de vizinhança a partir de uma lista de pares de territórios
def construir_grafo(conexoes_territorios):
    """
    Constrói um grafo de vizinhança a partir de uma lista de conexões entre territórios.

    Um grafo é uma estrutura de dados que representa relações entre entidades (neste caso, territórios).
    Cada território é um nó, e cada conexão entre dois territórios é uma aresta.

    :param conexoes_territorios: Lista de pares de territórios conectados.
                                 Cada par é uma lista ou tupla com dois territórios.
                                 Exemplo: [["Venezuela", "Brasil"], ["Brasil", "Argentina"]]

    :return: Dicionário representando o grafo de vizinhança.
             - Cada chave é um território (nó).
             - Cada valor é uma lista de territórios vizinhos (nós conectados).
             Exemplo: {"Venezuela": ["Brasil"], "Brasil": ["Venezuela", "Argentina"], "Argentina": ["Brasil"]}
    """
    grafo = {}  # Dicionário que armazenará o grafo de vizinhança

    # Itera sobre cada par de territórios conectados
    for territorio_a, territorio_b in conexoes_territorios:
        # Se o território A ainda não está no grafo, adiciona-o com uma lista vazia de vizinhos
        if territorio_a not in grafo:
            grafo[territorio_a] = []

        # Se o território B ainda não está no grafo, adiciona-o com uma lista vazia de vizinhos
        if territorio_b not in grafo:
            grafo[territorio_b] = []

        # Adiciona o território B como vizinho do território A
        grafo[territorio_a].append(territorio_b)

        # Adiciona o território A como vizinho do território B
        grafo[territorio_b].append(territorio_a)

    return grafo  # Retorna o grafo completo


# Função para filtrar os territórios pertencentes a um jogador específico
def obter_territorios_jogador(cor_jogador, tropas):
    """
    Filtra os territórios que pertencem a um jogador específico.
    
    :param cor_jogador: Cor do jogador.
    :param tropas: Lista de tuplas contendo (território, tropas, dono).
    :return: Dicionário com os territórios e suas tropas pertencentes ao jogador.
    """
    return {territorio: tropas for territorio, tropas, dono in tropas if dono == cor_jogador}


# Função para encontrar inimigos vizinhos de um território
def encontrar_vizinhos_inimigos(grafo, tropas, cor_jogador, territorio):
    """
    Encontra os vizinhos inimigos de um território específico.

    Um vizinho inimigo é um território conectado ao território atual que pertence a um jogador diferente.

    :param grafo: Dicionário que representa o grafo de vizinhança.
                  Exemplo: {"A": ["B", "C"], "B": ["A"], "C": ["A"]}
    :param tropas: Lista de tuplas contendo informações sobre os territórios.
                  Cada tupla tem o formato (nome_territorio, quantidade_tropas, cor_dono).
                  Exemplo: [("A", 10, "azul"), ("B", 5, "vermelho"), ("C", 8, "azul")]
    :param cor_jogador: Cor do jogador atual.
                        Exemplo: "azul"
    :param territorio: Nome do território atual.
                       Exemplo: "A"
    :return: Lista de territórios vizinhos que são inimigos.
             Exemplo: ["B"]
    """
    inimigos_vizinhos = []  # Lista para armazenar os vizinhos inimigos

    # Itera sobre os vizinhos do território atual
    for vizinho in grafo.get(territorio, []):
        # Itera sobre a lista de tropas para verificar o dono do território vizinho
        for nome_territorio, _, cor_dono in tropas:
            if nome_territorio == vizinho and cor_dono != cor_jogador:
                inimigos_vizinhos.append(vizinho)  # Adiciona o vizinho à lista de inimigos
                break  # Para de verificar este vizinho e passa para o próximo

    return inimigos_vizinhos  # Retorna a lista de vizinhos inimigos


# Função para calcular a menor distância entre um território e qualquer inimigo
def calcular_distancia_minima_para_inimigos(territorio, tropas, cor_jogador, grafo):
    """
    Calcula a menor distância entre um território e qualquer território inimigo.

    A distância é calculada usando a função `calcular_distancia`, que realiza uma busca em largura (BFS).

    :param territorio: Nome do território atual.
                       Exemplo: "A"
    :param tropas: Lista de tuplas contendo informações sobre os territórios.
                  Cada tupla tem o formato (nome_territorio, quantidade_tropas, cor_dono).
                  Exemplo: [("A", 10, "azul"), ("B", 5, "vermelho"), ("C", 8, "azul")]
    :param cor_jogador: Cor do jogador atual.
                        Exemplo: "azul"
    :param grafo: Dicionário que representa o grafo de vizinhança.
                  Exemplo: {"A": ["B", "C"], "B": ["A"], "C": ["A"]}
    :return: Menor distância até um território inimigo.
             Retorna infinito (float('inf')) se não houver inimigos.
    """
    menor_distancia = float('inf')  # Inicializa a menor distância como infinito

    # Itera sobre a lista de tropas para encontrar inimigos
    for nome_territorio, _, cor_dono in tropas:
        # Verifica se o território pertence a um inimigo
        if cor_dono != cor_jogador:
            # Calcula a distância entre o território atual e o território inimigo
            distancia = calcular_distancia(grafo, territorio, nome_territorio)
            
            # Atualiza a menor distância se a distância calculada for menor
            if distancia < menor_distancia:
                menor_distancia = distancia

    return menor_distancia  # Retorna a menor distância encontrada


# Função para determinar o melhor vizinho para mover tropas
def calcular_melhor_vizinho(territorio, vizinhos_do_territorio, tropas, cor_jogador, grafo):
    """
    Determina o melhor vizinho para mover tropas, considerando a distância até os inimigos e outras condições.
    
    :param territorio: Território atual.
    :param vizinhos_do_territorio: Lista de vizinhos do território.
    :param tropas: Lista de tuplas contendo (território, tropas, dono).
    :param cor_jogador: Cor do jogador.
    :param grafo: Grafo de vizinhança.
    :return: Melhor vizinho para mover tropas ou None se não houver.
    """
    melhor_vizinho = None
    menor_distancia = float('inf')
    menor_tropas = float('inf')
    melhor_nome_alfabetico = None
    
    # Obtém o número de tropas no território atual
    tropa_atual = next(tropa for t, tropa, dono in tropas if t == territorio and dono == cor_jogador)
    
    for vizinho in vizinhos_do_territorio:
        # Verifica se o vizinho pertence ao jogador
        if not any(nome_territorio == vizinho and cor_dono == cor_jogador for nome_territorio, _, cor_dono in tropas):
            continue  # Ignora vizinhos que não pertencem ao jogador
        
        # Calcula a distância mínima até os inimigos
        distancia_minima_inimigos = calcular_distancia_minima_para_inimigos(vizinho, tropas, cor_jogador, grafo)
        
        # Verifica se o vizinho atual é o melhor com base nas condições
        if (distancia_minima_inimigos < menor_distancia or
            (distancia_minima_inimigos == menor_distancia and tropa_atual < menor_tropas) or
            (distancia_minima_inimigos == menor_distancia and tropa_atual == menor_tropas and vizinho < melhor_nome_alfabetico)):
            
            melhor_vizinho = vizinho
            menor_distancia = distancia_minima_inimigos
            menor_tropas = tropa_atual
            melhor_nome_alfabetico = vizinho

    return melhor_vizinho


# Função principal que organiza a movimentação das tropas
def mover_tropas(cor, vizinhos, tropas):
    """
    Organiza a movimentação das tropas do jogador.
    
    :param cor: Cor do jogador.
    :param vizinhos: Lista de pares de territórios vizinhos.
    :param tropas: Lista de tuplas contendo (território, tropas, dono).
    :return: Lista de movimentações sugeridas.
    """
    try:
        grafo = construir_grafo(vizinhos)  # Constrói o grafo de vizinhança
        territorios_jogador = obter_territorios_jogador(cor, tropas)  # Filtra os territórios do jogador
        movimentacoes = []

        for territorio, tropa in territorios_jogador.items():
            if tropa > 1:  # Só movimenta se houver mais de 1 tropa
                vizinhos_do_territorio = grafo.get(territorio, [])
                inimigos_vizinhos = encontrar_vizinhos_inimigos(grafo, tropas, cor, territorio)
                
                # Verifica se o território atual não tem inimigos vizinhos
                if not inimigos_vizinhos:
                    melhor_vizinho = calcular_melhor_vizinho(territorio, vizinhos_do_territorio, tropas, cor, grafo)
                    
                    # Se houver um melhor vizinho, sugere a movimentação
                    if melhor_vizinho:
                        movimentacoes.append((territorio, melhor_vizinho))

        return movimentacoes
    except Exception as e:
        print(f"Erro ao mover tropas: {e}")
        return []  # Retorna uma lista vazia em caso de erro