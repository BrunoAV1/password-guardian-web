import secrets
import string
import re

# Lista de palavras comuns para penalizar senhas fracas
COMMON_PASSWORDS = [
    'senha', 'password', '123456', 'qwerty', 'abc123', 'admin', 'letmein', 'welcome', 'monkey', 'login', '123456789', 'iloveyou', '123123', '000000', 'senha123', 'oi', 'meunome'
]

def gerar_senha(tamanho=12, maiusculas=True, minusculas=True, numeros=True, simbolos=True):
    """
    Gera uma senha forte e aleatória usando a biblioteca secrets.
    Parâmetros:
        tamanho (int): tamanho da senha
        maiusculas (bool): incluir letras maiúsculas
        minusculas (bool): incluir letras minúsculas
        numeros (bool): incluir números
        simbolos (bool): incluir símbolos
    Retorna:
        str: senha gerada
    """
    if tamanho < 6 or tamanho > 50:
        raise ValueError('O tamanho da senha deve ser entre 6 e 50.')
    caracteres = ''
    if maiusculas:
        caracteres += string.ascii_uppercase
    if minusculas:
        caracteres += string.ascii_lowercase
    if numeros:
        caracteres += string.digits
    if simbolos:
        caracteres += string.punctuation
    if not caracteres:
        raise ValueError('Selecione pelo menos um tipo de caractere.')
    senha = ''.join(secrets.choice(caracteres) for _ in range(tamanho))
    return senha

def avaliar_forca_senha(senha):
    """
    Avalia a força de uma senha e retorna pontuação e mensagem.
    Critérios: tamanho, variedade, padrões, palavras comuns.
    Retorna:
        dict: {'pontuacao': int, 'mensagem': str, 'cor': str}
    """
    pontuacao = 0
    mensagem = ''
    cor = 'danger'
    tamanho = len(senha)
    # Penaliza senhas muito curtas
    if tamanho < 6:
        return {'pontuacao': 5, 'mensagem': 'Senha muito curta', 'cor': 'danger'}
    # Pontuação por tamanho
    if tamanho >= 12:
        pontuacao += 30
    elif tamanho >= 8:
        pontuacao += 20
    else:
        pontuacao += 10
    # Variedade de caracteres
    tipos = 0
    if re.search(r'[A-Z]', senha):
        tipos += 1
    if re.search(r'[a-z]', senha):
        tipos += 1
    if re.search(r'[0-9]', senha):
        tipos += 1
    if re.search(r'[^A-Za-z0-9]', senha):
        tipos += 1
    pontuacao += tipos * 15
    # Penaliza padrões repetidos
    if re.search(r'(.)\1{2,}', senha):
        pontuacao -= 10
        mensagem = 'Evite caracteres repetidos.'
    # Penaliza sequências comuns
    if re.search(r'(012|123|234|345|456|567|678|789|890|abc|bcd|cde|def|qwe|asd)', senha.lower()):
        pontuacao -= 10
        mensagem = 'Evite sequências previsíveis.'
    # Penaliza palavras comuns
    for palavra in COMMON_PASSWORDS:
        if palavra in senha.lower():
            pontuacao -= 20
            mensagem = 'Evite palavras comuns.'
            break
    # Garante que a pontuação fique entre 0 e 100
    pontuacao = max(0, min(100, pontuacao))
    # Define cor e mensagem final
    if pontuacao < 40:
        cor = 'danger'
        if not mensagem:
            mensagem = 'Senha fraca: aumente o tamanho e varie os caracteres.'
    elif pontuacao < 70:
        cor = 'warning'
        if not mensagem:
            mensagem = 'Senha média: pode ser melhorada com mais variedade.'
    else:
        cor = 'success'
        mensagem = 'Senha forte!'
    return {'pontuacao': pontuacao, 'mensagem': mensagem, 'cor': cor} 