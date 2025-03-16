def conta_correcoes(qtd_estados, transicoes, episodio, max_prof):
    """
    Calcula o número de correções possíveis para um episódio com lacunas em transições inválidas.
    
    Parâmetros:
    - qtd_estados (int): Número total de estados.
    - transicoes (dict): Dicionário de transições permitidas.
    - episodio (list): Lista de estados registrados no episódio.
    - max_prof (int): Número máximo de passos intermediários permitidos por lacuna.
    
    Retorna:
    - int: Número total de correções possíveis, -1 se não houver lacunas, 0 se alguma lacuna for irreparável.
    """
    
    # Função auxiliar: verifica se uma transição entre dois estados é permitida
    def transicao_valida(de_estado, para_estado):
        """Verifica se uma transição entre dois estados é permitida."""
        return transicoes.get((de_estado, para_estado), 0) == 1

    # Função auxiliar: encontra todas as lacunas (transições inválidas) no episódio
    def encontrar_lacunas():
        """Identifica todas as transições inválidas consecutivas no episódio."""
        lacunas = []
        
        # Percorre o episódio do primeiro ao penúltimo estado (para evitar índice fora do range)
        for i in range(len(episodio) - 1):
            # Estado atual na posição i do episódio
            estado_atual = episodio[i]
            # Próximo estado na posição i + 1 do episódio
            proximo_estado = episodio[i + 1]
            
            # Verifica se a transição do estado atual para o próximo é INVÁLIDA
            if not transicao_valida(estado_atual, proximo_estado):
                # Adiciona o par (atual, próximo) à lista de lacunas
                lacunas.append((estado_atual, proximo_estado))
        
        # Retorna a lista de lacunas encontradas no episódio
        return lacunas

    # Função recursiva: conta caminhos válidos entre dois estados com até max_prof passos extras
    def contar_caminhos(origem, destino, passos_restantes):
        """Calcula quantos caminhos válidos existem entre dois estados, 
        inserindo até `passos_restantes` estados intermediários."""
        # Caso base: se a transição direta é válida, conta como 1 caminho
        caminhos = 0
        if transicao_valida(origem, destino):
            caminhos += 1
        
        # Se ainda há passos restantes, explora intermediários
        if passos_restantes > 0:
            for intermediario in range(1, qtd_estados + 1):
                # Só continua se a transição para o intermediário for válida
                if transicao_valida(origem, intermediario):
                    # Chama recursivamente reduzindo os passos restantes
                    caminhos += contar_caminhos(intermediario, destino, passos_restantes - 1)
        return caminhos

    # Passo 1: Identificar lacunas no episódio
    lacunas = encontrar_lacunas()
    
    # Caso sem lacunas: retorna -1
    if not lacunas:
        return -1
    
    # Passo 2: Calcular correções para cada lacuna
    total_correcoes = 1
    for origem, destino in lacunas:
        # Calcula caminhos válidos para esta lacuna
        caminhos = contar_caminhos(origem, destino, max_prof)
        
        # Se alguma lacuna não tem correção, retorna 0
        if caminhos == 0:
            return 0
        
        # Multiplica o total pelas correções desta lacuna
        total_correcoes *= caminhos
    
    return total_correcoes