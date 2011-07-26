#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import configparser
import io
import os
import sys

config = configparser.RawConfigParser()

def configura_default():
    config['user'] = {'nickname': None, 'email': None}
    __save()

def __save():
    with open(__get_config_file(), "w") as configfile:
        config.write(configfile)

def configura(params):
    config.read(__get_config_file())
    config['user'][params[0]] = params[1]
    #config.set('user', params[0], params[1])
    __save()

def get_config(param):
    config.read(__get_config_file())
    return config['user'][param]

def __get_config_file():
    return os.getenv('HOME')+'/.aaconfig'

if __name__ == "__main__":
    configura()
