#!/usr/bin/python
# -*- coding: utf-8 -*-
# python 3.5.1
"""
Author: Bobby McDonnell
Date: 12/17/2015

Heirarchy:
BSQL > database > table > record
"""
# create a table class
# create a db class
# create sql type commands to navigate tables and db

from database import database


class table(database):
    # create tablename (stuff int, things, str, ...)
    # Inputs:
    # nametype ~ tuple (or list of tuples) of length 2, (str name, type)
    def __init__(self):
        pass
        # self._nametype = nametype
    
    # make the table itterable
    def __iter__(self):
        return self

    def __next__(self):
        pass
    #
    def insert(self, var_names, var_types):
        self.var_names = var_names
        self.var_types = var_types
 
    def select(self):
        pass