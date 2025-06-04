
const formGerar = document.getElementById('form-gerar');
const senhaGerada = document.getElementById('senha-gerada');
const erroGerar = document.getElementById('erro-gerar');
formGerar.addEventListener('submit', async function(e) {
    e.preventDefault();
    erroGerar.textContent = '';
    const tamanho = document.getElementById('tamanho').value;
    const maiusculas = document.getElementById('maiusculas').checked;
    const minusculas = document.getElementById('minusculas').checked;
    const numeros = document.getElementById('numeros').checked;
    const simbolos = document.getElementById('simbolos').checked;
    try {
        const resp = await fetch('/gerar_senha', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({ tamanho, maiusculas, minusculas, numeros, simbolos })
        });
        const data = await resp.json();
        if (data.senha) {
            senhaGerada.value = data.senha;
        } else {
            senhaGerada.value = '';
            erroGerar.textContent = data.erro || 'Erro ao gerar senha.';
        }
    } catch (err) {
        senhaGerada.value = '';
        erroGerar.textContent = 'Erro de conexão.';
    }
});

const btnCopiar = document.getElementById('btn-copiar');
btnCopiar.addEventListener('click', function() {
    if (senhaGerada.value) {
        navigator.clipboard.writeText(senhaGerada.value);
        btnCopiar.textContent = 'Copiado!';
        setTimeout(() => btnCopiar.textContent = 'Copiar', 1200);
    }
});

const senhaAvaliar = document.getElementById('senha-avaliar');
const barraForca = document.getElementById('barra-forca');
const mensagemForca = document.getElementById('mensagem-forca');
senhaAvaliar.addEventListener('input', async function() {
    const senha = senhaAvaliar.value;
    if (!senha) {
        barraForca.style.width = '0%';
        barraForca.className = 'progress-bar bg-danger';
        barraForca.textContent = '0';
        mensagemForca.textContent = '';
        return;
    }
    const resp = await fetch('/avaliar_senha', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({ senha })
    });
    const data = await resp.json();
    barraForca.style.width = data.pontuacao + '%';
    barraForca.textContent = data.pontuacao;
    barraForca.className = 'progress-bar bg-' + (data.cor === 'danger' ? 'danger' : (data.cor === 'warning' ? 'warning' : 'success'));
    mensagemForca.textContent = data.mensagem;
}); 