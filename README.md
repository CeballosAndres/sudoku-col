# Sudoku game
Use of different algorithms for solving Sudoku game.

## Set environment

### Create virtual environment

`python3 -m venv env`

### Activate virtual environment

**On macOS**

`source env/bin/activate`

**On Windows** 

cmd `env\Scripts\activate.bat`

PowerShell `venv\Scripts\Activate.ps1`

### Install dependencies 

`pip install -r requirements.txt`

## Run

### Local

`python wsgi.py`

`gunicorn wsgi:app`

### Heroku

[HerokuApp](https://sudoku-col.herokuapp.com/)
