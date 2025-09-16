from flask import Flask, render_template, request, session, redirect, url_for
from model.personagem import Personagem
from model.dado import Dado
from model.racas.humano import Humano
from model.racas.elfo import Elfo
from model.racas.anao import Anao
from model.classes.guerreiro import Guerreiro
from model.classes.clerigo import Clerigo
from model.classes.mago import Mago

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta_aqui' 

RACAS_MAP = {"humano": Humano(), "elfo": Elfo(), "anao": Anao()}
CLASSES_MAP = {"guerreiro": Guerreiro(), "clerigo": Clerigo(), "mago": Mago()}

@app.route('/')
def index():
    session.clear()
    return render_template('index.html')

@app.route('/distribuir_atributos', methods=['POST'])
def distribuir_atributos():
    estilo_id = request.form.get('estilo_atributos', type=int)

    session['personagem_data'] = {
        'nome': request.form.get('nome'),
        'raca_id': request.form.get('raca'),
        'classe_id': request.form.get('classe'),
        'estilo_id': estilo_id
    }

    if estilo_id == 1:
        return redirect(url_for('finalizar_personagem'))

    rolagens = []
    if estilo_id == 2:
        for _ in range(6): rolagens.append(Dado.rolar(3, 6))
    else:
        for _ in range(6): rolagens.append(Dado.rolar_com_descarte(4, 6, 1))
    
    session['rolagens'] = rolagens
    return render_template('distribuir.html', rolagens=rolagens)

@app.route('/finalizar_personagem', methods=['POST', 'GET'])
def finalizar_personagem():
    dados = session.get('personagem_data')
    if not dados:
        return redirect(url_for('index'))

    personagem = Personagem(dados['nome'])
    classe_obj = CLASSES_MAP[dados['classe_id']]
    personagem.classe = classe_obj

    if dados['estilo_id'] == 1:
        personagem.definir_atributos(1, classe_obj)
    else:
        rolagens_originais = session.get('rolagens', [])
        distribuicao = {}
        
        for attr in personagem.atributos.keys():
            valor = request.form.get(attr, type=int)
            distribuicao[attr] = valor
        
        if sorted(distribuicao.values()) != sorted(rolagens_originais):
            return render_template('distribuir.html', rolagens=rolagens_originais, erro="Valores inválidos. Por favor, distribua os valores rolados.")

        for attr, valor in distribuicao.items():
            personagem.atributos[attr]['valor'] = valor
            personagem.atributos[attr]['mod'] = personagem._calcular_modificador(valor)

    raca_obj = RACAS_MAP[dados['raca_id']]
    personagem.raca = raca_obj
    raca_obj.aplicar_habilidades_raciais(personagem)
    classe_obj.aplicar_bonus_de_classe(personagem)
    
    return render_template('resultado.html', personagem=personagem)

if __name__ == '__main__':
    app.run(debug=True)