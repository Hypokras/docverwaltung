#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import interface_0_0_1

def test(value):
	return """\
{
	"meta": {
	"error": 0,
	"version": "0.0.1",
	"typ": "test"
	}
}
	"""
	
def dosomething(message):

	# checks if data has been received and calls corresponding version method


	if len(message) == 0:
		return {
	"meta": {
		"error": 1,
		"error_message": "no data received",
		"version": "0.0.1"
	}
}
		
	message = json.loads(message)
	if not 'meta' in list(message):
		return {
	"meta": {
		"error": 1,
		"error_message": "unknown format",
		"version": "0.0.1"
	}
}

	if message['meta']['version'] == "0.0.1":
		return interface_0_0_1.dosomething(message)
	else:
		return {
	"meta": {
		"error": 1,
		"error_message": "unknown version: " + message['meta']['version'],
		"version": "0.0.1"
	}
}

	
