#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Controle. Envia alertas para o aad.

# aad <-------- aaa

import sys
from socket import *

if __name__=="__main__":
    # conexão com o aad X
    host = sys.argv[1]
    port = 4040
    buf = 1024
    addr = (host,port)

    UDPSock = socket(AF_INET,SOCK_DGRAM)

    data = sys.argv[2]
    if not data:
        print 'Falha no envio!'
    else:
        if(UDPSock.sendto(data,addr)):
            print 'Alerta "%s" enviado para "%s"' % (data, host)

    # Close socket
    UDPSock.close()
