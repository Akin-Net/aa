#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#-----------------------------------------------------------------------------
# Copyright 2011 Lab Macambira
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>
#-----------------------------------------------------------------------------

# Cliente para enviar mensagens ao servidor
# http://wiki.nosdigitais.teia.org.br/AA_0.0.1

import urllib.request
import urllib.parse
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
  alertas = f.read().splitlines()
  f.close()
  for alerta in alertas:
    # prepare the string
    alerta = alerta.split(',')
    msg = {'user': os.getenv('NICKNAME'), 'log': alerta[0]+'::'+alerta[1]}
    dados = urllib.parse.urlencode(msg)
    # sends the string
    print("Sending:",alerta[1])
    req = urllib.request.Request('http://nightsc.com.br/aa/novo_log.php',
                                 dados.encode('ascii'))
    res = urllib.request.urlopen(req)
    #pagina = res.read()
    res.close()


def direciona(args):
    """Parse AA arguments"""
    #talvez usar o argparse?
    if args[0] in ['start','inicio', 'inicia', 'início', 'begin']:
        comeca()
        log('start')
        print('[AA] Your session has started. Happy hacking!')
    elif args[0] in ['stop','fim', 'finaliza', 'termina', 'end']:
        # registra hora de fim
        log('stop')
        termina()
        print('[AA] You ended the sesssion and published at ' \
        'http://nightsc.com.br/aa. CYA!')
    elif args[0] in ['alert','informa', 'marca', 'anota', 'msg'] and args[1]:
        # registra marca no registro iniciado (corrente)
        msg = ''.join([pal + " " for pal in sys.argv[2:]])
        msg = msg.strip()
        log("alert " + msg)
        print('[AA] New alert: "%s" logged.' % msg)
    else:
        print('Opção "%s" inválida!' % args[0])

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


class Sentinela(object):
    """Warnings from time to time"""

    def __init__(self, minutos=15):
        """Give a warning after each minutos"""
        self.minutos = minutos
        self.timer = Timer(self.minutos*60, self.avisar)

    def iniciar(self):
        """Starts to count"""
        self.timer.start()

    def parar(self):
        """Stops to count"""
        self.timer.cancel()

    def avisar(self):
        """Gives the warning and restarts the Timer"""
        print("hello, world")
        self.timer = Timer(self.minutos*60, self.avisar)
        self.timer.start()


s = Sentinela(0.1)
#s.iniciar()


if __name__=="__main__":
    if len(sys.argv) > 1:
        direciona(sys.argv[1:])
    else:
        print(instrucoes)
