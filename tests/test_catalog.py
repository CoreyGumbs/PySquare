#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Test secrets.py
'''

import pytest
import squareconnect
from pysquare.secrets import get_secrets
from pysquare.catalog import Catalog


class Test_PySquare_Catalog(object):
	'''
	Test PySquare_Catalog Class.
	'''

	def test_catalog_class(self):
		self.catalog_category = Catalog()
		assert self.catalog_category.access_token == get_secrets('ACCESS_TOKEN')

		
