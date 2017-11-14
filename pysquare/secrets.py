#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Protects all API keys and allows them to be called when needed, where needed.
'''

import os
import json
import squareconnect

#Global Paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
security_key = os.path.join(BASE_DIR, 'secrets.json')

def get_secrets(setting):
	try:
		with open(security_key) as f:
			secrets = json.loads(f.read())

		return secrets[setting]
	except KeyError:
		return 'JSON name/value pair not found. Please check json file and set the {0} name/value pair'.format(setting)
