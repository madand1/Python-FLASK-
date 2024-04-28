from flask import Flask, render_template, request, redirect, url_for, abort
import json


app = Flask(__name__)

# Cargar datos del archivo JSON
with open('nobel.json') as f:
    nobel_data = json.load(f)

# Ruta para la página principal
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para el formulario de búsqueda
@app.route('/search_form')
def search_form():
    return render_template('search_form.html')



from flask import abort

# Ruta para procesar los resultados de búsqueda
@app.route('/search_results', methods=['POST'])
def search_results():
    search_term = request.form.get('search_term', '')
    search_year = request.form.get('search_year', '')

    # Verificar si no se proporciona ningún término de búsqueda y ningún año
    if not search_term and not search_year:
        # Mostrar todos los datos del json si no meto nada
        results = nobel_data
    else:
        # Filtrar los resultados según el término de búsqueda y el año
        results = []
        for item in nobel_data:
            for laureate in item.get('laureates', []):
                full_name = f"{laureate.get('firstname', '').lower()} {laureate.get('surname', '').lower()}"
                if (not search_term or search_term.lower() == full_name) and \
                   (not search_year or str(item['year']) == search_year):
                    results.append(item)
                    break  # Salir del bucle interior si se encuentra una coincidencia

        # Verificar si no se encontraron resultados para el término de búsqueda y el año
        if not results:
            # Si no se encontraron resultados, redirigir a la página de error 404
            abort(404)

    return render_template('search_results.html', results=results)




#POrque es lo que nos dara la ip para verlo


app.run("0.0.0.0",5000,debug=True)
