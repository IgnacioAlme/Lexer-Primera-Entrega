import lex

resul_lexema = []
#Lista de tokens
tokens = (
    'IDENTIFICADOR',
    'NUMERO',
    'ASIGNAR',
    'CARACTER',

    'SUMA',
    'RESTA',
    'MULT',
    'DIV',
    'POT',
    'MOD',

    #Condicionales
    'SI',
    'SINO',
    #Ciclos
    'MIENTRAS',
    'PARA',
    #Lógica
    'AND',
    'OR',
    'NOT',
    'MENORQUE',
    'MAYORQUE',
    'MAYORIGUAL',
    'IGUAL',
    'MENORIGUAL',
    'DISTINTO',
    #Símbolos
    'NUMERAL',
    'PARIZQ',
    'PARDER',
    'CORIZQ',
    'CORDER',
    'LLAIZQ',
    'LLADER',

)

reservadas = (

)

#tokens = tokens+list(reservadas.values())

#Reglas de expresiones regulares
t_SUMA = r'\+'
t_RESTA = r'-'
t_MULT = r'\*'
t_DIV =  r'/'
t_MOD = r'\%'
t_POT = r'\*{2} | \^'

t_ASIGNAR = r'='

#Expresiones lógicas
t_AND = r'\&'
t_OR = r'\|{2}'
t_NOT = r'\!'
t_MENORQUE = r'<'
t_MAYORQUE = r'>'
t_PARIZQ = r'\('
t_PARDER = r'\)'
t_LLAIZQ = r'\{'
t_LLADER = r'\}'

#Caracteres ignorados
#t_ignorado = '\t'

def t_NUMERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Valor del entero muy largo %d", t.value)
        t.value = 0
    return t

def t_sino(t):
    r'sino'
    return t

def t_si(t):
    r'si'
    return t

def t_cadena(t):
    r'\"?(\w+ \ *\w*\d9 \ *)"?'



def t_comentario_unalinea(t):
    r'\/\/(.)*\n'
    t.lexer.lineno += 1
    print("Comentario de una linea.")

def t_error(t):
    global resul_lexema
    estado = "** Token no válido en la línea {:4} Valor {:16} Posición {:4}".format(str(t.lineno), str(t.value), str(t.lexpos))
    resul_lexema.append(estado)
    t.lexer.skip(1)

def t_CARACTER(t):
     r'[a-zA-Z]'
     return t

#Prueba de ingreso
def prueba(data):
    global resul_lexema

    analizador = lex.lex()
    analizador.input(data)

    resul_lexema.clear()
    while True:
        tok = analizador.token()
        if not tok:
            break
        estado = "Linea {:4} Tipo {:16} Valor {:16} Posicion {:4}/n".format(str(tok.lineno), str(tok.type), str(tok.value), str(tok.lexpos))
        resul_lexema.append(estado)
    return resul_lexema


#Iniciando el analizador lexico
analizador = lex.lex()

if __name__ == '__main__':
    while True:
        data = input("ingrese: ")
        prueba(data)
        print(resul_lexema)