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
    sudoku_algorithm = request.form['sudoku_algorithm']
    if sudoku_algorithm not in ['profundidad', 'backtracking']:
        return jsonify({'status': 'error', 'type': 'Algoritmo no seleccionado'})
    sudoku_input = request.form['sudoku_input']
    sudoku = Sudoku(sudoku_input)
    # Medición del tiempo que le toma al algoritmo resolver el problema
    start = time.time()
    # Resolución con diferentes algoritmos
    if sudoku_algorithm == 'profundidad':
        response = sudoku.dfs()
    elif sudoku_algorithm == 'backtracking':
        response = sudoku.backtracking()
    time_of_resolution = time.time() - start
    
    if type(response) is not list:
        response = response.tolist()

    print(response)
    return jsonify({'status': 'ok', 'body': response, 'time': time_of_resolution})
