from collections import deque

def conta_correcoes(qtd_estados, transicoes, episodio, max_prof):
    def encontrar_caminhos(origem, destino, prof_max):
        """ Retorna o número de caminhos de 'origem' para 'destino' respeitando 'prof_max' """
        print(f"Buscando caminhos de {origem} para {destino} com profundidade máxima {prof_max}")

        if origem == destino:
            print(f"  Já estamos no destino ({origem} == {destino}) → 1 caminho")
            return 1  # Se já estamos no destino, é um caminho válido

        fila = deque([(origem, 0)])  # (estado_atual, profundidade)
        caminhos = 0

        while fila:
            estado_atual, profundidade = fila.popleft()

            if profundidade >= prof_max:
                continue  # Não podemos ultrapassar a profundidade máxima

            for prox_estado in range(1, qtd_estados + 1):
                if transicoes.get((estado_atual, prox_estado), 0) == 1:
                    if prox_estado == destino:
                        caminhos += 1  # Encontramos um caminho válido
                        print(f"  Caminho encontrado: {estado_atual} → {prox_estado}  (Total até agora: {caminhos})")
                    else:
                        fila.append((prox_estado, profundidade + 1))

        print(f"  Total de caminhos de {origem} para {destino}: {caminhos}")
        return caminhos

    total_correcoes = 1
    encontrou_lacuna = False  # Para verificar se houve necessidade de correção

    print(f"Analisando episódio: {episodio} com profundidade máxima {max_prof}")

    for i in range(len(episodio) - 1):
        origem, destino = episodio[i], episodio[i + 1]
        print(f"Verificando transição: {origem} → {destino}")

        if transicoes.get((origem, destino), 0) == 0:  # Não há transição direta
            print(f"  Falta transição direta de {origem} para {destino}")
            encontrou_lacuna = True
            caminhos_possiveis = encontrar_caminhos(origem, destino, max_prof)

            if caminhos_possiveis == 0:
                print(f"  Nenhum caminho encontrado → Retornando 0")
                return 0  # Se não há forma de corrigir a transição, retorna 0
            
            total_correcoes *= caminhos_possiveis  # Multiplica os caminhos possíveis
            print(f"  Multiplicando total_correcoes por {caminhos_possiveis} → {total_correcoes}")

    resultado = total_correcoes if encontrou_lacuna or total_correcoes > 1 else -1
    print(f"Resultado final: {resultado}")
    return resultado


# Testes com os exemplos fornecidos
print(conta_correcoes(3, {(1, 1): 1, (1, 2): 1, (1, 3): 0, (2, 1): 1, (2, 2): 0, (2, 3): 1, (3, 1): 1, (3, 2): 0, (3, 3): 0}, [1, 2, 3, 3, 2], 3))  # Output: 8
print(conta_correcoes(3, {(1, 1): 1, (1, 2): 1, (1, 3): 0, (2, 1): 1, (2, 2): 0, (2, 3): 1, (3, 1): 1, (3, 2): 0, (3, 3): 0}, [1, 2, 3, 1, 2], 1))  # Output: -1

# Input:
print(conta_correcoes(5,
{(1, 1): 0, (1, 2): 1, (1, 3): 1, (1, 4): 1, (1, 5): 0,
(2, 1): 0, (2, 2): 0, (2, 3): 0, (2, 4): 1, (2, 5): 1,
(3, 1): 1, (3, 2): 0, (3, 3): 1, (3, 4): 0, (3, 5): 0,
(4, 1): 1, (4, 2): 0, (4, 3): 1, (4, 4): 0, (4, 5): 0,
(5, 1): 0, (5, 2): 1, (5, 3): 0, (5, 4): 1, (5, 5): 1},
[1,2,3,4,5,4,3,2,1], 2))
# Output: 72

# Input:
print(conta_correcoes(5,
{(1, 1): 0, (1, 2): 1, (1, 3): 1, (1, 4): 1, (1, 5): 0,
(2, 1): 0, (2, 2): 0, (2, 3): 0, (2, 4): 1, (2, 5): 1,
(3, 1): 1, (3, 2): 0, (3, 3): 1, (3, 4): 0, (3, 5): 0,
(4, 1): 1, (4, 2): 0, (4, 3): 1, (4, 4): 0, (4, 5): 0,
(5, 1): 0, (5, 2): 1, (5, 3): 0, (5, 4): 1, (5, 5): 1},
[1,2,3,4,5,4,3,2,1], 1))
# Output: 0

# Input:
print(conta_correcoes(3,
{(1, 1): 1, (1, 2): 1, (1, 3): 0,
(2, 1): 1, (2, 2): 0, (2, 3): 1,
(3, 1): 1, (3, 2): 0, (3, 3): 0},
[1, 2, 3, 3, 2], 1))
# Output: 0

# Input:
print(conta_correcoes(4, {(1, 1): 0, (1, 2): 0, (1, 3): 1, (1, 4): 1,
(2, 1): 1, (2, 2): 0, (2, 3): 1, (2, 4): 0,
(3, 1): 0, (3, 2): 1, (3, 3): 0, (3, 4): 1,
(4, 1): 1, (4, 2): 1, (4, 3): 1, (4, 4): 1},

[3, 1, 3, 2, 2, 4], 3))
# Output: 1680