import lex
from lex import TOKEN

resul_lexema = []
#Lista de tokens
tokens = [
    'VARIABLE',
    'NUMERO',
    'CADENA',
    'ASIGNAR',
    'COMENTARIO',

    #Operadores
    'SUMA',
    'RESTA',
    'MULT',
    'DIV',
    'POT',
    'MOD',
    'PP',
    'MM',

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
    'ESPACIO',
    'PUNTOCOMA',

    #Especiales
    'VERT',
    'NEWLINE',
    'SP',
    'CARR'
]

reservadas = {
    #'_div'      :'DIV',
    #'_mod'      :'MOD',
    '_o'        :'O',
    'leer'      :'LEER',
    'escribir'  :'ESCRIBIR',
    'si'        :'SI',
    'entonces'  :'ENTONCES',
    'sino'      :'SINO',
    'fin_si'    :'FINSI',
    'mientras'  :'MIENTRAS',
    'hacer'     :'HACER',
    'fin_mientras':'FINMIENTRAS',
    'repetir'   :'REPETIR',
    'hasta_que' :'HASTAQUE',
    'para'      :'PARA',
    'hasta'     :'HASTA',
    'fin_para'  :'FINPARA',
    'segun'     :'SEGUN',
    'fin_segun' :'FINSEGUN',
    'accion'    :'ACCION',
    '_es'       :'ES',
    'fin_accion':'FINACCION',
    'proceso'   :'PROCESO',
    'ambiente'  :'AMBIENTE'
}

tokens = tokens+list(reservadas.values())

#Reglas de expresiones regulares
t_SUMA = r'\+'
t_PP = r'\+\+'
t_RESTA = r'-'
t_MM = r'--'
t_MULT = r'\*'
t_DIV =  r'/'
t_MOD = r'\%'
t_POT = r'\*{2} | \^'
 

t_ASIGNAR = r'\:='

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
t_ignore = '\t'
t_ignore_VERT = r'[\v]'
t_ignore_NEWLINE = r'[\n]'
t_ignore_SP = r'[\s]'
t_ignore_CARR = r'[\r]'

def t_ccode_nonspace(t):
 r'\s+'
 pass

#Si se descomenta esto solo reconoce las palabras reservadas
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reservadas.get(t.value.lower(),'ID')    #Revisa las palabras reservadas
    return t


def t_NUMERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Valor del entero muy largo %d", t.value)
        t.value = 0
    return t

def t_CADENA(t):
     r'"[a-zA-Z/0-9._+áéíóú,ñ:"()#¿?!¡:\\ ]+"'
     return t


def t_COMENTARIO(t):
    r'\#.*'
    pass
    #No devuleve ningún valor

def t_error(t):
    global resul_lexema
    estado = "** Token no válido en la línea [{:4}] Valor [{:16}] Posición [{:4}]".format(str(t.lineno), str(t.value), str(t.lexpos))
    resul_lexema.append(estado)
    t.lexer.skip(1)

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
        estado = "***Linea {:4} Tipo {:16} Valor {:16} Posicion {:4}***".format(str(tok.lineno), str(tok.type), str(tok.value), str(tok.lexpos))
        resul_lexema.append(estado)
    return resul_lexema


#Iniciando el analizador lexico
analizador = lex.lex()

if __name__ == '__main__':
    while True:
        data = input("ingrese: ")
        prueba(data)
        print(resul_lexema)