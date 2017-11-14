#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Test secrets.py
'''

import pytest
from pysquare.secrets import get_secrets


class Test_Get_Secrets_Method(object):
	'''
	Test of get_secrets()
	'''
	def test_get_secrets_reads_json(self):
		'''
		Test get_secret method returns setting variables from JSON file.
		'''
		secret_auth = get_secrets('ACCESS_TOKEN')
		assert secret_auth == get_secrets('ACCESS_TOKEN')

	def test_get_secrets_value_pair_error(self):
		'''
		Test get_secret method error reporting.
		'''
		secret_error = get_secrets('MY_NAME')
		assert secret_error == 'JSON name/value pair not found. Please check json file and set the MY_NAME name/value pair'
