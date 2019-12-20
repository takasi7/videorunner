#! /usr/local/bin/python3

import sqlite3
import gp

class DataBase :
	def __init__(self,dbfile=gp.DB):
		self.conn = sqlite3.connect(dbfile)
		self.cur = self.conn.cursor()
	
	def __del__(self):
		self.conn.close
	
	def add(record):
		pass
	
	def get(record):
		pass
	
	def update(record):
		pass
	
	def exesql(sql):
		pass
	
	
	
