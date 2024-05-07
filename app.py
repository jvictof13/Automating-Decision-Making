from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def index():
    print(escolher_anime())
    return render_template('index.html',anime=escolher_anime())

@app.route('/escolher_anime',methods=['POST'])
def anime():
    return render_template('index.html',anime=escolher_anime())

def escolher_anime():
    animes = [
    {
        "nome": "Attack on Titan",
        "capa": "https://m.media-amazon.com/images/I/71oYp0Y7bxL._AC_UF1000,1000_QL80_DpWeblab_.jpg",
        "pais": "Japão",
        "episodios": 75
    },
    {
        "nome": "My Hero Academia",
        "capa": "https://images.justwatch.com/poster/261483319/s718/boku-no-hero-academia.jpg",
        "pais": "Japão",
        "episodios": 113
    },
    {
        "nome": "Naruto",
        "capa": "https://m.media-amazon.com/images/I/81nFG+aE64L._AC_UF1000,1000_QL80_.jpg",
        "pais": "Japão",
        "episodios": 220
    },
    {
        "nome": "One Piece",
        "capa": "https://m.media-amazon.com/images/I/91ZJ8D9pmkL._AC_UF1000,1000_QL80_DpWeblab_.jpg",
        "pais": "Japão",
        "episodios": 1000
    }
]

    anime_escolhido = random.choice(animes)
    return anime_escolhido

if __name__ == '__main__':
    app.run(debug=True)
