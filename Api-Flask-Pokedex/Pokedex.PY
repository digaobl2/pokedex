from flask import Flask, render_template

# Cria uma instância do aplicativo Flask
app = Flask(__name__)

# Define uma rota para a página inicial
@app.route('/')
def index():
    return render_template('index.html')

# Executa o aplicativo Flask
if __name__ == '__main__':
    app.run(debug=True)