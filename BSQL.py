#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
An attempt at creating a SQL-like database in python, without using any SQL-like packages
Author: Bobby McDonnell
Date: 12/17/2015
"""
# create a table class
# create a db class
# create sql type commands to navigate tables and db
 
"""
a table will be a dictionary variable, whose keys will be the column names, the values
will be lists (of equal lenght between keys) with the row elements. the lists will contain
tuple pairs, where the first element will be the primary id and the second element will be
the actual value.
 
later, to mimic salesforce, could create an OO-like structure where the records will be the
objects (will define what an obect is later...)
"""

 
 
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
 
    def __init__(self, record_list):
        self.table = record_list
        self.cur_index = 0
        self.current_position = record_list[self.cur_index]
        self.last_index = len(self.table)
    # make the table itterable
    def __iter__(self):
        return self
    def __next__(self):
 
    #
    def insert(self,var_names,var_types):
        self.var_names = var_names
        self.var_types = var_types
 
    def select(self,...):
        pass
 
class record(table):
   
    def __init__(self,...):
        pass

