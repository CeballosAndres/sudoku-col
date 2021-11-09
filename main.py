from flask import Flask, json, render_template, request, jsonify, redirect
from sudoku import Sudoku

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
    sudoku_input = request.form['sudoku_input']
    sudoku = Sudoku(sudoku_input)
    if sudoku_algorithm == 'dump':
        response = sudoku.dump()
    return jsonify({'status': 'ok', 'body': response})
    
   

