def inverter_string(palavra):
    """
    Inverte uma string manualmente, caractere por caractere.

    Percorre a string do final para o início e constrói uma nova string invertida.
    Exemplo: "abcde" se torna "edcba".

    :param palavra: String a ser invertida.
    :return: String invertida.
    """
    invertida = ""  # Inicializa uma string vazia para armazenar o resultado invertido

    # Definindo variáveis explicativas para os valores do range
    inicio = len(palavra) - 1  # Último índice da string
    fim = -1  # Limite inferior (exclusivo)
    passo = -1  # Passo negativo para percorrer de trás para frente

    # Explicação do range(inicio, fim, passo):
    # - inicio: Começa no último índice da string.
    # - fim: Define o limite inferior (exclusivo). O loop para antes de chegar a -1, ou seja, inclui o índice 0.
    # - passo: Define o passo do loop. Um passo negativo faz o loop percorrer a string de trás para frente.
    # Resultado: range(inicio, fim, passo) gera a sequência de índices [4, 3, 2, 1, 0] para "abcde".

    # Loop que percorre a string de trás para frente
    for i in range(inicio, fim, passo):
        # Explicação do que acontece em cada iteração:
        # - i é o índice atual, começando do último caractere até o primeiro.
        # - palavra[i] acessa o caractere no índice i.
        # - invertida += palavra[i] adiciona o caractere ao final da string invertida.

        # Exemplo para palavra = "abcde":
        # 1ª iteração: i = 4, palavra[4] = "e", invertida = "e"
        # 2ª iteração: i = 3, palavra[3] = "d", invertida = "ed"
        # 3ª iteração: i = 2, palavra[2] = "c", invertida = "edc"
        # 4ª iteração: i = 1, palavra[1] = "b", invertida = "edcb"
        # 5ª iteração: i = 0, palavra[0] = "a", invertida = "edcba"

        invertida += palavra[i]  # Adiciona o caractere atual ao final da string invertida

    return invertida  # Retorna a string invertida

def corrigir_email(email):
    """
    Corrige um e-mail embaralhado.

    O e-mail é dividido em duas metades, cada metade é invertida e, em seguida,
    as metades invertidas são unidas para formar o e-mail corrigido.
    Se o domínio do e-mail corrigido não for "@usp.br", retorna "ERRO".

    :param email: E-mail embaralhado.
    :return: E-mail corrigido ou "ERRO" se o domínio estiver incorreto.
    """
    # Calcula o ponto de divisão (metade do e-mail)
    metade = len(email) // 2

    # Divide o e-mail em duas partes
    parte_esquerda = email[:metade]
    parte_direita = email[metade:]

    # Inverte as duas partes
    parte_esquerda_invertida = inverter_string(parte_esquerda)
    parte_direita_invertida = inverter_string(parte_direita)

    # Junta as partes invertidas para formar o e-mail corrigido
    email_corrigido = parte_esquerda_invertida + parte_direita_invertida

    # Verifica se o domínio está correto
    if email_corrigido.endswith("@usp.br"):
        return email_corrigido
    else:
        return "ERRO"


def corrige_emails(emails):
    """
    Corrige uma lista de e-mails embaralhados.

    Para cada e-mail na lista, aplica a função `corrigir_email` e retorna uma lista
    com os e-mails corrigidos ou "ERRO" para e-mails com domínio incorreto.

    :param emails: Lista de e-mails embaralhados.
    :return: Lista de e-mails corrigidos ou "ERRO".
    """
    return [corrigir_email(email) for email in emails]