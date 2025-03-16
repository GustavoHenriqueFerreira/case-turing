def deslocar_caractere(char: str, deslocamento: int, base: int) -> str:
    """
    Desloca um caractere dentro do intervalo do alfabeto (maiúsculo ou minúsculo),
    considerando o deslocamento.
    
    Parâmetros:
    char (str): O caractere a ser deslocado.
    deslocamento (int): O número de posições que o caractere será deslocado.
    base (int): O código ASCII da primeira letra do alfabeto ('A' ou 'a').
    
    Retorna:
    str: O caractere deslocado.
    """
    posicao_original = ord(char) - base  # Posição no alfabeto (0 a 25)
    nova_posicao = (posicao_original + deslocamento) % 26  # Aplica o deslocamento
    return chr(base + nova_posicao)  # Retorna o novo caractere


def cifra(texto: str, deslocamento: int) -> str:
    """
    Aplica a Cifra de César a um texto, deslocando as letras do alfabeto pelo número especificado.
    
    Parâmetros:
    texto (str): A mensagem a ser cifrada ou decifrada.
    deslocamento (int): O número de posições que cada letra será deslocada.
    
    Retorna:
    str: O texto transformado pela cifra.
    """
    resultado = []  # Lista para armazenar os caracteres modificados
    
    # Ajusta deslocamentos negativos para seu equivalente positivo dentro do intervalo [0, 25]
    deslocamento = deslocamento % 26  # Isso garante que, por exemplo, -30 seja tratado como +22 (facilita o deslocamento)
    
    for char in texto:
        if 'A' <= char <= 'Z':  # Verifica se o caractere é uma letra maiúscula
            novo_char = deslocar_caractere(char, deslocamento, ord('A'))
        elif 'a' <= char <= 'z':  # Verifica se o caractere é uma letra minúscula
            novo_char = deslocar_caractere(char, deslocamento, ord('a'))
        else:
            novo_char = char  # Mantem caracteres nao alfabeticos (espacos, pontuacao, numeros, etc.)
        
        resultado.append(novo_char)  # Adiciona o caractere modificado a lista
    
    return ''.join(resultado)  # Retorna a lista como uma string

# Testes
# Teste 1: Cifra de César com deslocamento +2
print(cifra("Y npcqqy c glgkgey by ncpdcgaym", 2))  # Esperado: "A pressa e inimiga da perfeicao"

# Teste 2: Cifra de César com deslocamento -30 (equivalente a deslocamento +22)
print(cifra("jmpls hi xyvmrkiv, xyvmrkymrls i.", -30))  # Esperado: "filho de turinger, turinguinho e."