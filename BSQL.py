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

class BSQL(object):
    # a database is a collection of tables
    # table_count = 0
    # table_collection = {}
 
    def __init__(self):
        pass
 
    def create_table(self, name):
        if(table_collection.has_key(name)):
            return None
        else:
            table_collection.update({name:table()})

