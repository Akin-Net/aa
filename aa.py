#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Cliente para enviar mensagens ao servidor
# http://wiki.nosdigitais.teia.org.br/AA_0.0.1

import urllib, urllib2
import sys
import os
from time import time, strftime
from threading import Timer

instrucoes = """
AA

Using:

   aa start             = starts the work session of the day
   aa alert <resumo>    = alerts what he is doing now
   aa stop              = stops the work session of the day
  
"""

def comeca():
  """Start the session"""
  home = os.getenv("HOME")
  f = open(home+"/.aa.txt", "w")
  f.close()

def termina():
  """Stop the session"""
  home = os.getenv("HOME")
  f = open(home+"/.aa.txt", "r")
  str = f.readline()
  while (len(str) > 0):
    str = str.split('\n')
    str = str[0].split(',')
    #msg = {'user': USER_MACAMBIRA, 'log': str[0]+'::'+str[1]}
    msg = {'user': '1', 'log': str[0]+'::'+str[1]}
    dados = urllib.urlencode(msg)
    # envia a string
    req = urllib2.Request('http://nightsc.com.br/aa/novo_log.php', dados)
    res = urllib2.urlopen(req)
    pagina = res.read()
    str = f.readline()

  res.close()

def direciona(args):
    """Parse AA arguments"""
    #talvez usar o argparse?
    if args[0] in ['start','inicio', 'inicia', 'início', 'begin']:
        comeca()
        log('start')
        print '[AA] Your session has started. Happy hacking!'
    elif args[0] in ['stop','fim', 'finaliza', 'termina', 'end']:
        # registra hora de fim
        log('stop')
        termina()
        print '[AA] You ended the sesssion and published at http://nightsc.com.br/aa. CYA!'
    elif args[0] in ['alert','informa', 'marca', 'anota', 'msg'] and args[1]:
        # registra marca no registro iniciado (corrente)
        #FIXME só funciona se a mensagem estiver entre parenteses:
        log("alert "+sys.argv[2:][0])
        print '[AA] New alert: "%s" logged.' % sys.argv[2:][0]
    else:
        print 'Opção "%s" inválida!' % args[0]

def log(msg):
    """Saves messages on the ~/.aa.txt temp file"""

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
