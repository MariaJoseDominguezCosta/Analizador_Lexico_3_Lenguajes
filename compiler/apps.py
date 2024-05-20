import lexer_python_rules,lexer_java_rules, lexer_js_rules
import ply.lex as lex
from flask import Flask, render_template, request

app = Flask(__name__)


# Construir los analizadores léxicos
lexer_python = lex.lex(module=lexer_python_rules)
lexer_java = lex.lex(module=lexer_java_rules)
lexer_js = lex.lex(module=lexer_js_rules)

# Función para analizar el código fuente
def analizar(codigo, lenguaje):
    tokens = []
    if lenguaje == 'python':
        lexer_python.input(codigo)
        while True:
            tok = lexer_python.token()
            if not tok:
                break
            tokens.append((tok.type, tok.value))
    elif lenguaje == 'java':
        lexer_java.input(codigo)
        while True:
            tok = lexer_java.token()
            if not tok:
                break
            tokens.append((tok.type, tok.value))
    elif lenguaje == 'javascript':
        lexer_js.input(codigo)
        while True:
            tok = lexer_js.token()
            if not tok:
                break
            tokens.append((tok.type, tok.value))
    return tokens

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        codigo = request.form['codigo']
        lenguaje = request.form['lenguaje']
        tokens = analizar(codigo, lenguaje)
        return render_template('resultado.html', tokens=tokens, lenguaje=lenguaje)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)