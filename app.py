from flask import Flask, render_template, request, session, redirect, url_for
from model.personagem import Personagem
from model.dado import Dado # Importamos Dado para usar na rota
from model.racas.humano import Humano
from model.racas.elfo import Elfo
from model.racas.anao import Anao
from model.classes.guerreiro import Guerreiro
from model.classes.clerigo import Clerigo
from model.classes.mago import Mago

app = Flask(__name__)
# A sessão do Flask precisa de uma 'chave secreta' para funcionar com segurança
app.secret_key = 'sua_chave_secreta_aqui' 

RACAS_MAP = {"humano": Humano(), "elfo": Elfo(), "anao": Anao()}
CLASSES_MAP = {"guerreiro": Guerreiro(), "clerigo": Clerigo(), "mago": Mago()}

@app.route('/')
def index():
    # Limpa a sessão antiga antes de começar um novo personagem
    session.clear()
    return render_template('index.html')

@app.route('/distribuir_atributos', methods=['POST'])
def distribuir_atributos():
    # Etapa 1: Pegar os dados iniciais e rolar os dados
    estilo_id = request.form.get('estilo_atributos', type=int)

    # Guarda os dados iniciais na sessão para usar depois
    session['personagem_data'] = {
        'nome': request.form.get('nome'),
        'raca_id': request.form.get('raca'),
        'classe_id': request.form.get('classe'),
        'estilo_id': estilo_id
    }

    # Se for estilo clássico, criamos o personagem direto
    if estilo_id == 1:
        return redirect(url_for('finalizar_personagem'))

    # Se for Aventureiro ou Heróico, rolamos os dados
    rolagens = []
    if estilo_id == 2: # Aventureiro
        for _ in range(6): rolagens.append(Dado.rolar(3, 6))
    else: # Heróico
        for _ in range(6): rolagens.append(Dado.rolar_com_descarte(4, 6, 1))
    
    # Guardamos os resultados na sessão e vamos para a página de distribuição
    session['rolagens'] = rolagens
    return render_template('distribuir.html', rolagens=rolagens)

@app.route('/finalizar_personagem', methods=['POST', 'GET'])
def finalizar_personagem():
    # Etapa 2: Recuperar dados da sessão e do formulário de distribuição
    dados = session.get('personagem_data')
    if not dados:
        return redirect(url_for('index')) # Se não tiver dados na sessão, volta pro início

    personagem = Personagem(dados['nome'])
    classe_obj = CLASSES_MAP[dados['classe_id']]
    personagem.classe = classe_obj

    if dados['estilo_id'] == 1:
        # Lógica para o Estilo Clássico (não interativo)
        personagem.definir_atributos(1, classe_obj)
    else:
        # Lógica para Aventureiro/Heróico (pega a distribuição do form)
        rolagens_originais = session.get('rolagens', [])
        distribuicao = {}
        # Pega os valores que o usuário escolheu no formulário
        for attr in personagem.atributos.keys():
            valor = request.form.get(attr, type=int)
            distribuicao[attr] = valor
        
        # Validação simples para garantir que os valores corretos foram usados
        if sorted(distribuicao.values()) != sorted(rolagens_originais):
            # Se os valores não baterem, redireciona de volta com erro
            return render_template('distribuir.html', rolagens=rolagens_originais, erro="Valores inválidos. Por favor, distribua os valores rolados.")

        # Atribui os valores escolhidos
        for attr, valor in distribuicao.items():
            personagem.atributos[attr]['valor'] = valor
            personagem.atributos[attr]['mod'] = personagem._calcular_modificador(valor)

    # Aplica bônus de raça e classe como antes
    raca_obj = RACAS_MAP[dados['raca_id']]
    personagem.raca = raca_obj
    raca_obj.aplicar_habilidades_raciais(personagem)
    classe_obj.aplicar_bonus_de_classe(personagem)
    
    return render_template('resultado.html', personagem=personagem)

if __name__ == '__main__':
    app.run(debug=True)