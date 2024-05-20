# module : lexer_js_rules.py
import ply.lex as lex
# Lista de tokens para JavaScript
tokens = [
    'PALABRA_RESERVADA_JS',
    'IDENTIFICADOR_JS',
    'NUMERO_JS',
    'SUMA_JS',
    'RESTA_JS',
    'MULTIPLICACION_JS',
    'DIVISION_JS',
    'ASIGNACION_JS',
    'IGUAL_JS',
    'DIFERENTE_JS',
    'COMENTARIO_JS'
]

symbols = {'"', "+", "=", ",", "(", ")", "{", "}", "[", "]", ";", "!"}

# Reglas para JavaScript
t_SUMA_JS = r'\+'
t_RESTA_JS = r'-'
t_MULTIPLICACION_JS = r'\*'
t_DIVISION_JS = r'/'
t_ASIGNACION_JS = r'='
t_IGUAL_JS = r'=='
t_DIFERENTE_JS = r'!='
t_COMENTARIO_JS = r'//.*'

def t_PALABRA_RESERVADA_JS(t):
    r'var|let|const|function|return|if|else|switch|case|default|break|continue|for|while|do|try|catch|finally|throw|new|this|true|false|null|undefined'
    return t

def t_IDENTIFICADOR_JS(t):
    r'[a-zA-Z_$][a-zA-Z_0-9$]*'
    return t

def t_NUMERO_JS(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value)
    return t

def t_SIMBOLO_JS(t):
    r'[{}()\[\]]|,|;|"'
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
    print(f"Caracter inválido '{t.value[0]}'")
    t.lexer.skip(1)
    
lexer = lex.lex()
