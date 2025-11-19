from flask import Flask
from controllers.personagem_controller import personagem_bp

app = Flask(__name__)
app.secret_key = "segredo_super_seguro"  # Necessário para sessões

# Registrar blueprint
app.register_blueprint(personagem_bp)

if __name__ == "__main__":
    app.run(debug=True)
