# 🔐 Password Guardian Web

## 🚀 Visão Geral

O **Password Guardian Web** é uma aplicação web educacional desenvolvida em **Python** com o framework **Flask**. Seu objetivo é conscientizar sobre a importância de senhas seguras, permitindo que qualquer pessoa gere senhas fortes e avalie a robustez de suas próprias senhas de forma simples, visual e didática.

A aplicação oferece um gerador de senhas personalizável e um avaliador de força de senha, ambos com interface moderna, responsiva e fácil de usar, ideal para fins educativos e para o dia a dia.

---

## 🛠 Tecnologias Utilizadas

### **Python 3.10+**
- Linguagem de alto nível, utilizada para toda a lógica de backend e geração/avaliação de senhas.

### **Flask**
- Framework web minimalista e poderoso para Python.
- Responsável por servir as rotas, processar requisições AJAX e renderizar a interface.

### **Bootstrap 5**
- Biblioteca CSS para layout responsivo e visual moderno.
- Utilizada via CDN para estilização rápida e eficiente.

### **HTML5, CSS3 e JavaScript**
- Estruturam e dinamizam a interface do usuário.
- JavaScript faz a comunicação AJAX com o backend e atualiza a barra de progresso.

### **Gunicorn**
- Servidor WSGI utilizado para deploy em produção (Render).

---

## 📋 Funcionalidades Implementadas

- **Gerador de Senhas Fortes**
  - Personalize o tamanho (6 a 50 caracteres).
  - Escolha incluir letras maiúsculas, minúsculas, números e símbolos.
  - Geração segura usando a biblioteca `secrets`.
  - Botão para copiar a senha gerada.

- **Avaliador de Força de Senha**
  - Digite qualquer senha e veja a pontuação de 0 a 100.
  - Barra de progresso colorida (vermelho, amarelo, verde) indicando a força.
  - Mensagens explicativas e dicas para melhorar a senha.
  - Algoritmo avalia tamanho, variedade de caracteres, padrões repetidos/sequenciais e palavras comuns.

- **Interface Responsiva**
  - Layout adaptado para desktop e celular.
  - Visual limpo, moderno e educacional.

---

## 💡 Como Executar o Projeto

### Pré-requisitos
- **Python 3.10 ou superior**
- **pip** (gerenciador de pacotes Python)

### Passos para Executar Localmente

1. **Clone o Repositório**
    ```bash
    git clone https://github.com/BrunoAV1/password-guardian-web.git
    cd password-guardian-web
    ```
2. **Instale as dependências**
    ```bash
    pip install -r requirements.txt
    ```
3. **Execute a aplicação**
    ```bash
    python app.py
    ```
4. **Acesse no navegador**
    - Abra [http://localhost:5000](http://localhost:5000)


---

## 📁 Estrutura do Projeto

```
password-guardian-web/
├── app.py                # App Flask principal
├── requirements.txt      # Dependências
├── Procfile              # Comando para deploy no Render
├── README.md             # Documentação
├── /src                  # Código Python modularizado
│   └── password_utils.py # Funções de geração e avaliação
├── /static               # CSS, JS, imagens
├── /templates            # HTML (Jinja2)
```

---

## 🤝 Contribuições
Este projeto é aberto para contribuições! Sinta-se à vontade para sugerir melhorias, reportar bugs ou enviar pull requests. Algumas ideias de contribuição:
- Adicionar suporte a outros idiomas.
- Melhorar o algoritmo de avaliação de senha.
- Criar novos temas visuais para a interface.
- Adicionar testes automatizados.

---

## 🧑‍💻 Desenvolvedor
### Bruno Araujo de Vasconcellos

Este projeto foi desenvolvido como parte do meu aprendizado contínuo em desenvolvimento de software, com foco em segurança da informação e boas práticas de programação. O objetivo é criar ferramentas úteis, educativas e de fácil acesso para todos!

---

## 🏷️ Tags
python, flask, cybersecurity, password, web, educacional

---

## 🌐 Demonstração Online

Você pode acessar e testar o Password Guardian Web diretamente pelo navegador, sem precisar instalar nada:

👉 [Acesse aqui a versão online!](https://password-guardian-web.onrender.com)



