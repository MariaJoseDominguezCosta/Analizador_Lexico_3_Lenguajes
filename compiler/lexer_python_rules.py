# module: lexer_python_rules.py
import ply.lex as lex
# Lista de tokens para Python
tokens = [
    'PALABRA_RESERVADA_PY',
    'IDENTIFICADOR_PY',
    'NUMERO_PY',
    'SUMA_PY',
    'RESTA_PY',
    'MULTIPLICACION_PY',
    'DIVISION_PY',
    'ASIGNACION_PY',
    'IGUAL_PY',
    'DIFERENTE_PY',
    'COMENTARIO_PY',
    'SIMBOLO_PY'
]

symbols = {'"', "+", "=", ",", "(", ")", "{", "}", "[", "]", "!"}

# Reglas para Python
t_SUMA_PY = r'\+'
t_RESTA_PY = r'-'
t_MULTIPLICACION_PY = r'\*'
t_DIVISION_PY = r'/'
t_ASIGNACION_PY = r'='
t_IGUAL_PY = r'=='
t_DIFERENTE_PY = r'!='
t_COMENTARIO_PY = r'\#.*'

def t_PALABRA_RESERVADA_PY(t):
    r'import|from|print|def|class|return|if|else|elif|for|while|in|not|and|or|True|False|None'
    return t

def t_IDENTIFICADOR_PY(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    return t

def t_NUMERO_PY(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_SIMBOLO_PY(t):
    r'[{}()\[\]]|,|"'
    if t.value not in symbols:
        print(f"Carácter inválido '{t.value}'")
        t.lexer.skip(1)
    return t

# Reglas comunes
t_ignore = ' \t\n'

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    
def t_error(t):
    print(f"Carácter inválido '{t.value[0]}'")
    t.lexer.skip(1)

lexer  = lex.lex()