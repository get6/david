# python3 -m pip install --user flask
from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return '상단에 /menu 를 추가해주세요'

@app.route('/menu')
def menu():
    return render_template('menu.html')

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)