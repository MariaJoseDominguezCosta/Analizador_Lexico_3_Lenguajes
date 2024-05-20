# module:lexer_java_rules.py
import ply.lex as lex

# Lista de tokens para Java
tokens = [
    "PALABRA_RESERVADA_JAVA",
    "IDENTIFICADOR_JAVA",
    "NUMERO_JAVA",
    "SUMA_JAVA",
    "RESTA_JAVA",
    "MULTIPLICACION_JAVA",
    "DIVISION_JAVA",
    "ASIGNACION_JAVA",
    "IGUAL_JAVA",
    "DIFERENTE_JAVA",
    "COMENTARIO_JAVA",
    "SIMBOLO_JAVA"
]

symbols = {'"', "+", "=", ",", "(", ")", "{", "}", "[", "]", ";", "!"}

# Reglas para Java
t_SUMA_JAVA = r"\+"
t_RESTA_JAVA = r"-"
t_MULTIPLICACION_JAVA = r"\*"
t_DIVISION_JAVA = r"/"
t_ASIGNACION_JAVA = r"="
t_IGUAL_JAVA = r"=="
t_DIFERENTE_JAVA = r"!="
t_COMENTARIO_JAVA = r"//.*"


def t_PALABRA_RESERVADA_JAVA(t):
    r"import|package|public|private|protected|class|interface|extends|implements|static|final|void|int|double|float|boolean|char|byte|short|long|if|else|switch|case|default|break|continue|for|while|do|try|catch|finally|throw|returns|new|this|super|true|false|null"
    return t


def t_IDENTIFICADOR_JAVA(t):
    r"[a-zA-Z_$][a-zA-Z_0-9$]*"
    return t


def t_NUMERO_JAVA(t):
    r"\d+(\.\d+)?"
    t.value = float(t.value)
    return t


# Reglas comunes
t_ignore = " \t\n"


# Define a rule so we can track line numbers
def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)

def t_SIMBOLO_JAVA(t):
    r'[{}()\[\]]|,|;|"'
    if t.value not in symbols:
        print(f"Carácter inválido '{t.value}'")
        t.lexer.skip(1)
    return t

def t_error(t):
    errors = []
    errors.append({"token": t.value[0], "line": t.lexer.lineno})
    print(f"Símbolo inválido '{t.value[0]}' en la línea {t.lexer.lineno}")
    t.lexer.skip(1)


lexer = lex.lex()
