from flask import Flask, json, render_template, request, jsonify, redirect
from sudoku import Sudoku
import numpy as np
import time

app = Flask(__name__)


@app.errorhandler(404)
def not_found(error):
    return '<H1>Página no encontrada</H1>'


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resolve', methods=['POST'])
def resolve():
    # Almacenar la generación en el caso del algoritmo genetico
    generation = None
    # Obtener nombre del algoritmo a resolver
    sudoku_algorithm = request.form['sudoku_algorithm']
    if sudoku_algorithm not in ['profundidad', 'backtracking','genetico']:
        return jsonify({'status': 'error', 'type': 'Algoritmo no seleccionado'})
    # Obtener entrada de sudoku: "1,2,3,4,5,6,7,..."
    sudoku_input = request.form['sudoku_input']
    try:
        # Instanciar clase sudoku
        sudoku = Sudoku(sudoku_input)
        # Medición del tiempo que le toma al algoritmo resolver el problema
        start = time.time()
        # Resolución con diferentes algoritmos
        if sudoku_algorithm == 'profundidad':
            response = sudoku.dfs()
        elif sudoku_algorithm == 'backtracking':
            response = sudoku.backtracking()
        elif sudoku_algorithm == 'genetico':
            genetic_elements = sudoku.genetic()
            response = genetic_elements[0]
            generation = genetic_elements[1]
        time_of_resolution = time.time() - start
        
        # Permitir serializar a json en caso de ser objeto numpy
        if type(response) is not list:
            response = response.tolist()

        return jsonify({'status': 'ok', 'body': response, 'time':
            time_of_resolution, 'generation': generation})
    except:
        return jsonify({'status': 'error', 'type': 'Error al resolver Sudoku'})
