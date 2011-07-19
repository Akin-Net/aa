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
        log('start')
        # registra hora de início
        pass
    elif args[0] in ['stop','fim', 'finaliza', 'termina', 'end']:
        log('stop')
        # registra hora de fim
        pass
    elif args[0] in ['alert','informa', 'marca', 'anota', 'msg']:
        log('alert')
        # registra marca no registro iniciado (corrente)
        pass
    else:
        print 'Opção "%s" inválida!' % args[0]

def log(msg):
    f = open("/tmp/.aa.txt","a")
    try:
        f.writelines(msg+"\n")
    finally:
        f.close()
    return


if __name__=="__main__":
    if len(sys.argv) > 1:
        direciona(sys.argv[1:])
    else:
        print instrucoes
