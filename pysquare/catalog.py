#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
PySquare Catalog Class.
'''

from .secrets import get_secrets

class Catalog(object):
	'''
	Constructor
	'''
	def __init__(self):
		self.access_token = get_secrets('ACCESS_TOKEN')