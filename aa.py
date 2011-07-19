#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Cliente para enviar mensagens ao servidor
# http://wiki.nosdigitais.teia.org.br/AA_0.0.1

import sys
import os
from time import time

instrucoes = """
Administrador da Ágora

Uso:

   aa start            = avisa que começou as atividades do dia
   aa alert <resumo>    = anota o que está fazendo em uma mensagem curta
   aa stop               = avisa que terminou as atividades do dia
  
"""

def direciona(args):
    if args[0] in ['inicio', 'inicia', 'início', 'start', 'begin']:
        # registra hora de início
        pass
    elif args[0] in ['fim', 'finaliza', 'termina', 'end']:
        # registra hora de fim
        pass
    elif args[0] in ['informa', 'marca', 'anota', 'msg']:
        # registra marca no registro iniciado (corrente)
        pass
    else:
        print 'Opção "%s" inválida!' % args[0]

if __name__=="__main__":
    if len(sys.argv) > 2:
        direciona(sys.argv[1:])
    else:
        print instrucoes
