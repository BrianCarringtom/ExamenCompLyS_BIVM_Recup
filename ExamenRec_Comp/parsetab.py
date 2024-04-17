
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND ASIGNAR BODY COMDOB CORDER CORIZQ DISTINTO DIV DOCTYPE DOSPUNTO ENTERO GET HEAD HTML IDENTIFICADOR IGUAL INCLUDE INT LLADER LLAIZQ MAYORDER MAYORIGUAL MAYORIZQ MAYORQUE MENORIGUAL MENORQUE MIENTRAS MINUSMINUS MODULO MULT NAMESPACE NOT NUMERAL OR PARDER PARIZQ PLUSPLUS POTENCIA PUNTO PUNTOCOMA RESERVADA RESTA RETURN SI SINO STD SUMA SYSTEM TITLE USING VOID\n    expresion : MENORQUE NOT RESERVADA RESERVADA MAYORQUE MENORQUE RESERVADA MAYORQUE MENORQUE RESERVADA MAYORQUE MENORQUE RESERVADA MAYORQUE IDENTIFICADOR IDENTIFICADOR IDENTIFICADOR MENORQUE DIV RESERVADA MAYORQUE MENORQUE DIV RESERVADA MAYORQUE MENORQUE RESERVADA MAYORQUE MENORQUE IDENTIFICADOR MAYORQUE IDENTIFICADOR IDENTIFICADOR NOT MENORQUE DIV IDENTIFICADOR MAYORQUE MENORQUE DIV RESERVADA MAYORQUE MENORQUE DIV RESERVADA MAYORQUE MAYORQUE\n    '
    
_lr_action_items = {'MENORQUE':([0,6,9,12,18,22,26,29,35,39,43,],[2,7,10,13,19,23,27,30,36,40,44,]),'$end':([1,48,],[0,-1,]),'NOT':([2,34,],[3,35,]),'RESERVADA':([3,4,7,10,13,20,24,27,41,45,],[4,5,8,11,14,21,25,28,42,46,]),'MAYORQUE':([5,8,11,14,21,25,28,31,38,42,46,47,],[6,9,12,15,22,26,29,32,39,43,47,48,]),'IDENTIFICADOR':([15,16,17,30,32,33,37,],[16,17,18,31,33,34,38,]),'DIV':([19,23,36,40,44,],[20,24,37,41,45,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expresion':([0,],[1,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expresion","S'",1,None,None,None),
  ('expresion -> MENORQUE NOT RESERVADA RESERVADA MAYORQUE MENORQUE RESERVADA MAYORQUE MENORQUE RESERVADA MAYORQUE MENORQUE RESERVADA MAYORQUE IDENTIFICADOR IDENTIFICADOR IDENTIFICADOR MENORQUE DIV RESERVADA MAYORQUE MENORQUE DIV RESERVADA MAYORQUE MENORQUE RESERVADA MAYORQUE MENORQUE IDENTIFICADOR MAYORQUE IDENTIFICADOR IDENTIFICADOR NOT MENORQUE DIV IDENTIFICADOR MAYORQUE MENORQUE DIV RESERVADA MAYORQUE MENORQUE DIV RESERVADA MAYORQUE MAYORQUE','expresion',47,'p_expresion','analizador_sintactico.py',9),
]