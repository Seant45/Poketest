from flask import Flask, render_template, request
import requests
#Run using python -m flask --app poketest run
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    pokemon = request.form['pokemon'].lower()
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        name = data['name'].capitalize()
        types = [t['type']['name'].capitalize() for t in data['types']]
        abilities = [a['ability']['name'].replace('-', ' ').capitalize() for a in data['abilities']]
        sprite = data['sprites']['front_default']
        height = data['height'] / 10  # meters
        weight = data['weight'] / 10  # kilograms

        return render_template('result.html', name=name, types=types, abilities=abilities,
                               sprite=sprite, height=height, weight=weight)
    else:
        error = "Pokémon not found. Please check the name or ID."
        return render_template('index.html', error=error)

if __name__ == '__main__':
    app.run(debug=True)


