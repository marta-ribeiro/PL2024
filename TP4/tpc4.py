import sys
import re
import ply.lex as lex

# List of token names.   This is always required
tokens = (
    'SELECT',
    'FROM',
    'WHERE',
    'ID',
    'NOME',
    'SALARIO',
    'EMPREGADOS',
    'NUMBER',
    'BIGGEREQ',
    'COMMA',
)

# Regular expression rules for simple tokens
t_SELECT    = r'(?i:select)'
t_FROM   = r'(?i:from)'
t_WHERE   = r'(?i:where)'
t_ID  = r'(?i:id)'
t_NOME  = r'(?i:nome)'
t_SALARIO  = r'(?i:salario)'
t_EMPREGADOS  = r'(?i:empregados)'
t_BIGGEREQ  = r'>='
t_COMMA  = r','

# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)    
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Test it out
data = '''
SELECT id, nome, salario FROM empregados
    WHERE salario >= 820
'''

# Give the lexer some input
lexer.input(data)

for tok in lexer:
    print(tok.type, tok.value, tok.lineno, tok.lexpos)