# 🐉 OLD DRAGON RPG - Flask + MVC + JSON Save

Este projeto é uma adaptação do sistema de criação de personagens do RPG **Old Dragon**, transformado em uma aplicação web utilizando **Flask**, arquitetura **MVC** e agora com **persistência em arquivo JSON**.

---

## ✅ Funcionalidades
✔ Criação de personagem com:
- Nome
- Raça (Humano, Elfo, Anão, Halfling)
- Classe (Guerreiro, Clérigo, Ladrão, Mago)
- Método de geração de atributos:
  - Clássico (3d6 em ordem)
  - Aventureiro (3d6 livre)
  - Heróico (4d6 drop lowest)

✔ Exibição da ficha completa no navegador.

✔ **Novo:** Salva a instância do personagem criado em um arquivo `personagem.json` usando `.__dict__`.

---

## ✅ Arquitetura MVC
- **Model** → Classes do RPG (Personagem, Raças, Classes, Métodos).
- **View** → Templates HTML com Bootstrap.
- **Controller** → Rotas Flask que conectam Model e View.

Estrutura:
```
rpg_flask/
├── app.py                # Ponto de entrada Flask
├── controllers/
│    ├── personagem_controller.py
├── models/
│    ├── personagem.py
│    ├── racas/
│    ├── classes/
│    ├── utils/
├── templates/
│    ├── index.html
│    ├── ficha.html
├── static/
│    ├── style.css
├── personagem.json       # Arquivo gerado com os dados do personagem
```
## ✅ Como rodar 
 1. Instale Flask:
```bash
 pip install flask
```
 3. Execute:
 ```bash
python app.py
```
 5. Acesse:
 ```bash
 (http://127.0.0.1:5000/)
 ```
