from flask import Flask, render_template, request, jsonify
from src.password_utils import gerar_senha, avaliar_forca_senha
import os

app = Flask(__name__)

@app.route('/')
def index():
    """
    Rota principal: renderiza a página única com as duas funcionalidades.
    """
    return render_template('index.html')

@app.route('/gerar_senha', methods=['POST'])
def gerar_senha_route():
    """
    Rota AJAX para geração de senha personalizada.
    """
    data = request.json
    try:
        senha = gerar_senha(
            tamanho=int(data.get('tamanho', 12)),
            maiusculas=data.get('maiusculas', True),
            minusculas=data.get('minusculas', True),
            numeros=data.get('numeros', True),
            simbolos=data.get('simbolos', True)
        )
        return jsonify({'senha': senha})
    except Exception as e:
        return jsonify({'erro': str(e)}), 400

@app.route('/avaliar_senha', methods=['POST'])
def avaliar_senha_route():
    """
    Rota AJAX para avaliação de força de senha.
    """
    data = request.json
    senha = data.get('senha', '')
    resultado = avaliar_forca_senha(senha)
    return jsonify(resultado)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port) 