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

   aa start             = avisa que começou as atividades do dia
   aa alert <resumo>    = anota o que está fazendo em uma mensagem curta
   aa stop              = avisa que terminou as atividades do dia
  
"""

def direciona(args):
    """ Trata os argumentos do AA """
    #talvez usar o argparse?
    if args[0] in ['start','inicio', 'inicia', 'início', 'begin']:
        # registra hora de início
        log('start')
        pass
    elif args[0] in ['stop','fim', 'finaliza', 'termina', 'end']:
        # registra hora de fim
        log('stop')
        pass
    elif args[0] in ['alert','informa', 'marca', 'anota', 'msg'] and args[1]:
        # registra marca no registro iniciado (corrente)
        #FIXME só funciona se a mensagem estiver entre parenteses:
        log("alert,"+sys.argv[2:][0])
        pass
    else:
        print 'Opção "%s" inválida!' % args[0]

def log(msg):
    """ Salva mensagens no arquivo temporario """

    home = os.getenv('HOME')
    f = open(home+"/.aa.txt","a")

    try:
        #escreve mensagem no arquivo com data/hora
        #FIXME definir melhor formato para data/hora
        f.writelines(strftime("%d-%m-%y %H-%M-%S")+","+msg+"\n")
    finally:
        f.close()
    return

if __name__=="__main__":

    if len(sys.argv) > 1:
        direciona(sys.argv[1:])
    else:
        print instrucoes
