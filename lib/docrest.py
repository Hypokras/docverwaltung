#!/usr/bin/env python
# -*- coding: utf-8 -*-

import filehelper

def errmsg(message, error=1):
	return {
		'meta': {
			'version': '0.0.2',
			'error': error,
			'error_message': message
		}
	}

def okmsg():
	return {
		'meta': {
			'version': '0.0.2',
			'error': '0'
		}
	}

def doit(data, name, method='GET'):
	# name = /store/action or /store/image/name or "/list"
	uri = name.split('/')
	uri.remove('')
	
	#get stores
	stores = filehelper.getStores()
	
	if len(uri) == 1:
		# /list
		if uri[0] == 'list':
			returnmsg = okmsg()
			returnmsg['store'] = stores
			print returnmsg
			return returnmsg
		else:
			return errmsg('unknown store or action')
	elif len(uri) == 2:
		# /?/list
		if uri[1] == 'list':
			# /store/list
			if uri[0] in stores:
				returnmsg = okmsg()
				returnmsg['images'] = filehelper.getImages(uri[0])
				return returnmsg
			else:
				return errmsg('unknown store')
	else:
		return errmsg('unknown action')
			
	
	
