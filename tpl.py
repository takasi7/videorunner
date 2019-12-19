#! /usr/local/bin/python3

import os
import re
import codecs

def load_template(tpl_file_path):
	f = codecs.open(tpl_file_path,codec='utf-8')
	string = f.read()
	close(f)
	return string

def replace_keyword(template,dic):
	
	
