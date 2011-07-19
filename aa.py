#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Cliente para enviar mensagens ao servidor
# http://wiki.nosdigitais.teia.org.br/AA_0.0.1

import sys
import os
from time import time, strftime
from threading import Timer

instrucoes = """
Administrador da Ágora

Uso:

   aa start            = avisa que começou as atividades do dia
   aa alert <resumo>    = anota o que está fazendo em uma mensagem curta
   aa stop               = avisa que terminou as atividades do dia
  
"""

def direciona(args):
    """ Trata os argumentos do AA """
    if args[0] in ['inicio', 'inicia', 'início', 'start', 'begin']:
        # registra hora de início
        log('start')
        pass
    elif args[0] in ['stop','fim', 'finaliza', 'termina', 'end']:
        # registra hora de fim
        log('stop')
        pass
    elif args[0] in ['alert','informa', 'marca', 'anota', 'msg']:
        # registra marca no registro iniciado (corrente)
        log('alert')
        pass
    else:
        print 'Opção "%s" inválida!' % args[0]

def log(msg):
    """ Salva mensagens no arquivo temporario """

    f = open(home+"/.aa.txt","a")

    try:
        #escreve mensagem no arquivo com data/hora
        #FIXME definit melhor formato para data/hora
        f.writelines(strftime("%d-%m-%y %H-%M-%S")+","+msg+"\n")
    finally:
        f.close()
    return

if __name__=="__main__":
    global home
    home = os.getenv('HOME')

    if len(sys.argv) > 1:
        direciona(sys.argv[1:])
    else:
        print instrucoes
