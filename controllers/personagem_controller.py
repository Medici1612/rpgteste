from flask import Blueprint, render_template, request, redirect, url_for, session
import json
import os
from models.personagem import Personagem
from models.racas.humano import Humano
from models.racas.elfo import Elfo
from models.racas.anao import Anao
from models.racas.halfling import Halfling
from models.classes.guerreiro import Guerreiro
from models.classes.clerigo import Clerigo
from models.classes.ladrao import Ladrao
from models.classes.mago import Mago
from models.utils.atributos import MetodoClassico, MetodoLivre, MetodoHeroico

personagem_bp = Blueprint("personagem", __name__)

@personagem_bp.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        nome = request.form.get("nome")
        raca = request.form.get("raca")
        classe = request.form.get("classe")
        metodo = request.form.get("metodo")

        racas_map = {"humano": Humano(), "elfo": Elfo(), "anao": Anao(), "halfling": Halfling()}
        classes_map = {"guerreiro": Guerreiro(), "clerigo": Clerigo(), "ladrao": Ladrao(), "mago": Mago()}
        metodos_map = {"classico": MetodoClassico(), "livre": MetodoLivre(), "heroico": MetodoHeroico()}

        personagem = Personagem(nome, racas_map[raca], classes_map[classe], metodos_map[metodo])

        # Salvar em JSON
        personagem_dict = {
            "nome": personagem.nome,
            "raca": personagem.raca.nome,
            "classe": personagem.classe.nome,
            "atributos": personagem.atributos.to_dict(),
            "habilidades_raca": personagem.raca.habilidades(),
            "habilidades_classe": personagem.classe.habilidades(),
            "movimento": personagem.raca.movimento,
            "infravisao": personagem.raca.infravisao,
            "dado_vida": personagem.classe.dado_vida,
            "armaduras": personagem.classe.armaduras,
            "armas": personagem.classe.armas
        }

        caminho_arquivo = os.path.join(os.getcwd(), "personagem.json")
        with open(caminho_arquivo, "w", encoding="utf-8") as f:
            json.dump(personagem_dict, f, ensure_ascii=False, indent=4)

        # Salvar na sessão para exibir na ficha
        session["personagem"] = personagem_dict

        return redirect(url_for("personagem.ficha"))

    return render_template("index.html")


@personagem_bp.route("/ficha")
def ficha():
    personagem = session.get("personagem")
    if not personagem:
        return redirect(url_for("personagem.index"))
    return render_template("ficha.html", personagem=personagem)


@personagem_bp.route("/personagem-salvo")
def personagem_salvo():
    caminho_arquivo = os.path.join(os.getcwd(), "personagem.json")
    if os.path.exists(caminho_arquivo):
        with open(caminho_arquivo, "r", encoding="utf-8") as f:
            personagem = json.load(f)
        return render_template("ficha.html", personagem=personagem)
    return "Nenhum personagem salvo ainda."
