# Função para inverter uma string
def inverter_string(s):
    """
    Recebe uma string e retorna sua versão invertida.
    """
    return s[::-1]

# Função para corrigir um único e-mail
def corrigir_email(email):
    """
    Recebe um e-mail embaralhado, divide-o, inverte as metades e verifica o domínio.
    Retorna o e-mail corrigido ou 'ERRO' se o domínio estiver errado.
    """
    n = len(email)
    
    # Calcula o ponto de divisão (metade do e-mail)
    metade = n // 2
    
    # Divide o e-mail em duas partes
    parte_esquerda = email[:metade]
    parte_direita = email[metade:]
    
    # Inverte as duas partes
    parte_esquerda_invertida = inverter_string(parte_esquerda)
    parte_direita_invertida = inverter_string(parte_direita)
    
    # Junta as duas partes invertidas para formar o e-mail corrigido
    email_corrigido = parte_esquerda_invertida + parte_direita_invertida
    
    # Verifica se o domínio está correto
    if email_corrigido.endswith("@usp.br"):
        return email_corrigido
    else:
        return "ERRO"

# Função principal para corrigir todos os e-mails
def corrige_emails(emails):
    """
    Recebe uma lista de e-mails e retorna uma lista com os e-mails corrigidos
    ou 'ERRO' quando o domínio estiver incorreto.
    """
    return [corrigir_email(email) for email in emails]

# Exemplos de teste para validar a solução

# Teste 1
emails_1 = [
    "id_atanerrb.psu@av",
    "t.alalalimacrb.repsu@ppo",
    ".orbmem_ovonrb.psu@gnirut"
]
print(corrige_emails(emails_1))  # Esperado: ["renata_diva@usp.br","ERRO","novo_membro.turing@usp.br"]

# Teste 2
emails_2 = [
    "sac_tsetrb.psu@1e",
    "c_tsetortuorb.psu@1esa",
    "c_tsetortuorb.5psu@1esa",
    ".ed.olpmexerb.psu@liame",
    "_odnatsetrb.psu@b1q",
    "tset_omitlurb.psu@esac"
]
print(corrige_emails(emails_2))  # Esperado: ["test_case1@usp.br", "outrotest_case1@usp.br", "ERRO", "exemplo.de.email@usp.br", "testando_q1b@usp.br", "ultimo_testcase@usp.br"]

# Teste 3
emails_3 = [
    "su@arb.p",
    "u@barb.ps",
    "slen@cbarb.psu.no"
]
print(corrige_emails(emails_3))  # Esperado: ["a@usp.br", "ab@usp.br", "ERRO"]

# Teste 4
emails_4 = [
    "am_ocuop_mu_e_liame_esserb.psu@sortuo_so_euq_roi",
    "slen@cbarb.psu.no"
]
print(corrige_emails(emails_4))  # Esperado: ["esse_email_e_um_pouco_maior_que_os_outros@usp.br", "ERRO"]
