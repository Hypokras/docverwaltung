#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json

class jsonmessage(object):
	# Konstruktor
	def __init__(self):
		self.__message = ""
		self.__workdir = os.path.join(os.path.dirname(__file__), '..', 'ExampleFiles', 'workdir')
		self.__returnmessage = {
														"meta": {
															"error": 1,
															"error_message": "shit happens",
															"version": "0.0.1"
															}
														}
		self.__versions = ["0.0.1"]
	# Destruktor	
	def __del__(self):
		pass
	# Getter	
	def workdir(self)
		return self.__workdir
	# Setter	
	def setWorkdir(self, workdir)
		if os.path.isdir(workdir):
			self.__workdir = workdir
		else:
			return "workdir does not exist"
	# Property Attribute
	Workdir = property(workdir, setWorkdir)
	# Methods
	def validate(message):
		if len(message) == 0:
			self.__returnmessage['meta']['error_message'] = "no data received"
			return self.__returnmessage
		try:
			self.__message = json.loads(message)
		except:
			self.__returnmessage['meta']['error_message'] = "could not parse message"
			return self.__returnmessage
		if not 'meta' in list(self.__message):
			self.__returnmessage['meta']['error_message'] = "unknown format"
			return self.__returnmessage
		if not 'version' in list(self.__message['meta']):
			self.__returnmessage['meta']['error_message'] = "unknown format"
			return self.__returnmessage
		if self.__message['meta']['version'] not in self.__versions:
			self.__returnmessage['meta']['error_message'] = "unknown version: " + str(self.__message['meta']['version'])
			return self.__returnmessage

		if self.__message['meta']['version'] == "0.0.1":
			return __validate_0_0_1()
		else:
			self.__returnmessage['meta']['error_message'] = "unknown error"
			return self.__returnmessage
			
			
	def __validate_0_0_1(self):
		action = ['list', 'modify']
		store = self.__workdir
		if not 'action' in self.__message['meta']:
			self.__returnmessage['meta']['error_message'] = "no action defined"
			return self.__returnmessage
		elif not self.__message['meta']['action'] in action:
			self.__returnmessage['meta']['error_message'] = "unknown action: " + str(self.__message['meta']['action'])
			return self.__returnmessage
		elif not 'store' in self.__message['meta']:
			self.__returnmessage['meta']['error_message'] = "no store defined"
			return self.__returnmessage
		elif not self.__message['meta']['store'] in os.listdir(store)
			self.__returnmessage['meta']['error_message'] = "unknown store"
			return self.__returnmessage
		elif self.__message['meta']['action'] == "list":
			__validate_0_0_1_list()
		
		
	def validate_0_0_1_list(self):
		contenttype = ['image/tiff','image/png','image/jpeg']
		limit = [1, 999]
		start = [0, 999]
		store = os.listdir(workdir)
		width = [1, 2550]
		height = [1, 3300]
		action = ['list']
		error_message = ""
	
		if not message['meta']['content-type'] in contenttype:
			error_message = error_message + ", Unknown content-type: " + message['meta']['content-type']
		
		if not message['meta']['limit'] in range(limit[0], limit[1]):
			error_message = error_message + ", Limit out of range: " + str(message['meta']['limit'])
		
		if not message['meta']['start'] in range(start[0], start[1]):
			error_message = error_message + ", Start out of range: " + str(message['meta']['start'])
	
		if not message['meta']['store'] in store:
			error_message = error_message + ", Unknown store: " + message['meta']['store']
		
		if not message['meta']['width'] in range(width[0], width[1]):
			error_message = error_message + ", Width out of range: " + str(message['meta']['width'])
		
		if not message['meta']['height'] in range(height[0], height[1]):
			error_message = error_message + ", Height out of range: " + str(message['meta']['height'])
	
		if not message['meta']['action'] in action:
			error_message = error_message + ", Unknown action: " + message['meta']['action']
		return error_message
