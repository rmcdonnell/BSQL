#!/usr/bin/python
# -*- coding: utf-8 -*-
# python 3.5.1
"""
Author: Bobby McDonnell
Date: 12/17/2015
"""
# create a table class
# create a db class
# create sql type commands to navigate tables and db

class BQL(object):
    # a database is a collection of tables
    table_count = 0
    table_collection = {}
 
    def __init__(self):
        pass
 
    def create_table(self, name):
        if(table_collection.has_key(name)):
            return None
        else:
            table_collection.update({name:table()})
 
class table(BSQL):
    # create tablename (stuff int, things, str, ...)
    # Inputs:
    # nametype ~ tuple (or list of tuples) of length 2, (str name, type)
    def __init__(self, nametype):
        self._nametype = nametype
    
    # make the table itterable
    def __iter__(self):
        return self

    def __next__(self):

    #
    def insert(self,var_names,var_types):
        self.var_names = var_names
        self.var_types = var_types
 
    def select(self):
        pass
 
class record(table):
   
    def __init__(self):
        pass

