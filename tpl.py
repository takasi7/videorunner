#! /usr/local/bin/python3

import os
import re
import codecs
import gp

def load_template(tpl_file_path):
	f = codecs.open(tpl_file_path,codec='utf-8')
	string = f.read()
	close(f)
	return string

def replace_data(tpl, dic):
	for key in dic.keys():
		val = dic[key]
		if type(val) is str:
			tpl = tpl.replace('__'+key+'__',val)
	return tpl

def recursive(string, dic):
	repstring = ''
	m = re.search('<!--#([a-zA-Z0-9_\-]+)#-->(.*)<!--##-->', string, flags=re.DOTALL)
	if m != None:
		key = m.group(1)
		lists = None
		retpstring = ''
		if key in dic and type(dic[key]) is list:
			lists = dic[key]
		for obj in lists:
			repstring += recursive(m.group(2),obj)
		ret = re.sub('<!--#[a-zA-Z0-9_\-]+#-->(.*)<!--##-->', repstring, string, flags=re.DOTALL)
		ret = replace_data(ret,dic)
	else:
		ret = replace_data(string, dic)
		
	return ret


def exstring(template,dic):
	ret = recursive(template,dic)
	return ret


if __name__ == '__main__':
	html = '''
		<html><head></head>
		<body>
		<p>__TITLE__</p>
		<!--#table#-->
		<table>
		<tr><td>Song Name</td><td>Artist</td></tr>
		<!--#item#--><tr><td>__SONG__</td><td>__ARTIST__</td></tr><!--##-->
		</table>
		<!--##-->
		</body>
		</html>
		'''
	
	data = {'TITLE':'best songs',
		'table':[
				{'item':[
						{'SONG':'eternal blaze','ARTIST':'mizuki nana'},
						{'SONG':'fearless hero','ARTIST':'mizuki nana'},
						{'SONG':'Rock-MODE18','ARTIST':'LiSA'}
					]
				},
				{'item':[
						{'SONG':'cloudy heart','ARTIST':'boowy'},
						{'SONG':'Raspberry Dream','ARTIST':'rebecca'}
					]
				}
			]
		}
	print(exstring(html,data))

	
